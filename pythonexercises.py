# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Functions
def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = d - b
	if diff < 0:
		diff *= -1
	return diff
	
def divide(w, p):
	return w / float(p)
	
def remainder(w, p):
	return w % p
	
def power(x, e):
	answer = 1
	for i in range(e):
		answer *= x
	return answer

def calculate(a, b, c, d, e):
	return (a + b /d -e) * c

def ratio(al, fred):
	if  al > fred:
		return al / fred
	else: 
		return fred / al
	
def pythagoras(a, b):
	return (a**2 + b**2)**(.5)

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff(10, 5): ", abs_diff (10, 5)
	print "test abs_diff(5,10): ", abs_diff (5, 10)
	print "test divide(10, 2): ", divide (10, 2)
	print "test divide(2, 10): ", divide (2, 10)
	print "test remainder(40, 19): ", remainder (40, 19)
	print "test remainder(126, 19): ", remainder (126, 19)
	print "test remainder(133, 19): ", remainder (133, 19)
	print "test power(2, 3): ", power (2, 3)
	print "test calculate (1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "test ratio(3.2, 7.8): ", ratio(3.2, 7.8)
	print "test pythagoras(3, 4): ", pythagoras(3, 4)
	print "test pythagoras(35, 67): ", pythagoras(35, 67)
	
def reverse(zack):
	return not zack
	
def band(a, b):
	return a and b
	
def bor(a, b):
	return a or b

def xsame(b, g):
	return b == g
	
def xor(a, b):
	return a == b
	

	
def main_boolean():
	print "test reverse(True): ", reverse(True)
	print "test reverse(False): ", reverse(False)
	print "test reverse(1): ", reverse(1)
	print "test reverse(0): ", reverse(0)
	print "test band(True,True): ", band(True, True)
	print "test band(True,False): ", band(True, False)
	print "test band(False,False): ", band(False, False)
	print "test bor(True, True): ", bor(True, True)
	print "test bor(True, False): ", bor(True, False)
	print "test bor(False, False): ", bor(False, False)
	print "test xsame(True, True): ", xsame(True, True)
	print "test xsame(True, False): ", xsame(True, False)
	print "test xsame(False, False): ", xsame(False, False)
	print "test xor(True, True): ", xor(True, True)
	print "test xor(True, False): ", xor(True, False)
	print "test xor(False, False): ", xor(False, False)
	
def positive(n):
	return n > 0
		

def bigger(r, p):
	return r > p
		
		
def no_diff(w, h):
	return w == h
	
def no_same(b, g):
	return not b == g

def less_than(r, p):
	return r < p
	
def at_least_13(d):
	return d >= 13
		
def main_boolean_numbers():
	print "test positive(29): ", positive(29)
	print "test positive(-29): ", positive(-29)
	print "test bigger(200, 10): ", bigger(200, 10)
	print "test bigger (10, 200: ", bigger (10, 200)
	print "test no_diff(99, 99): ", no_diff(99,99)
	print "test no-diff(67, 76): ", no_diff(67, 76)
	print "test no_same(99, 99): ", no_same(99,99)
	print "test no-same(67, 76): ", no_same(67, 76)
	print "test less_than(2, 8): ", less_than(2, 8)
	print "test less_than(8, 2): ", less_than(8, 2)
	print "test at_least_13(45): ", at_least_13(45)
	print "test at_least_13(13): ", at_least_13(13)
	print "test at_least_13(11): ", at_least_13(11)

def main():
	main_function()
	main_arithmetic()
	main_boolean()
	main_boolean_numbers()
	
main()