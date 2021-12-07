import json
import re
import pandas as pd
import os
cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]\s")
dic = {}
with open("data/robot/gilani/gilani-2017_tweets.json",'r') as load_f:
    load_dict = json.load(load_f)
    for json1 in load_dict:
        id = json1["user"]["id"]
        description = json1["user"]["description"]
        description = cop.sub('', description)
        description =description.replace("\n","")
        if len(description) != 0:
            xx = {id:description}
            dic.update(xx)

data = dict(sorted(dic.items(), key=lambda x: x[0]))


datatsv = pd.read_csv('data/robot/gilani/gilani-2017.tsv',encoding='gbk',sep='\t',header=0)
datatsv.columns = ["id","humorbot"]
datatsv.set_index('id', inplace=True)
#print(data.loc[390617262, "humorbot"])

filename = 'data/gilani.txt'
fileclean = 'data/corpus/gilani.clean.txt'
i = 1
with open(filename, 'w') as file_to_write:
    for key, value in data.items():
        if i % 4 != 0:
            try:
                file_to_write.write(str(key) + '\t' +"train" + '\t' + str(datatsv.loc[key, "humorbot"])+"\n")
            except:
                print("继续")
        else:
            try:
                file_to_write.write(str(key) + '\t' + "test" + '\t' + str(datatsv.loc[key, "humorbot"]) + "\n")
            except:
                print("不用管，继续")
        i = i+1

with open(fileclean, 'w') as file_to_write:
    for key, value in data.items():
        file_to_write.write(str(value).replace(".","").replace("'","")+"\n")

print("#####写入完毕####")
