# ResGen

Generate bullet points for software related resumes.

## Starting environments

Run alongside one another in different terminal tabs.

### Running Flask backend.

cd flask-server
python3 -m venv venv
source venv/bin/activate
pip3 install flask numpy nltk transformers torch gensim
python3 server.py

if you run in to issues, you may need to update python

### Running React frontend.

cd res-gen
npm init
npm install
npm start
