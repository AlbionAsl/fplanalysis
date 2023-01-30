from flask import Flask, render_template, request
import random
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    start_time = time.time()
    questions = []
    for i in range(50):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        operator = random.choice(["+", "-"])
        question = f"{num1} {operator} {num2} = ?"
        questions.append(question)

    return render_template("questions.html", questions=questions, start_time=start_time)

@app.route("/submit", methods=["POST"])
def submit():
    answers = request.form.getlist("answer")
    start_time = float(request.form["start_time"])
    end_time = time.time()
    total_time = end_time - start_time

    score = 0
    for i, answer in enumerate(answers):
        num1, operator, num2 = map(int, answer.split())
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        score += (result == int(answers[i]))

    return render_template("result.html", score=score, total_time=total_time)

if __name__ == "__main__":
    app.run()

