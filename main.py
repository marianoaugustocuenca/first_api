from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def about(word):
    word_definition = word.title()
    return {'word': word, 'definition': word_definition}


if __name__ == '__main__' :
    app.run(debug=True)
