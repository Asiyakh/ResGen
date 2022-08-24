from urllib import request
from flask import Flask
from flask import request
from buildMM import sol
from buildHMM import solHMM
from buildHuggingFace import solHF


app = Flask(__name__)

# @app.route("/members")
# def members():
#     return ["hello"]

@app.route('/mm', methods=['POST'])
def search():
    request_data = request.get_json()
    request_data['content'] = sol(request_data['content'])
    return request_data

@app.route('/hmm', methods=['POST'])
def hmm():
    request_data = request.get_json()
    request_data['content'] = solHMM(request_data['content'])
    return request_data

@app.route('/hf', methods=['POST'])
def hf():
    print("hf")
    request_data = request.get_json()
    request_data['content'] = solHF(request_data['content'])
    print(request_data)
    return request_data

if __name__ == "__main__":
    app.run(debug=True)