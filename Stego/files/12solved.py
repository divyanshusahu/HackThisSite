from PIL import Image

im = Image.open('12.bmp','r')
width,height = im.size

pix = im.load()
text = ''

for i in range(height) :
	for j in range(width) :
		n = pix[j,i]
		text += chr(255-n)

f = open('12.zip','w')
f.write(text)
f.close()