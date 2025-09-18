from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Projects route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Skills route
@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)