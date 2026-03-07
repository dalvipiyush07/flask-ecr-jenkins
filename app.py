from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Project 4! Docker + Jenkins + ECR + Lambda + final done by P.D.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
