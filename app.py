from flask import Flask,request,jsonify,render_template
from flask_cors import CORS,cross_origin
import Recommendation
import pandas as pd

app = Flask(__name__,template_folder='templates')
data = pd.read_excel('Preprocessed File.xls')
data=data.loc[:, ~data.columns.str.contains('^Unnamed')]
# print(data['original_title']=='Avatar')

@app.route("/",methods=['GET','POST'])
@cross_origin()
def main():
    if request.method=='GET':
        return render_template('index.html')
    if request.method=='POST':
        movie_name = request.form['movie_name']
        movie_name=movie_name.title()
        print(movie_name)
        if movie_name not in data['original_title'].unique():
            return render_template('negative.html')
        else:
            res=Recommendation.results(movie_name)
            return render_template('positive.html',movie_names=res['Title'].tolist(),
            director=res['Director'].tolist(),search_name=movie_name)
            # return 'welcome'
        # return render_template('positive.html')

# @app.route('/recommend',methods=['GET'])
# def recmd():
#     movie = request.form['title']
#     res=Recommendation.results(movie)
#     return res


if __name__ == "__main__":
    app.run(debug=True)