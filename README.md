# ResGen

Generate bullet points for software related resumes.

## Starting environments

Run alongside one another in different terminal tabs.

### Running Flask backend.

cd flask-server
python3 -m venv venv
source venv/bin/activate
pip3 install Flask
pip3 install numpy
pip3 install nltk
pip3 install transformers
pip3 install torch
pip3 install gensim
python3 server.py

(may require installations of numpy for example)

### Running React frontend.

cd res-gen
npm init
npm install
npm start
