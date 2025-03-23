from pydoc import html

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



@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route("/submit_data",methods=['POST'])
def submit_data():
    name_input = request.form.get('name')
    weight_input = request.form.get('weight')
    age_input = request.form.get('age')
    height_input = request.form.get('height')
    gender_input = request.form.get('gender')
    diet_input = request.form.get('diet')
    foodpreference_input = request.form.get('foodpreference')

    # Compose the query dynamically
    user_input = (f"Name: {name_input} \n"
                  f"Age: {age_input} Height: {height_input} \n"
                  f"Weight: {weight_input} \n"
                  f"Gender: {gender_input} \n"
                  f"[USER_REQUEST]: Dietary Restriction: {diet_input} \n\n"
                  f"[USER_REQUEST]: Food Preferences for Recommended Diet: {foodpreference_input} \n\n"
                  "What are the recommendations for a healthy diet? \n"
                  "What are the exercise recommendations? \n"
                  "What are some healthy habits to adopt? \n"
                  "How much sleep should I be getting daily? \n"
                  "How much water should I intake daily? \n"
                  "What is the healthy BMI range?\n"
                  "give output in HTML format along with bullet points")
    response =  get_chatgpt_response(user_input)
    response = response.replace("```html", "")
    response = response.replace("```", "")
    response = response.replace("This HTML document%", "")
    return render_template('result.html', response_output=response)

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
