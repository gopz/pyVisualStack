def meth1():
	meth2(0)
	meth3()
	meth4()

def meth2(i):
	if(i == 5):
		return
	else:
		meth2(i+1)

def meth3():
	for i in range(0,10):
		meth4()

def meth4():
	print("meth4!")
	meth5()

def meth5():
	print("hai")

meth1()
