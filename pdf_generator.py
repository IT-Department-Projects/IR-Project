import sys
from os import listdir

#For plotting Graphs using Matplotlib
from matplotlib import pyplot as plt
from matplotlib import style
plt.rcParams.update({'figure.max_open_warning': 0})
import numpy as np
import pandas as pd
style.use('ggplot')

#Fetching data from Wikipedia using wikiapi
from wikiapi import WikiApi
wiki = WikiApi()
wiki = WikiApi({ 'locale' : 'en'})

#Support for creation of PDFs
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
Story=[]

incomplete=[]
for file in listdir('ABSOLUTE-PATH-FOR-GRAPHS-DIRECTORY'):
	file_path='ABSOLUTE-PATH-FOR-GRAPHS-DIRECTORY'+"/"+file
	
	#Paragraph Generator
	copy_file=file
	file=file.split('.')
	results = wiki.find(file[0])
	if len(results) != 0:
		article = wiki.get_article(results[0])
		Summary=article.summary
	
		#PDF Generator
		doc = SimpleDocTemplate("['ABSOLUTE-PATH-FOR-STORING-PDFs']"+file[0]+".pdf",pagesize=letter,
							rightMargin=72,leftMargin=72,
							topMargin=72,bottomMargin=18)
		
		title="<center><strong>"+file[0]+"</strong></center>"
		Story.append(Paragraph(title, styles["Title"]))

		logo = file_path
		im = Image(logo, 5*inch, 5*inch)
		Story.append(im)
		Story.append(Paragraph(Summary, styles["Normal"]))
		doc.build(Story)
		print("Done:--->",file[0])
	else:
		incomplete.append(copy_file)

print(incomplete)
