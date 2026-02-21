"""

The input parameters are:
- user_info: a dictionary contains the bio of the doctor, such as
    {
        "name": "Dr. John Doe", # the name of the doctor
        "email": "drjohndoe@clinic.com", # the email of the doctor
    }
- specialty: a string represents the specialty of the doctor, such as "Otolaryngology"
- note_content: a dictionary contains the content of the SOAP note, where the key is the section name and the value is the content of the section, such as
    {
        "Patient Name": "Betty",
        "Chief Complaint": "Ear pain",
        "History of Present Illness": "\n• Left-sided ear pain\n• No drainage noted\n• Intermittent hearing loss reported\n• Pain worsens with chewing\n• Inconsistent use of mouthpiece for teeth clenching\n• Pain relief when lying on contralateral side",
        "Social History": "\n• Occasional Reactive use for allergies\n• Allergy to salt",
        "The Review of Systems": "\n• Intermittent hearing loss\n• No swallowing issues\n• No nasal congestion\n• Allergies present, takes Reactive occasionally",
        "Current Medications": "\n• Reactive for allergies",
        "Allergies": "\n• Allergic to salt",
        "Physical Examination": "\n• Right ear canal clear\n• Right tympanic membrane intact\n• Right ear space aerated\n• Left ear canal normal\n• Left eardrum normal, no fluid or infection\n• Nose patent\n• Paranasal sinuses normal\n• Oral cavity clear\n• Tonsils absent\n• Good dentition\n• Pain along pterygoid muscles\n• Heart and lungs clear\n• No neck tenderness or lymphadenopathy",
        "Assessment and Plan": "Problem 1:\nEar pain\nDDx:\n• Temporomandibular joint disorder: Likely given the jaw pain, history of teeth clenching, and normal ear examination.\nPlan:\n- Ordered audiogram to check hearing\n- Advised to see dentist for temporomandibular joint evaluation\n- Recommended ibuprofen for pain\n- Suggested soft foods diet\n- Avoid chewing gum, hard candies, hard fruits, ice, and nuts\n- Follow-up if symptoms persist"
    }
- note_date: a string represents the date of the SOAP note, such as "2022-01-01"
"""

import json
from typing import Optional

from openai_chat import chat_content


def create_consult_letter(
    user_info: dict, specialty: str, note_content: dict[str, Optional[str]], note_date: str
) -> str:

    SOAP_note = ""
    for key in note_content:
        SOAP_note += f"The patients {key} is {note_content.get(key)}. \n "

    result = chat_content(
        messages = [
            #First message assigns responsibility to the system
            {
                "role": "system",
                "content": f"Your name is {user_info.get("name")} and your email is {user_info.get("email")}, your speciality is {specialty}\
                your job is the create a Consult Letter in response to a referring Family Doctor, \
                providing information about the referred patient's basic diagnosis, along with the treatment plan and recommendations. \
                The Consult Letter generation should be tailored by specialty. \
                You will be given a SOAP note that contains information to be included in the Consult Letter. \
                **Make sure to use all information provided in the SOAP note",
            },
            {
                "role": "user",
                "content": f"This is the SOAP note, delimited by ```: \
                    ```{SOAP_note}```\
                        ",
            },
            {
                "role": "user",
                #Misc. rules for the consult letter
                "content": f"Do not include any placeholders, \
                    Use only paragraphs \
                    The date of encounter is {note_date}, \
                    keep the exact words from the SOAP note",
            },
            {
                "role": "user",
                #Hard rules for consult letter consistency and structure
                "content": f"Include these sections: \
                    Start the Consult Letter the sentence with the format: Thank you for your referral of (Patient Name) for (Your Specialty) Consultation. (Patients Pronoun) was examined on (Examined Date). \
                    Inlude a sentence with the format: If you have any further questions or require additional information, please do not hesitate to contact me at {user_info.get("email")}. \
                    Include at the end of the Consult Letter: Sincerely, \n(Your Name) \n (Your Specialty) \n(Your Email), \
                ",
            }
        ]
    )
    return result
