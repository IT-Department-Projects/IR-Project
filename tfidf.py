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


###Term Frequency###
def term_frequency(documents,vocabulary_list):
	TF=[]
	for document in documents:
		tf_per_document=[]
		for word in vocabulary_list:
			fij=document.count(word)
			if fij>0:
				tf=1+math.log(fij,2)
			else:
				tf=0
			tf_per_document.append(tf)
		TF.append(tf_per_document)

	return TF


###Inverse Document Frequency###
def inverse_document_frequency(documents,vocabulary_list):
	IDF=[]
	N=len(documents)
	for word in vocabulary_list:
		count=0
		for document in documents:
			if word in document:
				count+=1
		if count == 0:
			idf=0
		else:
			idf=math.log(N/count,2)
		IDF.append(idf)
	return IDF


###Term Frequency Inverse Document Frequency###
def term_frequency_inverse_document_frequency(TF,IDF):
	IDF=np.array(IDF)
	TFIDF=[]
	for tf in TF:
		tf=np.array(tf)
		tfidf=tf*IDF
		TFIDF.append(tfidf.tolist())
	return TFIDF


###Accessing the Vocabulary###
file_path='vocabulary.txt'
f1 = open(file_path, 'r')
vocabulary_list=f1.read()
vocabulary_list = ast.literal_eval(vocabulary_list)
f1.close()

###Accessing the Documents###
file_path='documents.txt'
f1 = open(file_path, 'r')
documents=f1.read()
documents = ast.literal_eval(documents)
f1.close()


###Input Query###
query=sys.argv[1]
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

###(iii)###
query=[token for token in query if token.isalpha()]

###(iv)###
query=[token for token in query if len(token)>1]

###Stopword Removal###
stop_words = set(stopwords.words('english'))
query=[token for token in query if not token in stop_words]


def term_frequency_query(documents,query,vocabulary_list):
	TF=[]
	for word in vocabulary_list:
		fij=query.count(word)
		if fij>0:
			tf=1+math.log(fij,2)
		else:
			tf=0
		TF.append(tf)

	return TF

def inverse_document_frequency_query(documents,query,vocabulary_list):
	IDF=[]
	N=len(documents)
	print(N)
	for word in vocabulary_list:
		if word in query:
			idf=math.log(N,2)
		else:
			idf=0
		IDF.append(idf)
	return IDF

def term_frequency_inverse_document_frequency_query(TF,IDF):
	TFIDF=np.multiply(TF,IDF)
	TFIDF=TFIDF.tolist()
	return TFIDF


###Performing TFIDF###
TF=term_frequency(documents,vocabulary_list)
IDF=inverse_document_frequency(documents,vocabulary_list)
TFIDF=term_frequency_inverse_document_frequency(TF,IDF)



###Performing TFIDF for Query###
TF_query=term_frequency_query(documents,query,vocabulary_list)
TFIDF_query=term_frequency_inverse_document_frequency_query(TF_query,IDF)



###Generating CSV###
file_path='tfidf.csv'
with open(file_path, 'w') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(vocabulary_list)
	
	for tfidf in TFIDF:
		wr.writerow(tfidf)
	wr.writerow(TFIDF_query)

