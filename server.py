#data = {"trip": 10, "history": 20, "immortal": 70, "ID": 2, "time": 50, "letter": 60}

from _data import guide, weight, chat
from flask import Flask, request, jsonify
from flask_cors import CORS
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def post_data():
    data = request.get_json()

    trip = data['trip']
    history = data['history']
    immortal = data['immortal']
    ID = data['ID']
    time = data['time']
    letter = data['letter']
    #读取数据

    if(ID == 0):
        text = guide[0][0]
        _letter = len(text)
        _trip = 1
        _history = 1
        _immortal = 1
        _sort = []
        condifence_scores = []
    else:
        ID = ID - 1
        _trip = trip * time * letter * weight[ID][0]
        _history = history * time * letter * weight[ID][1]
        _immortal = immortal * time * letter * weight[ID][1]
        #计算权重

        _all = _trip + _history + _immortal
        _trip = (_trip / _all) * 100
        _history = (_history / _all) * 100
        _immortal = (_immortal / _all) * 100
        #计算比例

        _sort = ['','','']
        _list = ['trip','history','immortal']
        max_val = max(_trip, _history, _immortal)
        min_val = min(_trip, _history, _immortal)

        if(_trip == max_val):
            _sort[0] = 'trip'
            _ID = 0
        elif(_history == max_val):
            _sort[0] = 'history'
            _ID = 1
        elif(_immortal == max_val):
            _sort[0] = 'immortal'
            _ID = 2

        if(_trip == min_val):
            _sort[2] = 'trip'
        elif(_history == min_val):
            _sort[2] = 'history'
        elif(_immortal == min_val):
            _sort[2] = 'immortal'
    
        set1 = set(_list)
        set2 = set(_sort)
        diff = set1.difference(set2)
        _diff = list(diff)
        _sort[1] = _diff[0]
        
        _dict = {}
        _dict['trip'] = _trip
        _dict['history'] = _history
        _dict['immortal'] = _immortal

        #求出按降序排列的列表
        ID = ID + 1
        if weight[ID][4] == 1 and _ID == weight[ID][3]:
            _text = 0
        elif weight[ID][4] == 0 and _ID != weight[ID][3]:
            _text = 0
        else:
            _text = 1

        text = guide[ID][_text]
        _letter = len(text)
        #选择导游词

        confidence_scores = [_dict[_sort[0]], _dict[_sort[1]], _dict[_sort[2]]]
        # 横坐标标签
        #labels = _sort
        # 创建柱状图
        #plt.rcParams['font.family'] = 'wqy-zenhei'
        #plt.bar(labels, confidence_scores, width=0.4)
        #plt.subplots_adjust(top=0.95)
        # 设置标题和标签
        #for i, v in enumerate(confidence_scores):
        #    plt.text(i, v+1, str(v), ha='center')

        #plt.title('Confidence Scores')
        #plt.xlabel('sight')
        #plt.ylabel('Confidence')
        # 保存图像
        #os.remove('/usr/share/website/assets/confidence_scores.png')
        #plt.savefig('/usr/share/website/assets/confidence_scores.png')

    return jsonify({'text': text, 'trip': _trip, 'history': _history, 'immortal': _immortal, 'letter': _letter, 'title': chat[ID]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

