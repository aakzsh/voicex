from flask import Flask, render_template, request



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/stories')
def stories():
    return render_template('stories.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/new')
def new():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)

