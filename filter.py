from flask import Flask, request
import json
import pandas as pd
import os
import jieba
import jieba.posseg


app = Flask(__name__)

@app.before_request
def work_before_request():
    global app_dic_df, yw_word_df
    app_dic = pd.read_csv('./app_dic_after_process.txt')
    app_dic_df = pd.DataFrame(app_dic)
    yw_word = pd.read_csv('./yw_word_after_process.txt')
    yw_word_df = pd.DataFrame(yw_word)
    #jieba.load_userdict(app_dic_df['name'])
    jieba.load_userdict('./app_dic_pos.txt')

@app.route('/filter', methods=['POST'])
def filter():
    request_body = request.get_json(force=True)
    content = request_body['content']
    result = data_process(content)
    return result

def data_process(input):
    for item in input:
        if item['type'] == 'app':
            seg_list = jieba.posseg.cut(item['name'])
            #print ('/'.join(seg_list))
            for word, flag in seg_list:
                print word, flag

    return 'hello'
    

if __name__ == '__main__':
    app.run(threaded=True)
