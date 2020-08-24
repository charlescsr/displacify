from flask import Flask, url_for, render_template, request
from flaskext.markdown import Markdown

#NLP Part
import en_core_web_sm
from spacy import displacy
nlp = en_core_web_sm.load()
import json

app = Flask(__name__)
Markdown(app)

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['POST'])
def inp():
    return render_template('input.html')

@app.route('/extract', methods=['POST'])
def extract():
    if request.method == 'POST':
        raw = request.form['rawtext']
        doc = nlp(raw)
        html = displacy.render(doc, style='ent')
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