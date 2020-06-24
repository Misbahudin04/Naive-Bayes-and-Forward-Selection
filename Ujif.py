import math as mt
import pandas as pd
import naivebayes as nbb
import crossvalidation as cv

class   UjiF :
    def __init__(self,urutanatribut,rsquare,features,labels,fsig,dataset):
        self.__urutanatribut = urutanatribut
        self.__rsquare = rsquare
        self.__feature = features
        self.__labels = labels
        self.__fsig = fsig
        self.__dataset = dataset
        self.fhitungg = []
        self.ftabell = []
        self.det1 = []
        self.det2 = []
        self.ftables = []
        self.__hasil = []

    def fhitung(self):
        i =0
        n = len(self.__feature)
        k = 1
        while i<len(self.__feature.columns):
            k += 1
            self.fhitungg.append((self.__rsquare[0][i] *(n-k-1)) / (k*(1-self.__rsquare[0][i])) )
            ###print('ini fhitung',self.fhitungg)
            i+=1

        ##print('ini fhitung',self.fhitungg)

        ##print('inipanjang', len(self.__feature.columns) )
        ##print('inirsquare',self.__rsquare[0][1])

    def ftable(self):
        k = 1
        n = len(self.__feature)
        i =0
        while i < len(self.__feature.columns):
            k+=1
            self.det1.append(k - 1)
            self.det2.append(n - k)
            i+=1
        ##print('det1', self.det1, 'det2', self.det2)
        ##print('ini belum',self.det2[1])
        #print('ini sudah', self.det2[1] = 21)
        #self.det2[1] = 21

        i = 0
        while i< len(self.__feature.columns):
            if 10 < self.det1[i] <= 12:
                self.det1[i] = 11
            elif 12 < self.det1[i] <= 15:
                self.det1[i] = 12
            elif 15 < self.det1[i] <= 20:
                self.det1[i] = 13
            elif 20 < self.det1[i] <= 24:
                self.det1[i] = 14
            elif 24 < self.det1[i] <= 30:
                self.det1[i] = 15
            elif 30 < self.det1[i] <= 40:
                self.det1[i] = 16
            elif 40 < self.det1[i] <= 60:
                self.det1[i] = 17
            elif 60 < self.det1[i] <= 120:
                self.det1[i] = 18
            elif self.det1[i] >120:
                self.det1[i] = 19
            i+=1
        i = 0
        while i< len(self.__feature.columns):
            if 25 < self.det2[i] <= 30:
                self.det2[i] = 26
            elif 30 < self.det2[i] <= 40:
                self.det2[i] = 27
            elif 40 < self.det2[i] <= 50:
                self.det2[i] = 28
            elif 50 < self.det2[i] <= 60:
                self.det2[i] = 29
            elif 60 < self.det2[i] <= 100:
                self.det2[i] = 30
            elif 100 < self.det2[i] <= 120:
                self.det2[i] = 31
            elif self.det2[i] >120:
                self.det2[i] = 32
            i+=1


        ##print('det1',self.det1,'det2',self.det2)
        ##print('ini det1 baris 1',self.det1[1],'ini det1 baris 2',self.det2[1])
        ##print('ininah',self.__fsig.iloc[1,1])
        ###print('ini nilai det',self.det1,self.det2)
        i=0
        while i<len(self.__feature.columns):
            self.ftables.append(self.__fsig.iloc[self.det2[i],self.det1[i]])
            i+=1
        ##print(self.fhitungg)
        ##print(self.ftables)

        #self.ftables.append(self.__fsig.loc(self.det1[1]),self.det2[1])
        i=0
        while i<len(self.__feature.columns):
            ###print('f hitung',self.fhitungg[i],'f tab',self.ftables[i])
            if self.fhitungg [i] > self.ftables [i]:
                ##print(self.fhitungg[i],self.ftables[i])
                self.__hasil.append(self.__urutanatribut[i])

            i+=1

        #print('ini apa ya',self.__hasil)
        return self.__hasil

    def datafilter(self):
        eeay = []
        dccc = pd.DataFrame()
        print(self.__hasil)

        label = []
        i = 0
        while i < len(self.__dataset):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1
        dccc['Classification'] = label
        ###print('pertama', dccc)
        datasetfold = dccc.copy()
        #print('kedua', datasetfold)
        #features = ds.drop(['Classification'], axis=1)
        print()
        atributtahap = []
        j = 0
        for i in self.__hasil:
            print(i)
            datasetfold = datasetfold.drop(['Classification'], axis = 1)
            while j < len(self.__dataset):
                eeay.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1
                j += 1
            datasetfold[self.__dataset.columns[i]] = eeay
            datasetfold['Classification'] = label
            #print('iniqq', datasetfold)
            atributtahap.append(i)
            #print('ini atribut tahap',atributtahap)
            cvv = cv.Crossvalidation(datasetfold, atributtahap, self.__dataset,i)
            dictionary di append disini
            fold = cvv.panggilfold()


            # 1
            eeay = []
            j = 0



        #nb = nbb.Naivebayes(self.__dataset)
        #dl = nb.test()
        #print('ini1',dccc)
        #return dccc