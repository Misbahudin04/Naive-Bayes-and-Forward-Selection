import pandas as pd
import naivebayes as nbb
import APLIKASINAIVEBAYES as ab
class Crossvalidation:

    def __init__(self,dcc,atribut_terpilih,dataset,i):
        self.__datasett = dcc.copy()
        self.__dataset = dataset
        self.__atribut_terpilih = atribut_terpilih
        self.i = i
        self.uji1 = []
        self.uji2 = []
        self.uji3 = []
        self.uji4 = []
        self.uji5 = []
        self.uji6 = []
        self.uji7 = []
        self.uji8 = []
        self.uji9 = []
        self.uji10 = []
        self.data = []
    def kfold(self):
        self.fold1 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji1:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold1[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.uji1):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.fold1['Classification'] = label
        #print('fold 1',self.fold1)
        #self.fold1.to_excel(r'fold11.xlsx', sheet_name='fold 1')
        #======naive bayes=========
        #nb = nbb.Naivebayes(self.train1)
        #du = nb.uji(self.fold1)  # model latih


        return self.fold1

    def kfold2(self):
        self.fold2 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji2:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold2[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.uji2):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.fold2['Classification'] = label
        print("fold 1")
        return self.fold2

    def kfold3(self):
        self.fold3 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji3:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold3[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []
        label = []
        i=0
        while i < len(self.uji3):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1
        print("fold 1")
        self.fold3['Classification'] = label
        return self.fold3

    def kfold4(self):
        self.fold4 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji4:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold4[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []
        label =[]
        i = 0
        while i < len(self.uji4):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.fold4['Classification'] = label
        return self.fold4

    def kfold5(self):
        self.fold5 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji5:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold5[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.uji5):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1
        self.fold5['Classification'] = label
        return self.fold5

    def kfold6(self):
        self.fold6 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji6:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold6[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.uji6):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1
        self.fold6['Classification'] = label
        return self.fold6

    def kfold7(self):
        self.fold7 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji7:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold7[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.uji7):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1
        self.fold7['Classification'] = label
        return self.fold7

    def kfold8(self):
        self.fold8 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji8:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold8[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.uji8):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1
        self.fold8['Classification'] = label
        return self.fold8

    def kfold9(self):
        self.fold9 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji9:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold9[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.uji9):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1
        self.fold9['Classification'] = label
        return self.fold9

    def kfold10(self):
        self.fold10 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.uji10:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.fold10[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.uji10):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1
        self.fold10['Classification'] = label
        return self.fold10

    def nilai(self):
        foldd = len(self.__datasett) / 10
        print(foldd)
        i=0
        j=0

        '''=================== Nilai Index Atribut Latih ========================='''
        k=0
        while i<(len(self.__datasett)):
            while j <foldd:
                if i <foldd:
                    self.uji1.append(i)
                elif i < foldd*2:
                    self.uji2.append(i)
                elif i < foldd*3:
                    self.uji3.append(i)
                elif i < foldd*4:
                    self.uji4.append(i)
                elif i < foldd*5:
                    self.uji5.append(i)
                elif i < foldd*6:
                    self.uji6.append(i)
                elif i < foldd*7:
                    self.uji7.append(i)
                elif i < foldd*8:
                    self.uji8.append(i)
                elif i < foldd*9:
                    self.uji9.append(i)
                elif i < foldd*10:
                    self.uji10.append(i)
                i+=1
                j+=1
            j=0
        '''=================== Nilai Index Atribut Latih ========================='''
        i=0
        j=0
        while i < len(self.__datasett):
            self.data.append(i)
            i+=1

        self.latih1 = self.data.copy()
        self.latih2 = self.data.copy()
        self.latih3 = self.data.copy()
        self.latih4 = self.data.copy()
        self.latih5 = self.data.copy()
        self.latih6 = self.data.copy()
        self.latih7 = self.data.copy()
        self.latih8 = self.data.copy()
        self.latih9 = self.data.copy()
        self.latih10 = self.data.copy()

        print(self.uji1)


        for j in self.uji1:
            self.latih1.remove(self.uji1[j])
            self.latih2.remove(self.uji2[j])
            self.latih3.remove(self.uji3[j])
            self.latih4.remove(self.uji3[j])
            self.latih5.remove(self.uji3[j])
            self.latih6.remove(self.uji3[j])
            self.latih7.remove(self.uji3[j])
            self.latih8.remove(self.uji3[j])
            self.latih9.remove(self.uji3[j])
            self.latih10.remove(self.uji3[j])
            j+=1

        #print(self.latih1)
        #print(self.latih2)
        #print(self.latih3)
        #print(self.latih4)
        #print(self.latih5)
        #print(self.latih6)
        #print(self.latih7)
        #print(self.latih8)
        #print(self.latih9)
        #print(self.latih10)

    '''====================== Buat Tabel Latih======================'''
    def latihh1(self):
        self.train1 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih1:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train1[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.latih1):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.train1['Classification'] = label
        #print('latih 1', self.train1)

        nb = nbb.Naivebayes(self.train1)
        dl = nb.latih()
        self.kfold()
        du = nb.uji(self.fold1)
        print('IA',du)
        #UI = ab.New_Toplevel()
        #UII = UI.config(1)
        #self.train1.to_excel(r'train11.xlsx', sheet_name='train 1')
        return self.train1

    def latihh2(self):
        self.train2 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih2:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train2[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.latih2):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1
        print("latih 2")
        self.train2['Classification'] = label

        nb = nbb.Naivebayes(self.train2)
        dl = nb.latih()
        self.kfold2()
        du = nb.uji(self.fold2)
        print('IA', du)

        return self.train2

    def latihh3(self):
        self.train3 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih3:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train3[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.latih3):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.train3['Classification'] = label

        nb = nbb.Naivebayes(self.train3)
        dl = nb.latih()
        self.kfold3()
        du = nb.uji(self.fold3)

        return self.train3

    def latihh4(self):
        self.train4 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih4:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train4[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.latih4):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.train4['Classification'] = label

        nb = nbb.Naivebayes(self.train4)
        dl = nb.latih()
        self.kfold4()
        du = nb.uji(self.fold4)

        return self.train4

    def latihh5(self):
        self.train5 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih5:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train5[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []
        label = []
        i = 0
        while i < len(self.latih5):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.train5['Classification'] = label

        nb = nbb.Naivebayes(self.train5)
        dl = nb.latih()
        self.kfold5()
        du = nb.uji(self.fold5)

        return self.train5

    def latihh6(self):
        self.train6 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih6:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train6[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []
        label = []
        i = 0
        while i < len(self.latih6):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.train6['Classification'] = label

        nb = nbb.Naivebayes(self.train6)
        dl = nb.latih()
        self.kfold6()
        du = nb.uji(self.fold6)

        return self.train6

    def latihh7(self):
        self.train7 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih7:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train7[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []
        label = []
        i = 0
        while i < len(self.latih7):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.train7['Classification'] = label

        nb = nbb.Naivebayes(self.train7)
        dl = nb.latih()
        self.kfold7()
        du = nb.uji(self.fold7)

        return self.train7

    def latihh8(self):
        self.train8 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih8:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train8[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.latih8):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.train8['Classification'] = label

        nb = nbb.Naivebayes(self.train8)
        dl = nb.latih()
        self.kfold8()
        du = nb.uji(self.fold8)

        return self.train8

    def latihh9(self):
        self.train9 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih9:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train9[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []

        label = []
        i = 0
        while i < len(self.latih9):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.train9['Classification'] = label

        nb = nbb.Naivebayes(self.train9)
        dl = nb.latih()
        self.kfold9()
        du = nb.uji(self.fold9)

        return self.train9

    def latihh10(self):
        self.train10 = pd.DataFrame()
        eeays = []
        #print('att',self.__atribut_terpilih)

        for i in self.__atribut_terpilih:
            #print('i',i)
            for j in self.latih10:
                #print('y',j)
                eeays.append(self.__dataset.iloc[j, i])
                #        dcc.at[i, dc.columns[i]] = 1

            self.train10[self.__dataset.columns[i]] = eeays
            #print('ini', eeays)
            eeays = []
        label = []
        i = 0
        while i < len(self.latih10):
            label.append(self.__dataset.loc[i, 'Classification'])
            i += 1

        self.train10['Classification'] = label

        nb = nbb.Naivebayes(self.train10)
        dl = nb.latih()
        self.kfold10()
        du = nb.uji(self.fold10)

        return self.train10

    def test(self):
        print('test')

    def panggilfold(self):
        #cvv = cv.Crossvalidation(dcc, atribut_terpilih, dataset)
        # Dataset Uji
        self.nilai()

        # Dataset Training

        self.latihh1()

        # print(train1)
        self.latihh2()
        self.latihh3()
        self.latihh4()
        self.latihh5()
        self.latihh6()
        self.latihh7()
        self.latihh8()
        self.latihh9()
        self.latihh10()

        #print("ANJAYYY")
        #self.test()

        self.kfold2()
        self.kfold3()
        self.kfold4()
        self.kfold5()
        self.kfold6()
        self.kfold7()
        self.kfold8()
        self.kfold9()
        self.kfold10()





