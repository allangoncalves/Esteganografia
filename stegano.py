from functions import *
import sys

if sys.argv[2] == 'encode':
	try:
		image = Image.open(sys.argv[1])
	except IOError as e:
		print('Não foi possível abrir o arquivo corretamente.')
	if len(sys.argv[1])*8 < len(image.getdata()*3):
		length = image.size
		binarized = imageBin(image)
		modified = encode(textBin(sys.argv[3]),binarized)
		rgb = imageRGB(modified)
		imageSave(rgb, sys.argv[1], length)
	else:
		print("message doesn't fit.")
elif sys.argv[2] == 'decode':
	image = Image.open('modified_'+sys.argv[1])
	binarized = imageBin(image)
	decode(binarized)
