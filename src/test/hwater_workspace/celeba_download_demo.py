import sys, os
import numpy as np
import pandas as pd
import csv
'''
cur_dir = os.getcwd()
test_dir = os.path.join(cur_dir, os.pardir)
src_dir = os.path.join(test_dir, os.pardir)
FirstGwansang_dir = os.path.join(src_dir, os.pardir)
Gits_dir = os.path.abspath(os.path.join(FirstGwansang_dir, os.pardir))

sys.path.append(Gits_dir)




list_attr_celeba_path = 'C://Workspace/Gits/CelebA/Anno/list_attr_celeba.txt'

df = pd.read_csv(list_attr_celeba_path, sep=' ')
print(df)

with open(list_attr_celeba_path, 'r') as list_attr_celeba:
    data_num = int(list_attr_celeba.readline()) # 202599 data
    list_attr_data = list_attr_celeba.read()

    
    print(data_num)'''

class Curdir_loader:
    def __init__(self):
        self.cur_dir = os.path.abspath(os.getcwd())

    def show_filename(self):
        print('list_attr_celeba.txt')

    def load_file_asDF(self, filename):
        file_path = os.path.join(self.cur_dir, filename)
        df = pd.read_csv(file_path, sep='\s+')

        return pd.DataFrame(data=df)

'''
list_attr_celeba_filename = 'list_attr_celeba.txt'
cl = Curdir_loader()
df = cl.load_file_asDF(list_attr_celeba_filename)

print(df.columns)
'''
