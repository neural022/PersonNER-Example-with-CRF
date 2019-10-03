# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:58:34 2019

@author: neural022
"""

class crfPRF():
    def __init__(self, file):
        self.file = file
        
    def totalCorrect(self, list1, list2):
        cor_count = 0
        if(len(list1) == len(list2)):
            for i in range(0, len(list1)):
                if list1[i] == list2[i]:
                    cor_count += 1
        return cor_count
    
    def getTotalTag(self, tag_list):
        tmp_set = set()
        for tag in tag_list:
            tmp_set.add(tag)
        return tmp_set
    
    def singleCorrect(self, list1, list2, list3, errorlist, tag): # 核心
        cor_count = 0                                             #   記錄正確數
        for i in range(0, len(list1)):
            if list2[i] == tag and list2[i] == list3[i]:
                cor_count += 1
            elif list2[i] == tag:
                error_content = list1[i]+" "+list2[i]+" "+list3[i]
                errorlist.append(error_content)
        return cor_count

    def countSingleTag(self, tag_list, tag):
        count = 0
        for t in tag_list:
            if t == tag:
                count += 1
        return count
            
    def calculate_PRF(self, lines):
        text_list, ans_list, predict_list = [], [], []     
        for line in lines:
            if line != '\n':
                text_list.append(line.split('\t')[0])
                ans_list.append(line.split('\t')[2]) # 記錄第二列
                predict_list.append(line.split('\t')[3].replace('\n','')) # 記錄第三列
        
        # P、R、F計算核心
        # 第三列辨識正確個數 / 第三列辨識個數
        # 第三列辨識正確個數 / 第二列辨識個數
        # 綜合P、R指標
        print("ans_list and predict_list Loaded..\n")        
        totalP = 0
        error_list = []
        tag_set = self.getTotalTag(ans_list)
        #print(tag_set)
        print("-"*60)
        print("Precision\tRecall\t\ttag")
        print("-"*60)
        for tag in tag_set:
            correct = self.singleCorrect(text_list, ans_list, predict_list, error_list, tag)            
            P = correct / len(predict_list) * 100
            R = correct / self.countSingleTag(ans_list, tag) * 100
            totalP += P
            print("%7.2f %%\t%7.2f %%\t" % (P, R), tag)
        print("total", "-"*60)        
        tol_correct = self.totalCorrect(ans_list, predict_list)
        tP = tol_correct / len(predict_list) * 100
        tR = tol_correct / len(ans_list) * 100
        print("%7.2f %%\t%7.2f %%\t%d / %d (correct / total)" % (tP, tR, tol_correct, len(ans_list)))
        print("\nerror:")
        for error in error_list:
            print(error)
        
    def printPRF(self):        
        with open(self.file,"r",encoding='utf-8') as f:
            lines = f.readlines()
        self.calculate_PRF(lines)   
        
if __name__ == '__main__':
    file = input("請輸入欲計算PRF檔案:\n")
    prf = crfPRF(file)
    prf.printPRF()
        