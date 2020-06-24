import math, numpy as np
import math as mt

class ForwardSelection:

    def __init__(self, dataset):
        self.dataset = dataset
        self.__korelasii = {}
        self.__xsquare = {}
        self.__x = {}
        self.__y = {}
        self.__xy= {}
        self.__korelasicopy = {}
        indexlist = []
        self.__urutanatrbut = []
        #self.__big = {}
        #self.korelasii = []


    def correlation(self):
        x = 0
        y = 0
        n = len(self.dataset)
        '''=====================mencari jumlah x====================='''
        totx = 0
        while y < len(self.dataset.columns):
            while x <len(self.dataset):
                totx += self.dataset.iloc[x, y]
                self.__x.update({(self.dataset.columns[y]): totx})
                x+=1
            x=0
            totx = 0
            y+=1
        #print('ini x', self.__x)
        '''=====================mencari x kuadrat============================'''
        totxs = 0
        x=0
        y=0
        while y < len(self.dataset.columns):
            while x < len(self.dataset):
                totxs += (self.dataset.iloc[x, y]**2)
                self.__xsquare.update({(self.dataset.columns[y]): totxs})
                x += 1
            x = 0
            totxs = 0
            y += 1
        #print('ini xsquare', self.__xsquare)
        '''=====================mencari jumlah xy=========================='''
        x = 0
        y = 0
        totxss = 0
        while y < len(self.dataset.columns):
            while x < len(self.dataset):
                totxss += self.dataset.iloc[x, y] * self.dataset.iloc[x,-1]
                #print(totxss)
                self.__xy.update({(self.dataset.columns[y]): totxss})
                x += 1
            x = 0
            totxss = 0
            y += 1
        #print('ini xy', self.__xy)

        #===================================================================#
        #CAKNYO SALAH INIprint('ini x square',self.__xsquare)
        '''mencari a + b'''
        #z = 1
        #while y < len(self.dataset.columns)-1:
        #    while z < len(self.dataset.columns)-1:
        #        while x <len(self.dataset):
        #            cor = self.dataset.iloc[x,y] + self.dataset.iloc[x,z]  #mencari x+y
        #            print (cor)
        #            x += 1
        #        #   print('=====================')
        #        z += 1
        #    x = 0
        #Q    y += 1
        #    z=0
        #====================================================================

        '''INI MASUK KE KORELASI'''
        x=0
        z=1
        g=0
        n = len(self.dataset)
        #print('ini n',n)

        #print(self.__x[self.dataset.columns[y]])
        y = 0
        '''baru sum x y tinggal tambah rumus sudahnyo yang akar2'''
        while y < len(self.dataset.columns) - 1:
            #print(y)
            korelasix = (n*(self.__xy[self.dataset.columns[y]])-(self.__x[self.dataset.columns[y]] * self.__x[self.dataset.columns[-1]])) / ((mt.sqrt((n*((self.__xsquare[self.dataset.columns[y]]))) - ((self.__x[self.dataset.columns[y]])**2)))*(mt.sqrt((n * ((self.__xsquare[self.dataset.columns[-1]]))) - ((self.__x[self.dataset.columns[-1]]) ** 2))))
            self.__korelasii.update({(self.dataset.columns[y]): korelasix})
            #self.__xsquare.update({(self.dataset.columns[y]): totxs})
            #print(self.__korelasii)
            y += 1
        y=0
        #print('korelasi',self.__korelasii)
        self.__korelasicopy = self.__korelasii

        y=0  #POSITIFIN KORELASI
        while y < len(self.dataset.columns) - 1:
            self.__korelasicopy.update({(self.dataset.columns[y]): abs(self.__korelasicopy[self.dataset.columns[y]])})
            y+=1

        #print('in korelasi di +in',self.__korelasicopy)
        sortingkorelasi = []
        sortingkorelasi.append(sorted(self.__korelasicopy.values(),reverse = True))
        #print('in korelasi di +in', self.__korelasicopy)
        #print('ini sorting', sortingkorelasi)

        i=0
        j=0
        z=0

        #if sortingkorelasi[0][1] == self.__korelasicopy[self.dataset.columns[6]]:
        #    print('aaa')
        while i <len(self.__korelasicopy):
            while j<len(self.__korelasicopy):
                if sortingkorelasi[z][i] == self.__korelasicopy[self.dataset.columns[j]]:
                    self.__urutanatrbut.append(j)
                    break
                j+=1
            j=0
            i+=1
        #print('urutan',urutanatrbut)

        ##print('ini',self.__urutanatrbut)
       #for i in urutanatrbut:
        #    print ('ini',self.__korelasicopy[self.dataset.columns[i]])

        return sortingkorelasi

    def urutan(self):
        ##print('jangan',self.__urutanatrbut)
        return self.__urutanatrbut






        #print(sortingkorelasi[5])
        #print('ini sorting',sortingkorelasi)
        #print('iniiiii',sortingkorelasi[0])

        #while i<len(self.__korelasicopy):
        #    while j<len(self.__korelasicopy):
         #       sortingkorelasi.append(sorted(self.__korelasicopy.values()))




        #i = 0
        #j = 0 #BUBLE SORT
        #while i<len(self.__korelasicopy)-1:
        #    while j<2:

        #        m = self.__korelasicopy[self.dataset.columns[j]]
        #        n = self.__korelasicopy[self.dataset.columns[j+1]]
        #        print('ini n',self.__korelasicopy[self.dataset.columns[j+1]])
        #        print('ini m',m,'ini n',n)
        #        if  m > n:
        #            temp = self.__korelasicopy[self.dataset.columns[j]]
        #            self.__korelasicopy.update({self.dataset.columns[j]:self.dataset.columns[j+1]})
        #            self.__korelasicopy[self.dataset.columns[j+1]] =temp
                    #print(self.__korelasii[self.dataset.columns[i]])
                    #print(self.__korelasii[self.dataset.columns[i + 1]])
       #          #  print(j)
        #        j+=1
        #    j=0
        #    i+=1

        #i=0
        #while i < len(self.__korelasicopy)-1:
        #    m = self.__korelasicopy[self.dataset.columns[i]]
        #    n = self.__korelasicopy[self.dataset.columns[i+1]]
        #    if m > n:
        #        print('gas')
        #    i+=1


        #print('ini korelasi akhir',self.__korelasicopy)


























        #print('ini copyan',self.__korelasicopy)
        #print('ini sorting', sorted(self.__korelasicopy.values()))
        #while y <len(self.dataset.columns) -1:

        #    y+=1
        #print(self.__korelasicopy)
        #print ('ini sorting',sorted(self.__korelasicopy.values()))
     
        #print(self.__x[self.dataset.columns[-1]])
        #self.korelasii.append(self.__x[self.dataset.columns[0]] + self.__x[self.dataset.columns[-1]])
        #print(self.korelasii)

    #def big(self):
    ##    y=0
    #    z=0
    #    print('printttt',self.__korelasii[self.dataset.columns[y]])
   #  #   while z < len(self.dataset.columns) - 1:
    #        while y < len(self.dataset.columns) - 1:
    #            bigg = self.__korelasii[self.dataset.columns[y]
    #            self.__big.update({self.dataset.columns : bigg]})
    #            print(' INI BIGGGG' ,self.__big[self.dataset.columns[y]])
    #            #if self.__big(self.dataset.columns[y]) < self.__korelasii[self.dataset.columns[y]]:
   #  #           #    self.__korelasicopy.update({self.dataset.columns[y]:big})
    #            #    print('inidia',self.__korelasicopy)
    #            y+=1
    #        y=0
    #        z+=1