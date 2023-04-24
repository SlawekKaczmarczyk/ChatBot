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



# Save the updated knowledge base to the JSON file
def save_knowledge_base(file_path: str, data: dict):

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

    

# Find the closest matching question
def find_best_match(user_question: str, questions: list[str]) -> str | None:

    """
    Find the closest matching question in the knowledge base.
    :param user_question: The user's input question.
    :param questions: A list of questions from the knowledge base.
    :return: The closest matching question or None if no match is found.
    """
    
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None



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

        # Finds the best match, otherwise returns None
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(user_input, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer: str = input("Type the answer or 'skip' to skip: ")

            if new_answer.lower()!= 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Bot: Thank you! I've learned something new.")

if __name__ == "__main__":
    chatbot()