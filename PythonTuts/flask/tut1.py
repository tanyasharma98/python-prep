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





# @app.route('/')
# def tanya():
#     name = request.args.get("name", "World!!")
#     return f'Hello, {escape(name)}!'
# @app.route('/tanya')
# def tanya():
#     name = request.args.get("name", "tanya mam, this is me , get lost")
#     return f'Hello, {escape(name)}!'

# app.run()
# app.run(debug=True)
