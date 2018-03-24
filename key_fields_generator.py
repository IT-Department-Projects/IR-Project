import sys
from os import listdir
import PyPDF2 
import re
import simplejson 
import ast

KEY_FIELDS=[]
for file in listdir('/Users/aimanabdullahanees/Desktop/IR-Project/Latex/Population'):
	file_path='/Users/aimanabdullahanees/Desktop/IR-Project/Latex/Population/'+file

	if file_path != "/Users/aimanabdullahanees/Desktop/IR-Project/Latex/Population/.DS_Store":

		temp = open(file_path,'r').read().split('\n')

		#Getting Title
		title_list=temp[6].split('=')
		title = re.sub('[^ a-zA-Z0-9]', '', title_list[1])

		#Getting X-Label
		x_label_list=temp[7].split('=')
		x_label= re.sub('[^ a-zA-Z0-9]', '', x_label_list[1])

		#Getting Y-Label
		y_label_list=temp[8].split('=')
		y_label= re.sub('[^ a-zA-Z0-9]', '', y_label_list[1])

		#Getting X-min&X-max
		x_list=temp[9].split(',')
		x_min=x_list[0].split('=')[1]
		x_max=x_list[1].split('=')[1]

		#Getting Y-min&Y-max
		y_list=temp[10].split(',')
		y_min=y_list[0].split('=')[1]
		y_max=y_list[1].split('=')[1]

		file=file.split('.')
		filename = '/Users/aimanabdullahanees/Desktop/IR-Project/PDFs/Population_PDFs/' +file[0]+'.pdf'
		pdfFileObj = open(filename,'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		num_pages = pdfReader.numPages
		count = 0
		text = ""
		while count < num_pages:
			pageObj = pdfReader.getPage(count)
			count +=1
			text += pageObj.extractText()

		i = text.index('\n')
		text=text[i+1:]


		d={
		"Title":title,
		"X-Label":x_label,
		"Y-Label":y_label,
		"X-min":x_min,
		"X-max":x_max,
		"Y-min":y_min,
		"Y-max":y_max,
		"Description":text
		}

		KEY_FIELDS.append(d)


f = open('key_fields.json', 'w')
simplejson.dump(KEY_FIELDS, f)
f.close()


