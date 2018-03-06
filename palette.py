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
	diff_r = ((end[0] - start[0]) / steps)
	diff_g = ((end[1] - start[1]) / steps)
	diff_b = ((end[2] - start[2]) / steps)

	colors = list()
	colors.append(tuple(start))
	for i in range(1, steps - 1):
		color = list()
		color.append(int(start[0] + i * diff_r))
		color.append(int(start[1] + i * diff_g))
		color.append(int(start[2] + i * diff_b))
		colors.append(tuple(color))
	colors.append(tuple(end))
	return tuple(colors)

upleft = random_color()
downleft = random_color()
upright = random_color()
downright = random_color()

output = tuple()
first_row = gradient(upleft, downleft, size)
last_row = gradient(upright, downright, size)

for i in range(0, size):
	top_color = first_row[i]
	bottom_color = last_row[i]
	output = output + gradient(top_color, bottom_color, size)
	
imgname = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
im = Image.new('RGB', (size, size))
im.putdata(tuple(output))
im = im.resize((final_scale, final_scale))
im.save('images/' + imgname + '.png')
print('Saved as: ' + imgname + '.png')
