from flask import Flask, render_template

# Initialise a new flask instance
app = Flask(__name__)
@app.route('/')

def index():
    return render_template('first_app.html')

if __name__ == '__main__':
    app.run()