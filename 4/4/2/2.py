import os

ROOT = 'os_task'
path = os.path.join(os.getcwd(), ROOT)

def analyse(path, to_fill):

	os.chdir(path)

	content = os.listdir(path)
	# get files
	files = [f for f in content if os.path.isfile(f)]
	# get dirs
	dirs = [elem for elem in content if elem not in files]


	for temp_dir in dirs:
		to_fill.append({temp_dir: []})
		if analyse(os.path.join(path, temp_dir), to_fill[-1][temp_dir]) == -1:
			to_fill[-1][temp_dir] = None
		# back to origin
		os.chdir(path)

	for file in files:
		to_fill.append(file)

	if to_fill == []:
		return -1


if __name__ == '__main__':
	dict_to_fill = {
		ROOT: []
	}
	analyse(path, dict_to_fill[ROOT])
	print(dict_to_fill)