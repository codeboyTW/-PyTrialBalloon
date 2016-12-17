#encoding=utf-8

import json
import jieba
import jieba.analyse
from pprint import pprint
import codecs
import re
import sys

jieba.set_dictionary('../dict.txt.big')
jieba.load_userdict("../userdict.txt")
jieba.analyse.set_stop_words("../stop_words.txt")

with open(sys.argv[1]) as data_file:    
    data = json.load(data_file)

#print(data['articles'][0]['content'])
#print(len(data['articles']))
result = []

target = unicode('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+\:︰', "utf-8")

sStr = unicode('朱立倫', "utf-8")
#sStr = unicode('陳水扁', "utf-8")
print sStr

for articles in data['articles'] :
    if('content' in articles and articles['content'].find(sStr)!=-1 and articles['article_id'].find("M.1479132252.A.E25")==-1 ):
        #print articles['content']
        print "==============================="
        ofilename = sys.argv[2] + "/"  + articles['article_id'] +  ".txt"
        f = codecs.open(ofilename, "w", "utf-8")

        results=re.compile(r'http://[a-zA-Z0-9.?/&=:]*',re.S)
        string=results.sub("",articles['content'])
        
        string = re.sub(target, " ".decode("utf8"),string)  
        
        print articles['article_id']
        #print string
        
        seg_list = jieba.cut(string,cut_all=False)
        print "\t".join(seg_list)

        tags = jieba.analyse.extract_tags(string, 20)
        print "\n".join(tags)
        
       # print string  
        f.write( "\n".join(tags))
        for tag in tags :
             result.append(tag)
        f.close()

print "\n".join(result)

cfilename = "./result/" +sys.argv[2] + "-cloud.txt"
f2 = codecs.open(cfilename, "w", "utf-8")
f2.write( "\n".join(result))
f2.close()
 
#sStr= 'strchr'   
#sStr = 's'   
#nPos = sStr1.index(sStr)   
#print nPos  

#pprint(data)