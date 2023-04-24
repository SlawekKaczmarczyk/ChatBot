# ChatBot

A simple chatbot that answers your questions.
If it does not know the answer - it asks you to provide one so it can learn. 

Instruction

    1. Load the knowledge base from a JSON file.
    2. Continuously prompt the user for questions.
    3. Find the closest matching question in the knowledge base.
    4. If a match is found, return the answer. Otherwise, ask the user to teach the chatbot.
    5. If the user provides a new answer, add it to the knowledge base and save the updated knowledge base to the JSON file.
    6. Exit the chatbot when the user types 'quit'.
