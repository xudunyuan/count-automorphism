from graph import *
from graph_io import *
TOTALCOLOR = {}
TOTALDEGREE = 0

def mainFunc():
	with open('test.txt') as f:
		G = load_graph(f)
	# with open('mygraph.dot', 'w') as f:
	# 	write_dot(G, f)
	#print(G)
	# v = G.vertices[0]
	#print(G.vertices)

	#for i in G.vertices:
		#print(i,i.degree)

	print("max degree is : ", FindMaxDegree(G.vertices))
	print("we need %d colors in total."%FindColorNumbers(G.vertices))
	#print(G.vertices[len(G.vertices)-1].degree)
	AssginColor1Round(G.vertices)
	print(TOTALCOLOR)
	with open('mygraph.dot', 'w') as f:
		write_dot(G, f)


def FindMaxDegree(AllVertice): # input a list contains all vertices in this graph, return the max degree among these vertices
	Max = 0
	for i in AllVertice:
		#print(i)
		if i.degree > Max:
			Max = i.degree
			#print(Max, ",", i)
	return Max

def FindColorNumbers(AllVertice):# input a list contains all vertices in this graph, return the total colors we are going to use in this graph
	NumOfColors = 0
	emptyList = []
	for i in AllVertice:
		if i.degree not in  emptyList:
			NumOfColors+=1
			emptyList.append(i.degree)
	index = 0
	print(NumOfColors)
	for i in range(0, NumOfColors):
		color_list = []
		for j in range(NumOfColors[i]):
			color_list.append('1')
		TOTALCOLOR['%s'%index] = color_list
	return NumOfColors

def AssginColor1Round(AllVertice): # this is the first round to assign color to each vertice
	#simple assign color according to their degrees
	for i in range(AllVertice):

		#if

		return 
mainFunc()
