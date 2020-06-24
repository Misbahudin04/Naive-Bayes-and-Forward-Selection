import numpy as np
import math as mt
import time
import pandas as pd

class Naivebayes:
    def __init__(self,dataset_latih):
        self.__datalatih = dataset_latih.copy()
        #self.__datauji = dataset_uji
        self.__meanClass = {}
        self.__stdClass = {}
        self.__uniqueClass = np.empty([1, 1])
        self.__classprob = {}

    def latih(self):

        #print(self.__datalatih)
        '''GaussianNB.fit(self.datalatih)'''
        allcolumns = list(self.__datalatih)
        KolomKelas = allcolumns[-1] #untuk mencari kolom kelas
        self.__uniqueClass = self.__datalatih.__getattr__(KolomKelas).unique()
        i = 0

        while i < len(self.__uniqueClass):  #menghitung probabilitas nilai 1 ada brapa, dan nilai label 0 ada berapa
            #print(self.__uniqueClass[i])
            tempprob = len(self.__datalatih.loc[self.__datalatih.iloc[:, -1] == self.__uniqueClass[i]]) / len(self.__datalatih)
            self.__classprob.update({self.__uniqueClass[i]: tempprob})  #dictionary ({ keys : value})
            i += 1

        i = 0
        j = 0

        while i < len(self.__uniqueClass):
            tdf = self.__datalatih.loc[self.__datalatih.iloc[:, -1] == self.__uniqueClass[i]]
            while j < (len(self.__datalatih.columns) - 1):
                mean = tdf.iloc[:, j].mean() #menghitung rata2 setiap isi atribut j itu adalah atribut
                standardeviasi = tdf.iloc[:, j].std() #standar deviasi antar aribut, i itu label 0 atau 1
                self.__meanClass.update({(self.__uniqueClass[i], self.__datalatih.columns[j]): mean}) # nyimpen rata2 setiap atribut( berdasarkan label 1 atau 0) dijadiken list #di(keys,keys:value)
                self.__stdClass.update({(self.__uniqueClass[i], self.__datalatih.columns[j]): standardeviasi}) #nyimpen std seperti diatas
                j += 1
            j = 0
            i += 1
        print("LATIH SELESAI")
        #print(self.__stdClass)
        #print(self.__meanClass)


    def uji(self,dataset_uji):
        i = 0
        datauji = dataset_uji.copy()  #ngapo di copy
        datapredik = datauji.copy()
        datapredik['PREDIKSI'] = 'NaN'
        totalprob = {}

        while i < len(datauji):  #seluruh record
            j = 0
            while j < len(self.__uniqueClass): #j kurang dari panjang kelas yaitu 2 (0 dan 1)
                k = 0
                pxctotal = 1
                while k < len(datauji.columns) - 1:  #k itu setiap atribut #banyak kolom

                    x = datauji.iat[i, k] #x sama dengan data record 1 (i) pada kolom 1 (k) atau dengan kata lain x ini adalah nilai atribut pada data latih


                    epower = (-(mt.pow((x - self.__meanClass[self.__uniqueClass[j], datauji.columns[k]]), 2) / (  # x (isi atribut) - rata2 unique clas 0 / 1 pada kolom tergantung k)
                                2 * mt.pow(self.__stdClass[self.__uniqueClass[j], datauji.columns[k]], 2))))  # -(x-mean clas) /  std deviasi kelas) kondisi pangkat atas
                    pxc = (1 / (mt.sqrt(2 * mt.pi) * self.__stdClass[self.__uniqueClass[j], datauji.columns[k]])) * mt.pow(mt.e,
                                                                                                                               epower) #kondisi utuh rumus 1/ akar 2 pi * stdviasi

                    pxctotal = pxctotal * pxc #untuk setiap probab dari 1 ataupun 0 yang dihasilkan pada setiap atribut
                    k += 1
                totalprob.update({self.__uniqueClass[j]: (pxctotal * self.__classprob[self.__uniqueClass[j]])}) #total probabilitas 1 atau 0

                j += 1

            m = 0
            big = 0
            while m < len(totalprob): #jika m kurang dari setiap probabilitas antara atribut 1 / 0, jadi m<2 (prob atribut 1 / 0)
                if big < totalprob[self.__uniqueClass[m]]:
                    big = totalprob[self.__uniqueClass[m]]
                    datapredik.loc[i, 'PREDIKSI'] = self.__uniqueClass[m]  #data prediksi pada baris record 1 diisi ke tabel isi. #data predik ke i
                m += 1

            i += 1
        return datapredik
        #datapredik.to_excel(r'outputss.xlsx',sheet_name='Data Uji Satu')
        #datapredik.to_excel(r'CM22331.xlsx')
        tabelcf = pd.DataFrame(0, self.__uniqueClass, self.__uniqueClass) #memasukan ke bentuk tablel panda
        print(tabelcf)
        i = 0
        while i<len(datapredik): #menghitung setiap data predik

            tabelcf.at[datapredik.iat[i, -1], datapredik.iat[i, -2]] = tabelcf.at[
                                                                           datapredik.iat[i, -1], datapredik.iat[
                                                                               i, -2]] + 1
            i+=1
        # Total sum per row:
        tabelcf.loc['Total', :] = tabelcf.sum(axis=0)
        # Total sum per column:
        tabelcf.loc[:, 'Total'] = tabelcf.sum(axis=1)
        i = 0
        TPTN = 0
        TP = 0
        FN = 0
        FP = 0
        while i < (len(tabelcf) - 1):
            TPTN = TPTN + tabelcf.iat[i, i]
            TP = TP
            i += 1

        TP = TP + tabelcf.iat[0, 0]
        FP = FP + tabelcf.iat[0, 1]
        FN = FN + tabelcf.iat[1, 0]

        print('tp', TP)
        print('FP', FP)
        print('FN', FN)

        accuracy = TPTN / len(datauji)
        precision = TP / (TP + FP)
        recall = TP / (TP + FN)

        tesa = accuracy*100
        tesa = "{0:.2f}".format(tesa)
        print("Accuracy= {}".format(accuracy))

        tesb = precision * 100
        tesa = "{0:.2f}".format(tesb)
        print("Precision= {}".format(precision))

        tesc = recall * 100
        tesa = "{0:.2f}".format(tesc)
        print("Recall= {}".format(recall))

        print(tabelcf)

        #tabelcf.to_excel(r'outputs.xlsx', sheet_name='Confusion matrix 1')





