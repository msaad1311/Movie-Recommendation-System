from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import scipy.sparse as sp


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__, template_folder='templates')
data = pd.read_csv('Preprocessed File.bz',compression='bz2')
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

def transformer(data):
    count = CountVectorizer(stop_words='english')
    cvt_matrix = count.fit_transform(data['Combined'])
    
    tfidf = TfidfVectorizer(stop_words='english')
    tf_matrix=tfidf.fit_transform(data['overview'])
    
    combo = sp.hstack([cvt_matrix,tf_matrix],format='csr')
    
    similarity = cosine_similarity(combo,combo)
    return similarity

def recommendations(title,data,model):
    indices = pd.Series(data.index, index = data['original_title'])
    idx = indices[title]
    sim = list(enumerate(model[idx]))
    sim = sorted(sim, key=lambda x: x[1], reverse=True)
    sim = sim[1:6]
    movie_indices = [i[0] for i in sim]
    titles = data['original_title'].iloc[movie_indices]
    directors = data['Director'].iloc[movie_indices]
    recommendation_table = pd.DataFrame(columns=['Title','Director'])
    recommendation_table['Title']=titles
    recommendation_table['Director']=directors
    return recommendation_table

def results(title):
    if title not in data['original_title'].unique():
        return "The movie is not in the database. Kindly try another view"
    sim_model = transformer(data)
    return recommendations(title,data,sim_model)



@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def main():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        movie_name = movie_name.title()
        if movie_name not in data['original_title'].unique():
            return render_template('negative.html')
        else:
            res = results(movie_name)
            return render_template('positive.html', movie_names=res['Title'].tolist(), 
            director=res['Director'].tolist(), search_name=movie_name)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0',port=8080)