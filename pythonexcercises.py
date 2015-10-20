# python learning exercises

#Functions
def echo(thing):
	return thing
	

def swap(thing1,thing2):
	return thing2, thing1
	

		
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): " , echo(' no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')
	
	
#Arithmetic Functions
def reverse(x):
	return	-x

def plus(a,b):
	return a+b
	
def diff(y,z):
	return z-y	
	
def abs_diff(abc,xyz):
	return abc*xyz	
	
def main_arithmetic():
	print "testing reverse(3)", reverse (3)	
	print "test reverse(-3)", reverse (-3)
	print "test plus(12,5)", plus (12,5)
	print "testing diff(3,10)", diff(3,10)
	print "testing abs_diff(4,3)", abs_diff(4,3)
	
	
def main():
	main_function()
	main_arithmetic()
main()