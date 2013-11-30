#!/usr/bin/env python
import sys
import subprocess

#The responsibility of this class is to grab the data from stdout
#and put it into a text file to be parsed 

class HandlePy:
	def main(self):
		with open('out.txt', 'w') as output:
			pyProgram = str(sys.argv[1])
			sys.stdout = open("out.txt", 'w')
			s = subprocess.Popen(["pycallgraph", "-d", "graphviz", pyProgram], stdout = output)
			s.communicate()
		s1 = subprocess.Popen(["python3.3", "parseYh.py"])
		s2 = subprocess.Popen(["firefox", "yhack.html"])
		s1.communicate()
		s2.communicate()
			
if __name__ == "__main__":
	(HandlePy()).main()
