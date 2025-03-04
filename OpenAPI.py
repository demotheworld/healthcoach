from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
def get_chatgpt_response(prompt):
    """Sends a prompt to the ChatGPT API and returns the response."""
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",  # Or another available model like "gpt-4"
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Collect user details interactively
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    height = input("Enter Height (e.g., 5 ft 11 inches): ")
    weight = input("Enter Weight (e.g., 170 lb): ")
    gender = input("Enter Gender: ")
    dietary_restrictions = input("Enter any Dietary Restrictions (e.g., No Dairy): ")

    # Compose the query dynamically
    user_input = (f"Name: {name} \n"
                  f"Age: {age} Height: {height} \n"
                  f"Weight: {weight} \n"
                  f"Gender: {gender} \n"
                  f"[USER_REQUEST]: Dietary Restriction: {dietary_restrictions} \n\n"
                  "What are the recommendations for a healthy diet? \n"
                  "What are the exercise recommendations? \n"
                  "What are some healthy habits to adopt? \n"
                  "What is the healthy BMI range?")
    response = get_chatgpt_response(user_input)
    print("ChatGPT's response:", response)
