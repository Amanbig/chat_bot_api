from flask_cors import CORS
from flask import Flask, request, jsonify
from public.educations import educations
from public.colleges import colleges

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/education',methods=["GET"])
def education():
    return jsonify({'educations':educations})

@app.route('/college',methods=["GET"])
def college():
    return jsonify({'colleges':colleges})

if __name__ == '__main__':
    app.run(debug=True)