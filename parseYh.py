#!/usr/bin/env python

import json
#!/usr/bin/env python

import json
import re

nodes = list()
edges = list()
parseNodes = False
parseEdges = False

out = open("output.json", 'w')

#populate list of nodes and list of edges
with open("out.txt", 'r') as f:
	for line in f:
		if(not line.isspace()  and not '__main__' in line):
			if('// Nodes' in line):
				parseNodes = True
				continue
			elif('// Edges' in line):
				parseNodes = False
				parseEdges = True
				continue
			if(parseNodes):
				s = line.split()
				nodes.append((s[0], s[8]))
			elif(parseEdges):
				if('}' not in line):
					s = line.split()
					edges.append((s[0], s[2], s[8]))

#strip quotation marks
for i in range(0, len(nodes)):
	node1 = nodes[i][0]
	node2 = nodes[i][1]
	node1 = node1.replace('"', "")
	node2 = node2.replace('"', "")
	node2 = node2.strip('s];')
	nodes[i] = ((node1, node2))

for i in range(0, len(edges)):
	edge1 = edges[i][0]
	edge2 = edges[i][1]
	edge3 = edges[i][2]
	edge1 = edge1.strip('"')
	edge2 = edge2.strip('"')
	edge3 = edge3.strip('"[];')
	edges[i] = ((edge1, edge2, edge3))

#build tree
tree =  list()

#find root
maxlist = list()
for (x,y) in nodes:
	maxlist.append(y)
maxval = max(maxlist)

#find root
for(x, y) in nodes:
	if(y == maxval):
		root = x
	
tree = {"name":root, "size":maxval, "children":[]}


def main():
	tree["children"] = buildTree(tree)
	out.write(json.dumps(tree, indent=2))
	
def match(matchVal):
	matches = []
	for (e1, e2, calls) in edges:
		if (e1 == matchVal):
			matches.append((e2,calls, getSize(e1,e2)))		
			edges.remove((e1,e2,calls))	
	return matches
	
def getSize(caller, callee):
	size = ""
	tCalls = 0
	callerCalls = 0
	#calculate times called 
	for (e1, e2, calls) in edges:
		#print ("e1 ", e1, "e2 ", e2)
		if e2 == callee:
			if (e1 == caller):
				callerCalls = calls
			tCalls += int(calls)
	print ("tcalls ", tCalls)
	for (n, s) in nodes:
		if (n == callee):
			size = s
	iSize = (float(size)/tCalls/10)
	return str((float(iSize)*1000000))
	
	 

def buildTree(root):
	#totChildrenSize = 0
	n = root["name"]
	s = root["size"]
	matches = match(n)
	if (matches == []):
		return None
	elif (matches != []):
		#print ("Matches are ", matches)
		newChildren = []
		for (m, calls,size) in matches:		
			for x in range(0, int(calls)):
				newChild = {}
				newChild["name"] = m
				newChild["size"] = size
				temp = buildTree(newChild)
				if temp != None:
					newChild["children"] = temp
				newChildren.append(newChild)
		newLeaf = {}
		newLeaf["name"] = ""
		newLeaf["size"] = str(float(s))
		newChildren.append(newLeaf)
		return newChildren


if __name__ == "__main__":
	(main())
		
