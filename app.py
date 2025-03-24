from flask import Flask, render_template, request
HEAD

app = Flask(__name__)

# Function to perform calculations


def calculate(numbers, operator):
    try:
        numbers = [float(num) for num in numbers]  # Convert input to float

        if operator == "+":
            return sum(numbers)
        elif operator == "-":
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            return result
        elif operator == "*":
            result = 1
            for num in numbers:
                result *= num
            return result
        elif operator == "/":
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    return "Error: Division by zero is not allowed."
                result /= num
            return result
        elif operator == "**":
            result = numbers[0]
            for num in numbers[1:]:
                result **= num
            return result
        elif operator == "%":
            result = numbers[0]
            for num in numbers[1:]:
                result %= num
            return result
        else:
            return "Invalid operator"

    except ValueError:
        return "Error: Please enter valid numbers."


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        numbers_str = request.form.get("numbers")
        operator = request.form.get("operator")

        if not numbers_str:
            error = "Please enter at least one number."
        else:
            numbers = numbers_str.split(",")
            result = calculate(numbers, operator)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)

# Function to perform calculations


def calculate(numbers, operator):
    try:
        numbers = [float(num) for num in numbers]  # Convert input to float

        if operator == "+":
            return sum(numbers)
        elif operator == "-":
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            return result
        elif operator == "*":
            result = 1
            for num in numbers:
                result *= num
            return result
        elif operator == "/":
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    return "Error: Division by zero is not allowed."
                result /= num
            return result
        elif operator == "**":
            result = numbers[0]
            for num in numbers[1:]:
                result **= num
            return result
        elif operator == "%":
            result = numbers[0]
            for num in numbers[1:]:
                result %= num
            return result
        else:
            return "Invalid operator"

    except ValueError:
        return "Error: Please enter valid numbers."


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        numbers_str = request.form.get("numbers")
        operator = request.form.get("operator")

        if not numbers_str:
            error = "Please enter at least one number."
        else:
            numbers = numbers_str.split(",")
            result = calculate(numbers, operator)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)

