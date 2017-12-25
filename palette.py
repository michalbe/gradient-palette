import random

size = 5;

def to_hex(rgb):
	return '#' + ''.join('%02x'%i for i in rgb).upper()

def random_color():
	r = lambda: random.randint(0,255)
	return [r(), r(), r()]

def gradient(start, end, steps):
	diff_r = int((end[0] - start[0]) / steps)
	diff_g = int((end[1] - start[1]) / steps)
	diff_b = int((end[2] - start[2]) / steps)

	colors = list()
	colors.append(start)
	for i in range(1, steps - 1):
		color = list()
		color.append(start[0] + i * diff_r)
		color.append(start[1] + i * diff_g)
		color.append(start[2] + i * diff_b)
		colors.append(color)
	colors.append(end)
	return colors

c00 = random_color()
c10 = random_color()
c01 = random_color()
c11 = random_color()

output = list()
first_row = gradient(c00, c10, size)
last_row = gradient(c01, c11, size)

for i in range(0, size):
	top_color = first_row[i]
	bottom_color = last_row[i]
	output.append(gradient(top_color, bottom_color, size))


print(output)
