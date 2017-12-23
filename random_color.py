import random

def random_color():
	r = lambda: random.randint(0,255)
	hex = ''.join('%02x'%i for i in (r(), r(), r()))
	return hex;

print(random_color())
