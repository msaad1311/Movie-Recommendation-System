import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import scipy.sparse as sp
import pickle


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def reader():
    movie = pd.read_csv('Preprocessed File.bz',compression='bz2')
    return movie

def transformer(data,save=False,present=False):
    if present:
        count=pickle.load(open('Count_transform.pkl','rb'))
        tfidf=pickle.load(open('Tfidf_transform.pkl','rb'))
    else:
        count = CountVectorizer(stop_words='english')
        tfidf = TfidfVectorizer(stop_words='english')

    cvt_matrix = count.fit_transform(data['Combined']) 
    tf_matrix=tfidf.fit_transform(data['overview'])
    
    combo = sp.hstack([cvt_matrix,tf_matrix],format='csr')
    
    similarity = cosine_similarity(combo,combo)
    if save:
        return count,tfidf
    else:
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
    data = reader()
    if title not in data['original_title'].unique():
        return 'negative'
    else:
        sim_model = transformer(data,False,True)
        return recommendations(title,data,sim_model)
    # print(list(recommendations(title,data,sim_model)))
    
def saver():
    data = reader()
    cvt,tfidf = transformer(data,True)
    pickle.dump(cvt,open('Count_transform.pkl','wb'))
    pickle.dump(tfidf,open('Tfidf_transform.pkl','wb'))
    return    

