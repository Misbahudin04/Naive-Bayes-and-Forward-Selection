import pandas as pd
class Crossvalidation:

    def __init__(self,dcc,atribut_terpilih,dataset):
        self.__datasett = dcc.copy()
        self.__dataset = dataset
        self.__atribut_terpilih = atribut_terpilih
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

        print(self.latih1)
        print(self.latih2)
        print(self.latih3)
        print(self.latih4)
        print(self.latih5)
        print(self.latih6)
        print(self.latih7)
        print(self.latih8)
        print(self.latih9)
        print(self.latih10)

