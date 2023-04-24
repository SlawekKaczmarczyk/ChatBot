import json
from difflib import get_close_matches

# Load the knowledge from a JSON file

def load_knowledge_base(file_path: str):
    """
    :param file_path: The path to json file with knowledge
    :return A dictionary with the knowledge base data.
    """
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data



def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

    """
    Retrieve the answer for a given question from the knowledge base.
    :param question: The matched question from the knowledge base.
    :param knowledge_base: A dictionary containing the knowledge base data.
    :return: The answer to the question or None if the question is not found.
    """

def chatbot():

    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == 'quit':
            break

        answer: str = get_answer_for_question(user_input, knowledge_base)
        print(f"Bot: {answer}")



if __name__ == "__main__":
    chatbot()