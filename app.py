from flask import Flask,request,jsonify
from flask_cors import CORS
import Recommendation

app = Flask(__name__)

@app.route("/")
def home():
    return 'Welcome Home!'
@app.route('/recommend',methods=['GET'])
def recmd():
    movie = request.form['title']
    res=Recommendation.results(movie)
    return res

if __name__ == "__main__":
    app.run(debug=True)