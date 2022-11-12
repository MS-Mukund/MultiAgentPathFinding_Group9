import random

def make_input(input_file, output_file,n):
	with open(output_file, 'w') as outfile:
		with open('./Dragon_Age_Origins/Maps/'+input_file+'.map', 'r') as f:
			line = f.readline()
			height = f.readline()
			width = f.readline()
			height = height.split(' ')
			height = int(height[1])
			width = width.split(' ')
			width = int(width[1])
			line = f.readline()
			row = height-1
			outfile.write("agents:\n")
			matrix = []
			for line in f:
				matrix.append(line[:-1])
			count = 0
			while count < n:
				x1 = random.randint(0,width-1)
				x2 = random.randint(0,width-1)
				y1 = random.randint(0,height-1)
				y2 = random.randint(0,height-1)
				if matrix[y1][x1] == '.' and matrix[y2][x2] == '.':
					outfile.write("-  start: [{}, {}]\n".format(x1, y1))
					outfile.write("   goal: [{}, {}]\n".format(x2, y2))
					outfile.write("   name: agent{}\n".format(count))
					count += 1
			outfile.write("map:\n")
			outfile.write("   dimensions: [{}, {}]\n".format(width, height))
			outfile.write("   obstacles:\n")
			for line in matrix:
				col = 0
				for char in line:
					if char != '.':
						outfile.write("   - !!python/tuple [{}, {}]\n".format(col, row))
					col += 1
				row -= 1
			f.close()
		outfile.close()
