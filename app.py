from asyncio.windows_events import NULL
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///campaigns.db"
db = SQLAlchemy(app)

class Campaigns(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(2000), nullable = False)
    imgurl = db.Column(db.String(200), nullable = False)
    upvotes = db.Column(db.Integer, nullable = False)
    donation = db.Column(db.Integer, nullable = False)
    target =  db.Column(db.Integer, nullable = False)
    def __repr__(self) -> str:
        return f'{self.sno}-{self.title}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    allCam = Campaigns.query.all()
    print(allCam)

    return render_template('home.html', allCam = allCam)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        print("post hai")
        title = request.form['title']


        desc = request.form['desc']
        imgurl = request.form['imgurl']
        target = request.form['donation']

        data = {
"api_key": "vFqoj20y8mAKZgSzgBkudoT4j3QIHRabAfXxsZIr",
    "features": [
        {
        "v2": title
        }
    ],
    "include_features": False,
    "model": "custom_prediction_classification_1649590243695",
    "version": "1"
        }
        r = requests.post(url = "https://api.mage.ai/v1/predict", data = data)

        print(r.text)
        if target==NULL:
            target=0
        added = Campaigns(title=title, desc=desc, imgurl = imgurl, donation = 0, target = target, upvotes = 0)
        db.session.add(added)
        db.session.commit()
    return redirect('/show')

@app.route('/show')
def show():
    allCam = Campaigns.query.all()
    print(allCam)

    return render_template('home.html', allCam = allCam)

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

