### To complete the task, follow these steps:

1. Install Python libraries via `pip install -r requirements.txt`
2. Create a new package including the following files:
    * A new module file: Write your prompt function using the `chat_content` function in `openai_chat.py`
    * A unit test file with the prefix `test_`
3. Run tests with `python -m pytest .`

### Notes
Some issues encountered while working on this project and how they were dealt with:

How to include everything from the SOAP note with different specialties
- format dict into a string

How to keep the Consult Letter consistent across same and varying inputs
- included hard set structured sections
- lower temperature
- I think the model's criteria of what is considered "consistent" is more like "identical". So while I could add more hard set rules, I think the tradeoff of run time outweighs the need for identical output

**Information from SOAP note are not included in a few tests**
- lower temperature even more
- add instruction to make sure all information is included (not effective)
- add instruction to make sure all information is not reworded (effective)

Long runtimes
- Remove redudant prompts
- imporove verbage