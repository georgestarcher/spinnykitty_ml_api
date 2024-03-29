"""Simple ML Model Serving API"""
import pickle
from flask import Flask, request, jsonify
import numpy as np


# Load Model
model = pickle.load(open('./model/spinnyKitty.pkl','rb'))
# Setup API
api = Flask(__name__)

@api.route('/spinny', methods=['POST'])
def post_spinny():
    """ API response function"""
    frame_time = request.json['time']
    distinct_user_count = request.json['distinctUserCount']
    mean_token_count = request.json['meanTokenCount']
    mean_spinny_count = request.json['meanSpinnyCount']
    array = [frame_time, distinct_user_count, mean_token_count, mean_spinny_count]
    prediction = model.predict([array])
    result_ml = dict()
    result_ml["prediction"] = np.reshape(prediction, -1).tolist()[0]
    return jsonify(result_ml), 201

if __name__ == '__main__':
    api.run(host='0.0.0.0')

