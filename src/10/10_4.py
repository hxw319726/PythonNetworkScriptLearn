# 借助jieba分词和tagul在线制作词云工具，制作词云
import jieba.analyse
path='F:\work\python\PythonNetworkScriptLearn\data\doupo.txt'
fp=open(path,'r')
content=fp.read()
try:
    jieba.analyse.set_stop_words('中文停用词表.txt')
    tags=jieba.analyse.extract_tags(content,topK=100,withWeight=True)
    for tag in tags:
        print(tag[0]+'\t'+str(int(tag[1]*1000)))
finally:
    fp.close()