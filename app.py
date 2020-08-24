from flask import Flask, url_for, render_template, request
from flaskext.markdown import Markdown

#NLP Part
import spacy
from spacy import displacy
nlp = spacy.load('en')
import json

app = Flask(__name__)
Markdown(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    if request.method == 'POST':
        raw = request.form['rawtext']
        doc = nlp(raw)
        html = displacy(doc, style='ent')
        html = html.replace('\n\n', '\n')
        res = HTML_WRAPPER.format(html)
    
    return render_template('result.html', rawtext=raw, result=res)

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/preview', methods=['POST'])
def preview():
    if request.method == 'POST':
        new = request.form['newtext']
        res = new

    return render_template('preview.html', newtext=new, result=res)

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)