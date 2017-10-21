s = '00 00 16 16 17 17 17 16 16 16 16 17 17 16 16 17 17 16 16 17 17 16 17 17 17 16 17 17 16 17 16 16 16 16 17 17 16 16 16 16 17 16 17 17 17 16 16 17 17 16 16 17 17 16 17 17 16 00 00'
s = s.replace(' ','')
s = s[4:-4]
s = s.replace('16','0')
s = s.replace('17','1')

#print s

text = ''
char = '' 
for i in range(7,len(s)) :
	char += s[i]
	if len(char) == 8 :
		text += chr(int(char,2))
		#print len(char)
		#print int(char,2)
		char = ''
#print text

char1 = ''
for i in range(0,7) :
	char1 += s[i]

char1 =  char1 + '0'
#print chr(int(char1,2))

password = chr(int(char1,2)) + text
print password