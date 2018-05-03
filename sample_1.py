import sys
import ast
from collections import Counter
from os import listdir
import simplejson
import math
import numpy as np
import csv
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from operator import itemgetter


def term_frequency_query(query,vocabulary_list):
	TF=[]
	for word in vocabulary_list:
		fij=query.count(word)
		if fij>0:
			tf=1+math.log(fij,2)
		else:
			tf=0
		TF.append(tf)

	return TF

def term_frequency_inverse_document_frequency_query(TF,IDF):
	TFIDF=np.multiply(TF,IDF)
	TFIDF=TFIDF.tolist()
	return TFIDF


###Accessing the Vocabulary###
file_path='vocabulary.txt'
f1 = open(file_path, 'r')
vocabulary_list=f1.read()
vocabulary_list = ast.literal_eval(vocabulary_list)
f1.close()

###Accessing IDF###
file_path='idf.txt'
f1 = open(file_path, 'r')
IDF=f1.read()
IDF = ast.literal_eval(IDF)
f1.close()

def get_documents(query):
	###Normalization###
	query=query.lower()
	###Tokenization###
	query=word_tokenize(query)
	###Lemmatization###
	lemmatizer=WordNetLemmatizer()
	for i in range(len(query)):
		query[i]=lemmatizer.lemmatize(query[i])

	###Cleaning###
	###(i) & (ii)###
	translation = str.maketrans("","", string.punctuation);
	for i in range(len(query)):
		query[i]=query[i].translate(translation)

	###(iv)###
	query=[token for token in query if len(token)>1]

	###Stopword Removal###
	stop_words = set(stopwords.words('english'))
	query=[token for token in query if not token in stop_words]

	###Performing TFIDF for Query###
	TF=term_frequency_query(query,vocabulary_list)
	TFIDF=term_frequency_inverse_document_frequency_query(TF,IDF)

	###Generating TFIDF of Query###
	file_path='tfidf.txt'
	f = open(file_path, 'w')
	simplejson.dump(TFIDF, f)
	f.close()

	documents=[]
	file_path='tfidf.csv'
	file=open(file_path, "r")
	reader = csv.reader(file)
	for line in reader:
		documents.append(line)

	###Accessing the TFIDF of Query###
	file_path='tfidf.txt'
	f1 = open(file_path, 'r')
	query=f1.read()
	query = ast.literal_eval(query)
	query=list(map(float, query))
	f1.close()

	del documents[0]
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
		return "Your search did not match any documents."
	else:
		COS_SIM.sort(key=itemgetter(1), reverse=True)
		return COS_SIM[0:11]


answer=get_documents(sys.argv[1])

print(answer)


