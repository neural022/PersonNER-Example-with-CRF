# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:37:38 2019

@author: neural022
"""
import os
import CRFPP

def load_model(path):
    if os.path.isfile(path):
        print("loading...model\n")
        return CRFPP.Tagger('-m %s' % path)
    else:
        print("model不存在\n")

def tag_label(sentence):
    tagger = load_model('model')
    for c in sentence:
        print(c)
        tagger.add(c)
    result = []
    word = ""
    tagger.parse()
    
    print("預測的句子的字數：%s\t特徵列的個數:%s" % (str(tagger.size()), str(tagger.xsize())))
    for i in range(0, tagger.size()-1):  
        for j in range(0, tagger.xsize()-1):
            ch = tagger.x(i, j)            
            tag = tagger.y2(i)
            #print(ch,tag)
            if tag == 'B_P':
                word = ch
            elif tag == 'M_P':
                word += ch
            elif tag == 'E_P':
                word += ch
                result.append(word)
    return result

if __name__ == '__main__':
    sentence = ["我\tr", "想\tv", "聽\tv", "周\tnr", "筆\tnr", "暢\tnr", "的\tuj", "歌\tn"]
    print(tag_label(sentence))