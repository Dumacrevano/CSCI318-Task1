from PIL import Image
import random
import cv2
from skimage.measure import compare_ssim

def image_feature_compare(imageA,imageB):
    imageA = cv2.imread(imageA)
    imageB = cv2.imread(imageB)
    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")

    # convert similarity percentage into distance between 0 to 100
    dist = abs(score * 100 - 100)
    return dist

# print(dist)

def image_color_avg_rgb(image):
    r = 0
    g = 0
    b = 0
    im = Image.open(image)
    pixelMap = im.load()
    rgb = []
    img = Image.new( im.mode, im.size)
    for i in range(img.size[0]):
        for j in range(0, img.size[1]):
            rgb_pixel = pixelMap[i,j]
            mapped = [rgb_pixel[0],rgb_pixel[1], rgb_pixel[2]]
            r+=rgb_pixel[0]
            g+=rgb_pixel[1]
            b+=rgb_pixel[2]
            rgb.append(mapped)
    red_average= (r/len(rgb))
    green_average=(g/len(rgb))
    blue_average=(b/len(rgb))
    return red_average,green_average,blue_average




def image_color_difference(image1,image2):
    rgb_difference_percentage=[]
    image1_RGB=image_color_avg_rgb(image1)
    image2_RGB=image_color_avg_rgb(image2)
    print(image1_RGB)
    print(image2_RGB)
    for x in range(3):
        big_num=image1_RGB[x] if image1_RGB[x]>=image2_RGB[x] else image2_RGB[x]
        c = (abs(image1_RGB[x] - image2_RGB[x])) / big_num * 100
        rgb_difference_percentage.append(c)
    final_average=sum(rgb_difference_percentage)/3
    print(rgb_difference_percentage)
    return final_average

