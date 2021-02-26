from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Say hello to Flask !--! images are fetched from ECR !-kar dia change-! nginx is working as a reverse proxy for our app'

app.run(host='0.0.0.0', port=5000)

