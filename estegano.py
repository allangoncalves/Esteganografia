import Image
import time


def imageBin(pic):
	newimage = list()
	for i in list(pic.getdata()):
		newimage.append(bin(i[0])[2:])
		newimage.append(bin(i[1])[2:])
		newimage.append(bin(i[2])[2:])
	return newimage

def textBin(message):
	binary = list()
	for i in message:
		binary.append(bin(ord(i))[2:])
	return binary

def encode(text, image):
	x = 0
	print(text)	
	for i in text:
		for j in list(i):
			image[x] = str(image[x])[:-1]+j
			x+=1
	for t in '00000011':
		image[x] = str(image[x])[:-1]+t
		x+=1
	return image

def imageSave(image, path, length):
	data = list()
	for i in image:
		data.append(tuple(i))
	newimage = Image.new('RGB', length)
	newimage.putdata(data)
	newimage.save('modified_'+path)

def imageRGB(imageBin):
	aux = 0
	newimage = list()
	pixel = list()
	for i in range(0,len(imageBin)):		
		pixel.insert(aux,int(imageBin[i],2))
		aux = (aux+1)%3							
		if (i+1)%3==0 and i!=0:
			newimage.insert(i,pixel)
			pixel = list()			
	return newimage


def decode(image):
	x = 0
	temp = str()
	message = str()
	for i in range(len(image)):
		for j in range(8):
			temp+=str(image[x])[-1]
			x+=1
		print(int(temp,2))
		if temp != '00000011':
			message+=temp
			temp = str()
		else:
			break
	print(int(message,2))		
		
image = Image.open('pepper50.bmp')
length = image.size
binarizada = imageBin(image)
modified = encode(textBin('J'),binarizada)
t1 = imageRGB(binarizada)
t2 = imageRGB(modified)
imageSave(t2,'PeppersRGB.bmp', length)
#testDecode = Image.open('modified_PeppersRGB.bmp')
#decodeBin = imageBin(testDecode)
#decode(decodeBin)
#print(t1[0])
#print(t2[0])
