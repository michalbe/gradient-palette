import random

def to_hex(rgb):
	return '#' + ''.join('%02x'%i for i in rgb).upper()

def random_color():
	r = lambda: random.randint(0,255)
	return (r(), r(), r())


def gradient(start, end, steps):
	diff_r = (end[0] - start[0]) / steps
	diff_g = (end[1] - start[1]) / steps
	diff_b = (end[2] - start[2]) / steps
	for x in range(0, steps):
		print(x)


gradient(random_color(), random_color(), 5)
