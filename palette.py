import random

def to_hex(rgb):
	return '#' + ''.join('%02x'%i for i in rgb).upper()

def random_color():
	r = lambda: random.randint(0,255)
	return (r(), r(), r())


def gradient(start, end, steps):
	diff_r = round((end[0] - start[0]) / steps)
	# r_delta = 1 if diff_r > 0 else -1
	diff_g = round((end[1] - start[1]) / steps)
	# g_delta = 1 if diff_g > 0 else -1
	diff_b = round((end[2] - start[2]) / steps)
	# b_delta = 1 if diff_b > 0 else -1

	# print('delty r{0} g{1} b{2}'.format(r_delta, g_delta, b_delta))
	print('r{0} g{1} b{2}'.format(diff_r, diff_g, diff_b))

	colors = list()
	colors.append(to_hex(start))
	for i in range(1, steps - 1):
		color = list()
		color.append(start[0] + i * diff_r)
		color.append(start[1] + i * diff_g)
		color.append(start[2] + i * diff_b)
		print(color)
		colors.append(to_hex(color))
	colors.append(to_hex(end))
	return colors

first = random_color()
second = random_color()

print(first)
print(second)
print(gradient(first, second, 5))
