import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance

import networkx as nx

def similarity(a,b,stopwords):
	
	a=[word.lower() for word in a]
	b=[word.lower() for word in b]
	words=list(set(a+b))
	x=len(words)
	v1=[0]*x
	v2=[0]*x
	
	for word in a:
		if word in stopwords:
			continue
		v1[words.index(word)] += 1
	
	for word in b:
		if word in stopwords:
			continue
		v2[words.index(word)] += 1

	return 1-cosine_distance(v1,v2)


def Similaritymatrix(content,stop_words):
	size=len(content)
	matrix=np.zeros((size,size))

	for i in range(size):
		for j in range(size):
			if i==j:
				continue
			matrix[i][j]=similarity(content[i],content[j],stop_words)
	
	return matrix


class summarize():
	def __init__(self) :
		pass

	def generate(file,n):
		stop_words=stopwords.words('english')
		summarize_text=[]

		f=open(file,"r")
		data = f.readlines()
		res=data[0].split(".")
		content=[]
		for x in res:
			content.append(x.replace("[^a-zA-Z]"," ").split(" "))
		content.pop()

		matrix=Similaritymatrix(content, stop_words)
		graph=nx.from_numpy_array(matrix)
		scores=nx.pagerank(graph)
		ranking=sorted(((scores[i],s)for i,s in enumerate(content)),reverse=True)
		
		for i in range(n):
			summarize_text.append(" ".join(ranking[i][1]))

		res=". ".join(summarize_text)
		return res

