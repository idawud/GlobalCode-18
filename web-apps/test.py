from flask import Flask,render_template,url_for
app = Flask(__name__)

@app.route('/<name>/')
def index(name):
    return render_template('main.html', to=name)

if __name__ == "__main__":
    app.run(debug = True)
