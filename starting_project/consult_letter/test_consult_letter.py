from consult_letter import create_consult_letter
from openai_chat import chat_content

consult_letter_a = create_consult_letter(
        user_info={"name": "Dr. John Doe", "email": "drjohndoe@clinic.com"},
        specialty="Obstetrics & Gynecology (ObGyn)",
        note_date="2022/01/01",
        note_content={
            "Patient Name": "Jane",
            "Patient Age": None,
            "Gender": "female",
            "Chief Complaint": "OB consultation for pregnancy management with planned repeat cesarean section.",
            "History of Present Illness": None,
            "Past Medical History": "The patient had COVID-19 in 2021, after which she experienced heart pain, but subsequent evaluations by her family doctor and hospital visits confirmed that everything was okay.",
            "Past Surgical History": "The patient had a cesarean section in 2019 and an abortion due to a fetal health issue.",
            "Family History": None,
            "Social History": "Jane is employed part-time as a banker, working two to three days per week. She and her spouse reside in a non-specified location without nearby family support. However, they have a local friend network. Postpartum, Jane's mother will assist, and they intend to employ a babysitter for two months.",
            "Obstetric History": "The patient is currently pregnant with her third child. She has had one previous live birth via cesarean section and one abortion due to fetal health issues. Her first child was born slightly premature at approximately 37 weeks, weighing 2.5 kilograms.",
            "The Review of Systems": "The patient reports no asthma, heart problems, seizures, or migraines. She has experienced chest pain post-COVID-19 but has been evaluated and found to be in good health. She is currently active, engaging in pregnancy yoga once a week and walking when she feels able.",
            "Current Medications": None,
            "Allergies": "The patient is allergic to minocycline.",
            "Vital Signs": None,
            "Physical Examination": None,
            "Investigations": None,
            "Problem": "1. Previous cesarean section (654.21)",
            "Differential Diagnosis": None,
            "Plan": "• Scheduled repeat cesarean section at 39 weeks gestation\n• Instructed patient to present to City Medical Center for emergency cesarean section if labor begins prior to scheduled date\n• Advised patient to walk daily for 20 to 30 minutes to improve blood pressure and baby's health\n• Arranged follow-up appointment in three weeks, with subsequent visits every two weeks, then weekly as due date nears",
            "Surgery Discussion": "• Purpose of the Surgery: The purpose of the repeat cesarean section is to safely deliver the baby, given the patient's previous cesarean delivery and her choice for a planned cesarean this time.\n• Risks and Complications: The risks of cesarean section include bleeding, infection, or injury to the bladder or bowel. These risks are small but not zero.\n• Anesthesia: Spinal anesthesia will be used during the procedure, which will prevent pain but allow the patient to be awake.\n• Alternatives: N/A",
        }
    )

consult_letter_b = create_consult_letter(
        user_info = {
            "name": "Dr. Jane Smith",
            "email": "drjanesmith@pediatricsclinic.com",
        },
        specialty = "Pediatrics",
        note_content = {
            "Patient Name": "Emily",
            "Age": "3 years old",
            "Chief Complaint": "Cough",
            "History of Present Illness": "\n• Mild cough for 3 days\n• Throat feels phlegmy\n• No fever recorded\n• No known allergies\n• Increased coughing at night",
            "Development": "\n• Meeting all developmental milestones\n• Good interaction and play with peers\n• Growing well in height and weight",
            "Pregnancy History": "\n• Full-term birth\n• No complications during pregnancy or delivery\n• Health satisfactory at birth",
            "Nutritional History": "\n• Balanced diet with fruits, vegetables, and proteins\n• No nutritional deficiencies noted",
            "The Review of Systems": "\n• No fever\n• No difficulty breathing\n• No skin rashes\n• Occasional runny nose",
            "Current Medications": "\n• None",
            "Allergies": "\n• None known",
            "Physical Examination": "\n• Throat shows phlegm, no redness or swelling\n• Nasal passages clear\n• Lungs clear on auscultation\n• Heart sounds normal\n• No tenderness in the abdomen\n• No lymphadenopathy in neck\n• Vital signs normal",
            "Assessment and Plan": "Problem 1:\nCough\nDDx:\n• Likely viral upper respiratory infection\nPlan:\n- Prescribed nasal spray to relieve congestion\n- Advised increased fluid intake\n- Recommended over-the-counter cough syrup if needed\n- Suggested humidifier use at night to ease coughing\n- Follow-up visit in one week or if symptoms worsen"
        },
        note_date = "2023-10-03"
    )

