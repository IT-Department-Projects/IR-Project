import nltk
from nltk.corpus import stopwords,state_union
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
ps=PorterStemmer()



###Step1-Tokenize###
def Tokenize(query):
	token_list=word_tokenize(query)
	token_list=Stopword_removal(token_list)
	token_list=Stemming(token_list)
	token_list=POS_Removal(token_list)
	return token_list


###Step2-Stopword Removal###
def Stopword_removal(token_list):
	stop_words = set(stopwords.words('english'))
	token_list=[token for token in token_list if token not in stop_words]
	return token_list

###Step3-Stemming###
def Stemming(token_list):
	for i in range(len(token_list)):
		token_list[i]=ps.stem(token_list[i])
	return token_list

###Step4-Parts Of Speech Removal###
def POS_Removal(token_list):
	token_list=nltk.pos_tag(token_list)
	return token_list





query=state_union.raw('2005-GWBush.txt')
result=Tokenize(query)
print(result)