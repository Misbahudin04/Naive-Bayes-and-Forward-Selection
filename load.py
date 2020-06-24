import pandas as pd

class load_dataset:

    def __init__(self, file):
        self.file = file

    def load(self):
        data = pd.read_csv(self.file, header=0)
        #print("File berhasil dimuat.")
        return (data)