def test_create_consult_letter():
    consult_letter = consult_letter_a

    result = chat_content(
        messages=[
            {
                "role": "system",
                "content": f"You are a professional medical assistant of Obstetrics & Gynecology (ObGyn), \
your job is to verify the content of consult letter",
            },
            {
                "role": "user",
                "content": f"""\
The consult letter is as following, delimited by ```:
```
{consult_letter}
```
""",
            },
            {
                "role": "user",
                "content": f"""\
Follow these test points when verify the consult letter:
- The letter shall have doctor's name "John Doe"
- The letter shall mention patient name as Jane, and the encounter happened at 2022/01/01
- The Patient had COVID-19 in 2021 with subsequent heart pain but found okay.
- The patient had a cesarean section in 2019 and an abortion due to a fetal health issue.
- Allergic to minocycline.
""",
            },
            {
                "role": "user",
                "content": "Write me PASS **ONLY** if the consult letter is correct, and FAIL with reason if not",
            },
        ]
    )
    assert result.upper() == "PASS"

def test_create_consult_letter2():
    consult_letter = consult_letter_b

    result = chat_content(
        messages=[
            {
                "role": "system",
                "content": f"You are a professional medical assistant of Pediatrics, \
your job is to verify the content of consult letter",
            },
            {
                "role": "user",
                "content": f"""\
The consult letter is as following, delimited by ```:
```
{consult_letter}
```
""",
            },
            {
                "role": "user",
                "content": f"""\
This is a sample example of what the consult letter could look like:
Thank you for your referral of Emily for Pediatrics Consultation. She was examined on October 3, 2023.

Emily, who is 3 years old, presented with a chief complaint of a mild cough for 3 days, with increased coughing at night. She reports her throat feeling phlegmy but has no recorded fever or known allergies. Emily's development is on track, meeting all developmental milestones, exhibiting good interaction and play with peers, and growing well in height and weight. Her pregnancy history includes a full-term birth with no complications during pregnancy or delivery, and her health was satisfactory at birth. Her nutritional history reflects a balanced diet with fruits, vegetables, and proteins, with no nutritional deficiencies noted.

Upon examination, Emily's throat showed phlegm with no redness or swelling, the nasal passages were clear, and the lungs were clear on auscultation. Her heart sounds were normal, there was no abdominal tenderness, and no lymphadenopathy was present in the neck. All vital signs were normal.

The review of systems revealed no fever, difficulty breathing, or skin rashes. She reported an occasional runny nose. Emily is not currently on any medications and has no known allergies.

The assessment suggests a likely diagnosis of a viral upper respiratory infection. The plan includes prescribing a nasal spray to relieve congestion, advising increased fluid intake, recommending over-the-counter cough syrup if needed, and suggesting the use of a humidifier at night to ease coughing. A follow-up visit is advised in one week or sooner if the symptoms worsen.

If you have any further questions or require additional information, please do not hesitate to contact me at drjanesmith@pediatricsclinic.com.

Sincerely,

Dr. Jane Smith
Pediatrics
drjanesmith@pediatricsclinic.com
""",
            },
            {
                "role": "user",
                "content": f"""\
Follow these test points when verify the consult letter:
- The letter shall have doctor's name "Jane Smith"
- The letter shall mention patient name as Emily and she is 3 years old, and the encounter happened at 2023/10/03
- The letter shall mention the patients health was satisfactory at birth
""",
            },
            {
                "role": "user",
                "content": "Write me PASS **ONLY** if the consult letter is correct, and FAIL with reason if not",
            },
        ]
    )

    assert result.upper() == "PASS"


