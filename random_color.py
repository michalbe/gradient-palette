import random

def to_hex(rgb):
	print(rgb)
	return '#' + ''.join('%02x'%i for i in rgb).upper()

def random_color():
	r = lambda: random.randint(0,255)
	return (r(), r(), r())


def gradient(start, end, steps):
	diff_r = int((end[0] - start[0]) / steps)
	print(diff_r)
	r_delta = 1 if diff_r > 0 else -1
	diff_g = int((end[1] - start[1]) / steps)
	g_delta = 1 if diff_g > 0 else -1
	diff_b = int((end[2] - start[2]) / steps)
	b_delta = 1 if diff_b > 0 else -1

	colors = list();
	for i in range(1, steps - 1):
		color = list()
		color.append(r_delta * i * diff_r + start[0])
		color.append(g_delta * i * diff_g + start[1])
		color.append(b_delta * i * diff_b + start[2])
		colors.append(to_hex(color))
	return colors

first = random_color()
second = random_color()

print(first)
print(second)
print(gradient(first, second, 5))
