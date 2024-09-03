from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/scholarships')
def scholarships():
    return render_template('scholarships.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        scholarship = request.form.get('scholarship')
        # Handle form data or save it to a database
    return render_template('apply.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Handle form data or save it to a database
    return render_template('contact.html')

# The '__name__ == "__main__"' block is not needed for WSGI deployment
