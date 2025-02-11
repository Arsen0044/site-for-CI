from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    value = None
    if request.method == "POST":
        value = request.form["input_value"]
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Simple Input Page</title>
        </head>
        <body>
            <h1>Input and Display Value</h1>
            <form method="POST">
                <input type="text" name="input_value" placeholder="Enter something" required>
                <button type="submit">Confirm</button>
            </form>

            {% if value %}
                <h2>You entered: {{ value }}</h2>
            {% endif %}
        </body>
        </html>
    """, value=value)


if __name__ == "__main__":
    app.run(debug=True)
