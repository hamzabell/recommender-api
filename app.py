from copyreg import pickle
from Recommender import RecommendationEngine
from flask import Flask, jsonify, request
from shareplum import Site, Office365
from Article import addArticle
from Updates import getUpdates, addUpdateID
from apscheduler.schedulers.background import BackgroundScheduler

import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recommend_article():
    rec = RecommendationEngine()
    data = request.get_json()

    response = rec.recommenend_article(data['title'])

    if isinstance(response, np.ndarray):
        response = response.tolist()


    return jsonify({
        "message": 'Recommendation obtained sucessfully',
        "data": response
    })


def scheduled():
    last_updated = []

    authCookie = Office365('https://hashemng.sharepoint.com', username='havisicare@ha-shem.com', password='$upp0rt@9*$!9!1242a').GetCookies()
    site = Site('https://hashemng.sharepoint.com/sites/HLHumanResourcesAPPS', authcookie=authCookie)


    data = site.List('Articles').GetListItems(fields=['ID', 'Title', 'Description', 'link'])

    last_updated = getUpdates()

    for i in range(len(data)):
        article_ID = data[i]['ID']

        if (not int(article_ID) in last_updated):
            addArticle(data[i]['Title'], data[i]['Description'], data[i]['link'])
            addUpdateID(article_ID)
        
    

    df = pd.DataFrame(data)


    rec = RecommendationEngine()

    rec.train(df.to_json())

sched = BackgroundScheduler(daemon=True)
sched.add_job(scheduled, 'cron', hour='23', minute='59')

sched.start()

