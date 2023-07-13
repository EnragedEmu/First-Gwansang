import sys, os
import pandas as pd
from torchvision import transforms
from PIL import Image        

class CelebALoader:
    def __init__(self):
        celeba_dir = os.path.dirname(__file__)
        self.anno_dir = os.path.join(celeba_dir, 'Anno')
        self.img_dir = os.path.join(celeba_dir, 'Img')
    
    def get_filenames(self):
        print('In Anno: list_attr_celeba_1024.txt,\n \
                        list_bbox_celeba_1024.txt,\n \
                        list_landmarks_align_celeba_1024.txt,\n \
                        list+landmarks_celeba_1024.txt')
        print('In Img: 000001.jpg ~ 001024.jpg')

    def load_anno(self, filename, as_DF=True):
        file_path = os.path.join(self.anno_dir, filename)
        if as_DF:
            df = pd.read_csv(file_path, sep='\s+')
            return pd.DataFrame(data=df)
        else:
            pass
            
    def load_img(self, startIdx=1, endIdx=1024, toTensor=True, gray=True):
        images = []
        for idx in range(startIdx, endIdx + 1):
            filename = '{:06d}.jpg'.format(idx)
            jpg = Image.open(os.path.join(self.img_dir, filename))
            convert_tensor = transforms.ToTensor()
            jpg_tensor = convert_tensor(jpg)
            jpg_gray = jpg_tensor.mean(dim=0)
            if toTensor:
                if gray:
                    images.append(jpg_gray)
                else:
                    images.append(jpg_tensor)
            else:
                images.append(jpg)

        return images