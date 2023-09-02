from flask import Flask, render_template, request
import openai

openai.api_key = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grade', methods=['POST'])
def grade_essay():
    essay_text = request.form['essay_text']

    # Call GPT-3 to grade the essay
    gpt_response = openai.Completion.create(
        engine="davinci",  # Use the Davinci engine
        prompt=essay_text,
        max_tokens=100000  # Adjust this value as needed
    )

    # Extract the grading result from the GPT-3 response
    grading_result = gpt_response.choices[0].text

    return render_template('result.html', result=grading_result)

if __name__ == '__main__':
    app.run(debug=True)

