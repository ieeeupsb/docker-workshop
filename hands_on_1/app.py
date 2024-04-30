from flask import Flask, request, redirect, url_for, render_template_string
import os

app = Flask(__name__)

DATA_FILE = '/app/data/submissions.txt'

os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            with open(DATA_FILE, 'a') as file:
                file.write(user_input + '\n')
        return redirect(url_for('index'))

    submissions = []
    try:
        with open(DATA_FILE, 'r') as file:
            submissions = [line.strip() for line in file]
    except FileNotFoundError:
        pass

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Submission Box</title>
        </head>
        <body>
            <form method="post">
                <input type="text" name="user_input" placeholder="Write something..." required>
                <button type="submit">Submit</button>
            </form>
            <h2>Submissions:</h2>
            <ul>
                {% for submission in submissions %}
                <li>{{ submission }}</li>
                {% endfor %}
            </ul>
        </body>
        </html>
    ''', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
