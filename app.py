from flask import Flask, request, render_template_string

app = Flask(__name__)

# Minimal HTML template embedded directly in the code
TEMPLATE = """
<!doctype html>
<html>
<head><title>Table Generator</title></head>
<body>
    <h2>Multiplication Table Generator</h2>
    
    <form method="POST">
        <label>Enter a number:</label>
        <input type="number" name="number" required>
        <button type="submit">Submit</button>
    </form>

    {% if table %}
        <hr>
        <h3>Table for {{ num }}:</h3>
        <ul>
            {% for row in table %}
                <li>{{ row }}</li>
            {% endfor %}
        </ul>
        <a href="/">Reset</a>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    table_data = []
    num = None
    
    if request.method == 'POST':
        try:
            # Get number from form input
            num = int(request.form.get('number'))
            # Generate the table list
            table_data = [f"{num} x {i} = {num * i}" for i in range(1, 11)]
        except ValueError:
            table_data = ["Please enter a valid integer."]

    return render_template_string(TEMPLATE, table=table_data, num=num)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)