import pandas as pd

def app_dic_pre_process():
    app_dic = pd.read_csv('./app_dic.txt', sep=" ")
    table = pd.DataFrame(app_dic)
    table['len'] = table['name'].apply(lambda x : len(x))
    table.to_csv('./app_dic_after_process.txt', index=None)

def app_dic_pos():
    app_dic = pd.read_csv('./app_dic.txt', sep=" ")
    table = pd.DataFrame(app_dic)
    table.pop('type')
    table.to_csv('./app_dic_pos.txt', index=None, sep=' ')

def yw_word_pre_process():
    yw_word = pd.read_csv('./yw_word.txt', sep=" ")
    table = pd.DataFrame(yw_word)
    table['len'] = table['name'].apply(lambda x : len(x))
    table.to_csv('./yw_word_after_process.txt', index=None)



app_dic_pre_process()
app_dic_pos()
yw_word_pre_process()
