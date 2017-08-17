from functions import *
import sys

if sys.argv[2] == 'encode':
	image = Image.open(sys.argv[1])
	length = image.size
	binarized = imageBin(image)
	modified = encode(textBin(sys.argv[3]),binarized)
	rgb = imageRGB(modified)
	imageSave(rgb, sys.argv[1], length)
elif sys.argv[2] == 'decode':
	image = Image.open('modified_'+sys.argv[1])
	binarized = imageBin(image)
	decode(binarized)
