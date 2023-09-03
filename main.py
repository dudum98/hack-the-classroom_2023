from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = ''

def grade_essay(essay_text):
    prompt = f"Please analyze and grade the following essay: {essay_text}\n\nCriteria:\n1. Content and Understanding (40%): Assess the depth of understanding, accuracy of information, and quality of arguments and supporting evidence.\n2. Organization and Structure (20%): Evaluate the overall organization, clarity of the thesis statement, logical flow of ideas, and paragraph transitions.\n3. Coherence and Clarity (20%): Examine sentence structure, clarity of expression, and use of vocabulary.\n4. Grammar and Mechanics (10%): Check for grammatical errors, spelling, punctuation, and adherence to writing conventions.\n5. Citations and References (10%): Assess the use of citations and references, if applicable.\n\nPlease provide a percentage grade and brief feedback on strengths and weaknesses in these areas. Your evaluation should be concise and constructive."

    try:
        response = openai.Completion.create(
            engine="davinci",  # Use the Davinci engine
            prompt=prompt,
            max_tokens=1000  # Adjust this value as needed
        )

        graded_essay = response.choices[0].text
        return graded_essay
    except Exception as error:
        return f"An error occurred: {str(error)}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grade', methods=['POST'])

def grade_essay_request():
    essay_text = request.form['essay_text']

    # Call the grade_essay function to grade the essay
    grading_result = grade_essay(essay_text)

    # Render 'index.html' and pass the grading result
    return render_template('result.html', result=grading_result)

if __name__ == '__main__':
    app.run(debug=True)
