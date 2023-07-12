import sys, os
import pandas as pd

anno = 'processed\\CelebA_1024\\Anno'
img = 'processed\\CelebA_1024\\Img'

test_dir = os.getcwd()
data_dir = os.path.abspath(os.path.join(test_dir, os.pardir))
sys.path.append(data_dir)

anno_dir = os.path.join(data_dir, anno)
img_dir = os.path.join(data_dir, img)

def load_file_asDF(filename):
    file_path = os.path.join(anno_dir, filename)
    df = pd.read_csv(file_path, sep='\s+')
    return pd.DataFrame(data=df)



#df = load_file_asDF('list_attr_celeba_1024.txt')

from matplotlib import pyplot as plt
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from PIL import Image

jpg1 = Image.open(os.path.join(img_dir, '000001.jpg'))

print(jpg1)

from torchvision import transforms

convert_tensor = transforms.ToTensor()

cvt_jpg1 = convert_tensor(jpg1)
print(cvt_jpg1)

gray_jpg1 = cvt_jpg1.mean(dim=0)
print(gray_jpg1)
print(gray_jpg1.shape)

imshow(gray_jpg1)
plt.show()