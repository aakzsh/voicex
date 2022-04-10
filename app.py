from flask import Flask, render_template, request



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

if __name__ == '__main__':
    app.run(debug=True)

