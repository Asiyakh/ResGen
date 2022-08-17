from urllib import request
from flask import Flask
from flask import request
from buildMM import sol


app = Flask(__name__)

# @app.route("/members")
# def members():
#     return ["hello"]

@app.route('/mm', methods=['POST'])
def search():
    request_data = request.get_json()
    print(request_data)
    request_data['content'] = sol("new content")
    return request_data

if __name__ == "__main__":
    app.run(debug=True)