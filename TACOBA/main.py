import numpy as np
import math
import pandas as pd
import naivebayes as nbb
import forwardselection as fs
import crossvalidation as cv
import Ujif as uf

dataset= pd.read_excel('data/nbfs.xlsx', header=0)
print('inipanjang',len(dataset))
dc = dataset.copy()
#dcc = dataset.copy()




'''========= FORWARD SELECTION ========'''
fss = fs.ForwardSelection(dc)

rsquare = fss.correlation()
#print('ini rsquare',rsquare)

urutanlist = fss.urutan()
#print('ini urutan',urutanlist)

'''========= UJI F ============'''
labels = dc['Classification']
features = dc.drop(['Classification'], axis=1)

fsig = pd.read_excel('data/sfig.xlsx', header=0)
#print(fsig.head(5))
UF = uf.UjiF(urutanlist,rsquare,features,labels,fsig)
UFF = UF.fhitung()
atribut_terpilih = UF.ftable()
#print(atribut_terpilih)

'''======================= Buat Dataset Baru ======================'''
eeay=[]
dcc= pd.DataFrame()

j=0
for i in atribut_terpilih:
    while j<len(dataset):
        eeay.append(dataset.iloc[j,i])
#        dcc.at[i, dc.columns[i]] = 1
        j+=1
    dcc[dc.columns[i]] = eeay
    #print('ini', eeay)
    eeay = []
    j=0

label = []
i=0
while i < len(dataset):
    label.append(dataset.loc[i,'Classification'])
    i+=1

dcc['Classification'] = label
#print(label)
#for i in atribut_terpilih:
#        dcc[dc.columns['Classification']] = label
#print(dataset.head(5))


#print(dcc)
#joy = np.append(eeay)
#eeay = [[2,3,4],
#        [2,3,4]]
#print('ini',joy)
#print('iniidai',eeay[2][1])
##for i in atribut_terpilih:
#        dcc[dc.columns[i]] = eeay
#print(eeay[1][1])
#print(dcc)

'''========= Cross Validation ============'''
cvv = cv.Crossvalidation(dcc,atribut_terpilih,dataset)
fold = cvv.nilai()
fold1 = cvv.kfold()
fold2 = cvv.kfold2()
fold3 = cvv.kfold3()
fold4 = cvv.kfold4()
fold5 = cvv.kfold5()
fold6 = cvv.kfold6()
fold7 = cvv.kfold7()
fold8 = cvv.kfold8()
fold9 = cvv.kfold9()
fold10 = cvv.kfold10()


'''========= NAIVE BAYES ============='''

atribut_dibuang = []

#print(atribut_terpilih[1])
#print(urutanlist)
#urutanlist.remove(2)
#print('inidia',urutanlist)
#i=0
#while i < len(urutanlist):
#    if atribut_terpilih[i] != urutanlist[i]:
#        atribut_dibuang.append(urutanlist[i])
##    i+=1
#print('ini atbuang',atribut_dibuang)

#datafinal = dataset.copy()
#datafinall = dataset.copy()
#i=0
#while i <len(atribut_terpilih):
#    datafinall = datafinall.drop(datafinal.columns[atribut_terpilih[i]], axis=1)
#    #datafinall = datafinall.drop(datafinal.columns[atribut_dibuang[i]], axis=1)
#    i+=1
#print(datafinal.head(5))
#print(datafinall.head(5))
#print(atribut_terpilih)

#print(datafinal.iloc[1,atribut_terpilih[1]])
#dataset_latih = dcc.iloc[19:116]             #split#
#datasetuji = dcc.iloc[0:17]
#dataset_uji = datasetuji      #split

#print(dataset_latih)
#print(dataset_uji)
#nb=nbb.Naivebayes(datasetuji)

#dl = nb.latih()         #model latih
#du = nb.uji(dataset_uji)           #predicted



#dc=dataset.copy()       #buat data baru untuk print
#labels = dc.iloc[:,-1]


#nb=Naivebayes(dataset)         #manggil kelas nb
#dl=nb.datalatih(dataset_latih)
#prediksii= nb.predicted        #manggil kelas hasil prediksi

#dc['prediksi']= predicted

#print(dc)

