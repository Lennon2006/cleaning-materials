from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Cleaning Materials app!'

if __name__ == '__main__':
    app.run(debug=True)