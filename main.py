from flask import Flask, render_template
from getNews import getData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/topHeadlines/<string:category>')
def topHeadlines(category):
    data = getData(category=category)
    limit = list(range(0,len(data)))
    return render_template('topHeadlines.html', category=category, data=data, limit = limit)


if __name__ == '__main__':
    app.run(debug=True)
 