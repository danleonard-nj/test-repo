from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return 'hello world'

@app.route('/other-route')
def other_route():
    return 'this is a new route'

if __name__ == '__main__':
    app.run(debug=True)

