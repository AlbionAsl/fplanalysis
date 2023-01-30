from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    operator = random.choice(["+", "-"])
    return render_template("game.html", a=a, b=b, operator=operator)

@app.route("/check", methods=["POST"])
def check_answer():
    a = int(request.form["a"])
    b = int(request.form["b"])
    operator = request.form["operator"]
    answer = int(request.form["answer"])
    if operator == "+":
        result = a + b
    else:
        result = a - b
    if result == answer:
        message = "Correct!"
    else:
        message = "Incorrect. The correct answer is {}".format(result)
    return render_template("result.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)

