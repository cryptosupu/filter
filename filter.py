# -*- coding: UTF-8 -*-

from flask import Flask, request
import json
import pandas as pd
import os
import jieba
import jieba.posseg
import hashlib


app = Flask(__name__)

@app.before_request
def work_before_request():
    global app_dic_df, yw_word_list
    app_dic = pd.read_csv('./app_dic_after_process.txt')
    app_dic_df = pd.DataFrame(app_dic)
    yw_word = pd.read_csv('./yw_word_after_process.txt')
    yw_word_df = pd.DataFrame(yw_word)
    yw_word_list = list(yw_word_df['name'])
    #jieba.load_userdict(app_dic_df['name'])
    jieba.load_userdict('./app_dic_pos.txt')

@app.route('/filter', methods=['POST'])
def filter():
    request_body = request.get_json(force=True)
    content = request_body['content']
    result = data_process(content)
    return result

def data_process(input):
    result_list = []
    for item in input:
        if item['type'] == 'app':
            seg_generator = jieba.posseg.cut(item['name'])
            print type(item['name'])
            seg_list = list(seg_generator)
            seg_list_len = len(seg_list)
            if seg_list_len == 1:
                for word, flag in seg_list:
                    if (word.encode("utf-8") in yw_word_list) and (flag in ['n','v']):
                        md5 = hashlib.md5(item['name'].encode("utf-8")).hexdigest()
                        result = json.dumps({'name':item['name'],'type':item['type'],'md5':md5,'num':0})
                        result_list.append(result)
            elif seg_list_len > 1:
                count = 0
                have_yw_word = False
                for word, flag in seg_list:
                    count += 1
                    if (len(word) == 1) or (flag not in ['a','ad','n','v']):
                        break
                    if word.encode("utf-8") in yw_word_list:
                        have_yw_word = True
                    if (count == seg_list_len) and (flag in ['n','v']) and have_yw_word:
                        //qu chong hou suan md5
                        md5 = hashlib.md5(item['name'].encode("utf-8")).hexdigest()
                        result = json.dumps({'name':item['name'],'type':item['type'],'md5':md5,'num':0})
                        result_list.append(result)
                        have_yw_word = False
                        


                    
                    
    print json.dumps({'data':result_list})
    return 'hello'
    

if __name__ == '__main__':
    #app.run(processes=4)
    app.run(threaded=True)