def test_consistent_consult_letter():
    consult_letter_1 = create_consult_letter(
        user_info={"name": "Dr. John Doe", "email": "drjohndoe@clinic.com"},
        specialty="Obstetrics & Gynecology (ObGyn)",
        note_date="2022/01/01",
        note_content={
            "Patient Name": "Jane",
            "Patient Age": None,
            "Gender": "female",
            "Chief Complaint": "OB consultation for pregnancy management with planned repeat cesarean section.",
            "History of Present Illness": None,
            "Past Medical History": "The patient had COVID-19 in 2021, after which she experienced heart pain, but subsequent evaluations by her family doctor and hospital visits confirmed that everything was okay.",
            "Past Surgical History": "The patient had a cesarean section in 2019 and an abortion due to a fetal health issue.",
            "Family History": None,
            "Social History": "Jane is employed part-time as a banker, working two to three days per week. She and her spouse reside in a non-specified location without nearby family support. However, they have a local friend network. Postpartum, Jane's mother will assist, and they intend to employ a babysitter for two months.",
            "Obstetric History": "The patient is currently pregnant with her third child. She has had one previous live birth via cesarean section and one abortion due to fetal health issues. Her first child was born slightly premature at approximately 37 weeks, weighing 2.5 kilograms.",
            "The Review of Systems": "The patient reports no asthma, heart problems, seizures, or migraines. She has experienced chest pain post-COVID-19 but has been evaluated and found to be in good health. She is currently active, engaging in pregnancy yoga once a week and walking when she feels able.",
            "Current Medications": None,
            "Allergies": "The patient is allergic to minocycline.",
            "Vital Signs": None,
            "Physical Examination": None,
            "Investigations": None,
            "Problem": "1. Previous cesarean section (654.21)",
            "Differential Diagnosis": None,
            "Plan": "• Scheduled repeat cesarean section at 39 weeks gestation\n• Instructed patient to present to City Medical Center for emergency cesarean section if labor begins prior to scheduled date\n• Advised patient to walk daily for 20 to 30 minutes to improve blood pressure and baby's health\n• Arranged follow-up appointment in three weeks, with subsequent visits every two weeks, then weekly as due date nears",
            "Surgery Discussion": "• Purpose of the Surgery: The purpose of the repeat cesarean section is to safely deliver the baby, given the patient's previous cesarean delivery and her choice for a planned cesarean this time.\n• Risks and Complications: The risks of cesarean section include bleeding, infection, or injury to the bladder or bowel. These risks are small but not zero.\n• Anesthesia: Spinal anesthesia will be used during the procedure, which will prevent pain but allow the patient to be awake.\n• Alternatives: N/A",
        }
    )
    consult_letter_2 = create_consult_letter(
        user_info={"name": "Dr. John Doe", "email": "drjohndoe@clinic.com"},
        specialty="Obstetrics & Gynecology (ObGyn)",
        note_date="2022/01/01",
        note_content={
            "Patient Name": "Jane",
            "Patient Age": None,
            "Gender": "female",
            "Chief Complaint": "OB consultation for pregnancy management with planned repeat cesarean section.",
            "History of Present Illness": None,
            "Past Medical History": "The patient had COVID-19 in 2021, after which she experienced heart pain, but subsequent evaluations by her family doctor and hospital visits confirmed that everything was okay.",
            "Past Surgical History": "The patient had a cesarean section in 2019 and an abortion due to a fetal health issue.",
            "Family History": None,
            "Social History": "Jane is employed part-time as a banker, working two to three days per week. She and her spouse reside in a non-specified location without nearby family support. However, they have a local friend network. Postpartum, Jane's mother will assist, and they intend to employ a babysitter for two months.",
            "Obstetric History": "The patient is currently pregnant with her third child. She has had one previous live birth via cesarean section and one abortion due to fetal health issues. Her first child was born slightly premature at approximately 37 weeks, weighing 2.5 kilograms.",
            "The Review of Systems": "The patient reports no asthma, heart problems, seizures, or migraines. She has experienced chest pain post-COVID-19 but has been evaluated and found to be in good health. She is currently active, engaging in pregnancy yoga once a week and walking when she feels able.",
            "Current Medications": None,
            "Allergies": "The patient is allergic to minocycline.",
            "Vital Signs": None,
            "Physical Examination": None,
            "Investigations": None,
            "Problem": "1. Previous cesarean section (654.21)",
            "Differential Diagnosis": None,
            "Plan": "• Scheduled repeat cesarean section at 39 weeks gestation\n• Instructed patient to present to City Medical Center for emergency cesarean section if labor begins prior to scheduled date\n• Advised patient to walk daily for 20 to 30 minutes to improve blood pressure and baby's health\n• Arranged follow-up appointment in three weeks, with subsequent visits every two weeks, then weekly as due date nears",
            "Surgery Discussion": "• Purpose of the Surgery: The purpose of the repeat cesarean section is to safely deliver the baby, given the patient's previous cesarean delivery and her choice for a planned cesarean this time.\n• Risks and Complications: The risks of cesarean section include bleeding, infection, or injury to the bladder or bowel. These risks are small but not zero.\n• Anesthesia: Spinal anesthesia will be used during the procedure, which will prevent pain but allow the patient to be awake.\n• Alternatives: N/A",
        }
    )

    result = chat_content(
        messages = [
              {
                "role": "system",
                "content": f"You will be given two consult letters generated from the same input, \
                    your job is to verify whether the two consult letters are consistent, error-free, and have stable format between them.",
            },
            {
                "role": "user",
                "content": f"""\
The first consult letter is as following, delimited by ```:
```
{consult_letter_1}
```
""",
            },
            {
                "role": "user",
                "content": f"""\
The second consult letter is as following, delimited by ```:
```
{consult_letter_2}
```
""",
            },
            {
                "role": "user",
                "content": "Write me PASS **ONLY** if both consult letters are similar, and FAIL with reason if not",
            },
        ]
    )
    assert result.upper() == "PASS"
