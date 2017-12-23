import random

def random_color():
	r = lambda: random.randint(0,255)
	return ''.join('%02x'%i for i in (r(), r(), r()))

print(random_color())
