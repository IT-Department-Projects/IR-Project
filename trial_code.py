import nltk
from nltk.corpus import stopwords,state_union,wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
ps=PorterStemmer()
syns=wordnet.synsets("program")





def performPreprocessing(query):
	token_list=word_tokenize(query)
	token_list=Stopword_removal(token_list)
	token_list=Stemming(token_list)
	#token_list=POS_Tagging(token_list)
	#chunked=Chunking(token_list)
	#named_entity=NER(token_list)
	token_list=Lemmatizing(token_list)
	return token_list



###Step1-Tokenize###
def Tokenize(query):
	token_list=word_tokenize(query)
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

###Step4-Parts Of Speech Tagging###
def POS_Tagging(token_list):
	token_list=nltk.pos_tag(token_list)
	return token_list


###Step5-Chunking&Chinking###
def Chunking(token_list):
	chunkGram=r"""Chunk: {<.*>+}
							}<VB.?|IN|DT|TO>+{"""
	chunkParser=nltk.RegexpParser(chunkGram)
	chunked=chunkParser.parse(token_list)
	return chunked

###Step6-Named Entity Recognition###
def NER(token_list):
	named_entity=nltk.ne_chunk(token_list,binary=True)
	return named_entity


###Step7-Lemmatizing###
def Lemmatizing(token_list):
	for i in range(len(token_list)):
		token_list[i]=lemmatizer.lemmatize(token_list[i])
	return token_list


query=state_union.raw('2005-GWBush.txt')
#result=performPreprocessing(query)
#print(result)

print(syns)