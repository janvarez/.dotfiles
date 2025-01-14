import os

def detect_language():
	Language_installed=os.popen("locale | grep LANG").read()
	if "fr" in Language_installed:
		Language="French"
	elif "de" in Language_installed:
		Language="German"
	elif "pt" in Language_installed:
		Language="Portuguese"
	elif "it" in Language_installed:
		Language="Italian"
	else:
		Language="English"
	return Language


def Inxi_Search(string,Total_Clean):
	Results=[]
	for line in Total_Clean:
		if string in line:
			#print(line)
			deb=line.find(string)
			#res=string[:deb]
			res=line[deb+len(string)+1:]
			#print (deb)
			Results.append(res)
	return Results



def Write_File(File_to_Write,content):
	f = open(File_to_Write, 'w')
	f.write(content)  # python will convert \n to os.linesep
	f.close()  # you can omit in most cases as the destructor will call it
