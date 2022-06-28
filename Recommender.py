import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from Article import getArticles
import pickle
import os



class RecommendationEngine:
    data = None
    model = None
    embeddings = None
    sim_data = None

    def __init__(self):
        if(os.path.exists('./model.pkl')):
            modelPickle = open('./model.pkl', 'rb')
            self.model =  pickle.load(modelPickle)

    def __saveModel(self, obj, filename):
      with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


    def getModel(self):
        if(not os.path.exists('./model.pkl')):
            self.model = SentenceTransformer('distilbert-base-nli-mean-tokens')
            self.__saveModel(self.model, 'model.pkl')

    def __getData(self):
        self.data = getArticles()
        self.data = pd.DataFrame(self.data)

    def __simData(self): 
         if(os.path.exists('./sim_data.pkl')):
            modelPickle = open('./sim_data.pkl', 'rb')
            self.sim_data =  pickle.load(modelPickle)


    def train(self, data):
        self.getModel()
        self.data = pd.DataFrame(eval(data))

        self.data = self.data.dropna()

        X = np.array(self.data.Description)

        self.embeddings = self.model.encode(X)
        self.sim_data = pd.DataFrame(cosine_similarity(self.embeddings))
        self.__saveModel(self.sim_data, 'sim_data.pkl')

    def recommenend_article(self, title: str):
        if (self.model == None):
            return []

        self.__getData()
        self.__simData()

        print(self.sim_data)

        # print(self.data[0])
        # mapping = pd.Series(self.data.index , index = self.data['title'])

        # print(mapping)

        # index = mapping[title]
        index_recommendation = self.sim_data[3].sort_values(ascending=False).index.tolist()[1:6]
        recommended_articles = self.data['title'].iloc[index_recommendation].values


        return recommended_articles


