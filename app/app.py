from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Devops and CICD Jenkins App THIS IS FIRST COMMIT AND BUILD IT AUTOMATICALLY THROUGH WEBHOOK API AND NOW SECOND COMMIT'

if __name__ == '__main__':SE
    app.run(debug=True, host='0.0.0.0')
