from PIL import Image
import numpy as np
import sys

def night_day(img_name):
    img = Image.open(img_name)
    im_np = np.asarray(img)
    height, width = im_np.shape[0], im_np.shape[1]
    gray_image = im_np.dot([0.299,0.587,0.144])
    # print(gray_image.shape)
    total = gray_image.shape[0]*gray_image.shape[1]
    black = (gray_image < 50).sum()
    if black > total/2 :
        # print(img_name)
        return 'Night'
    return 'Day'

if __name__== "__main__":
    print(night_day(sys.argv[1]))