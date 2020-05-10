import os

BASE_DIR = os.getcwd()

subjects1 = ['что-то', 'еще что-то']
subjects2 = ['что-то2', 'еще что-то2']

def create(subjects1: list, subjects2: list):
	dir1 = {
		'path': os.path.join(BASE_DIR, 'СЕМЕСТР 1'),
		'subjects': subjects1
	}
	dir2 = {
		'path': os.path.join(BASE_DIR, 'СЕМЕСТР 2'),
		'subjects': subjects2
	}

	dirs = [dir1, dir2]

	for temp_dir in dirs:
		if not os.path.exists(temp_dir['path']):
			os.mkdir(temp_dir['path'])
		os.chdir(temp_dir['path'])

		study_dir_path = os.path.join(temp_dir['path'], 'УЧЕБА')
		if not os.path.exists(study_dir_path):
			os.mkdir(study_dir_path)
		os.chdir(study_dir_path)

		for subject in temp_dir['subjects']:
			subject_path = os.path.join(study_dir_path, subject)
			os.mkdir(subject_path)
			os.chdir(subject_path)
			with open('subject_text.txt', 'w') as f:
				f.write(os.getcwd())
			# go up
			path_parent = os.path.dirname(os.getcwd())
			os.chdir(path_parent)
	return

if __name__ == '__main__':
	create(subjects1, subjects2)