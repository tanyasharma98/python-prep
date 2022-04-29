from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return render_template('/index.html')


@app.route('/about')
def tanya():
    name = request.args.get("name", "Tanya")
    return render_template('/about.html', name2=name)


@app.route('/bootstrap')
def boot():
    name = request.args.get("name", "Tanya")
    return render_template('/bootstrap.html')


app.run(debug=True)
