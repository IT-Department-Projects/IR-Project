import csv
import numpy as np
import math
import ast
from operator import itemgetter

documents=[]
file_path='tfidf.csv'
file=open(file_path, "r")
reader = csv.reader(file)
for line in reader:
	documents.append(line)

###Accessing TFIDF_query###
file_path='tfidf_query.txt'
f1 = open(file_path, 'r')
query=f1.read()
query = ast.literal_eval(query)
f1.close()

del documents[0]
query=list(map(float, query))

flag=1
COS_SIM=[]
for i in range(len(documents)):
	document=list(map(float, documents[i]))
	numerator=np.multiply(document,query)
	numerator=numerator.tolist()
	numerator=sum(numerator)
	a=np.square(query)
	a=a.tolist()
	a=sum(a)
	a=math.sqrt(a)
	b=np.square(document)
	b=b.tolist()
	b=sum(b)
	b=math.sqrt(b)
	if (a*b) == 0:
		flag=0
		break
	cos_sim=numerator/(a*b)
	COS_SIM.append([i+1,cos_sim])


if flag == 0:
	print("Your search did not match any documents.")
else:
	print("top-10")
	COS_SIM.sort(key=itemgetter(1), reverse=True)
	print(COS_SIM[0:11])



