from PIL import Image
import random
import sys

size = int(sys.argv[1]) if len(sys.argv) > 1 else 5
final_scale = int(sys.argv[2]) if len(sys.argv) > 2 else 500

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
	colors.append(tuple(start))
	for i in range(1, steps - 1):
		color = list()
		color.append(start[0] + i * diff_r)
		color.append(start[1] + i * diff_g)
		color.append(start[2] + i * diff_b)
		colors.append(tuple(color))
	colors.append(tuple(end))
	return tuple(colors)

c00 = random_color()
c10 = random_color()
c01 = random_color()
c11 = random_color()

output = tuple()
first_row = gradient(c00, c10, size)
last_row = gradient(c01, c11, size)

for i in range(0, size):
	top_color = first_row[i]
	bottom_color = last_row[i]
	output = output + gradient(top_color, bottom_color, size)

im = Image.new('RGB', (size, size))
im.putdata(tuple(output))
im = im.resize((final_scale, final_scale))
im.save('images/' + ''.join(random.choice('0123456789ABCDEF') for i in range(16)) + '.png')
