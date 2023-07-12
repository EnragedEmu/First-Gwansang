from celeba_download_demo import Curdir_loader

list_attr_celeba_filename = 'list_attr_celeba.txt'
cl = Curdir_loader()
df = cl.load_file_asDF(list_attr_celeba_filename)

male = df['Male']
mustache = df['Mustache']

heavy_makeup = df['Heavy_Makeup']
wearing_lipstick = df['Wearing_Lipstick']

corr = df[['Male', 'Mustache', 'Heavy_Makeup', 'Wearing_Lipstick']]

print(corr.corr())