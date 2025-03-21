from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template

load_dotenv()

# Replace with your actual API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/submit_data",methods=['POST'])
def submit_data():
    name_input = request.form.get('name')
    #name_input = request.form['name']
    weight_input = request.form.get('weight')
    #print("Name: ",name_input)
    #print("Weight: ",weight_input)
    return render_template('result.html', name=name_input, weight=weight_input)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

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
    app.run(debug=True)
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

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
