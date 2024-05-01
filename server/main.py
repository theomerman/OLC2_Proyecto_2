from flask import Flask, request, jsonify
from routes.routes import routes
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
app.register_blueprint(routes)

# allow access to the server from the client
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    app.run(debug=True)
