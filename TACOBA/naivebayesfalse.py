import numpy as np
import math as mt
import pandas as pd

class Naivebayes:
    def __init__(self,dataset_latih,dataset_uji):
        self.dataset_latih = dataset_latih
        self.dataset_uji =  dataset_uji
        self.__meanClass = {}
        self.__stdClass = {}
        self.__uniqueClass = [0,1]
        #self.__classprob= {}

    def datalatih(self):
        #print('ini data latih')
        #print(self.dataset_latih)
        #allcolumns = list(self.dataset_latih)
        #KolomKelas = allcolumns[-1]  # untuk mencari kolom kelas
        #self.__uniqueClass = self.dataset_latih.__getattr__(KolomKelas)
        i=0
        while i < len(self.__uniqueClass):
            print(self.__uniqueClass[i])
            i+=1
        a = 1
        b = 2
        i=0
        j=0
        k=0
        while i < len(self.dataset_latih):
            if self.dataset_latih.loc[i,'Classification'] == 1:
                j+=1
            else:
                k+=1
            i+=1
        classproba = j / len(self.dataset_latih)*100
        classprobb = k / len(self.dataset_latih)*100

        o=0
        j=0
        while o <len(self.__uniqueClass):
            tdf = self.dataset_latih.loc[self.dataset_latih.loc[:,-1] == self.__uniqueClass[o]]
            while j < (len(self.dataset_latih.columns) - 1):
                std = tdf.iloc[:,j].std()
                mean = self.dataset_latih.iloc[:,j].std()
                self.__meanClass.update({(self.__uniqueClass[o],self.dataset_latih.columns[j]):mean})
                print('mean',self.__meanClass)
                j+=1
            j=0
            o+=1
        print(self.dataset_latih.iloc[:,-1])
        print('Probabilitas kelas a=',classproba)
        print('Probabilitas kelas b=',classprobb)
    def datauji(self):
        print('ini data uji')
        #print(self.dataset_uji)