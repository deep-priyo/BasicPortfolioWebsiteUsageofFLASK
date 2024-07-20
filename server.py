from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# all html files should be in templates
# all static files like images ,css should be in static
# hold shift and reload chrome to deleter cache file and get the updates made in style sheet
if __name__ == '__main__':
    app.run(debug=True)
