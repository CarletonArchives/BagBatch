"""
	bagbatch.py
	Written to run BagIt on multiple directories at once.
	
	BagBatch Version 1.0.1
	Updated August 26 2014  

	Usage:	python bagbatch.py <dir>
			<dir> is the parent of the subdirectories to bag
			BAGIT_INST_PATH.txt will contain the installation path to bag.bat/bag.sh

	Input:		Parent directory with subdirectories to be bagged.
	Output:		Parent directory with bagged subdirectories.
	Dependency: BAGIT_INST_PATH.txt
		The first time bagbatch.py is run, it will create BAGIT_INST_PATH.txt 
		and prompt for the path to bag.bat or bag.sh. This path may be 
		"/Program Files/bagit/bin" or "C:\Program Files\bagit\bin". The path 
		will be saved in BAGIT_INST_PATH.txt. Each time bagbatch.py is run, it 
		will validate this location. 
"""

import os, sys, platform
import shlex, subprocess

VERSION = '1.0.1'
BAGIT_INST_PATH = "BAGIT_INST_PATH.txt"
BAGBATCH_DIR = os.getcwd()

def call_bag_baginplace(directory, timeout = None):
	""" Given a single directory, calls bag baginplace <dir> using 
	subprocess.check_call() for Windows and subprocess.Popen() for Mac. Errors  
	will be printed out. """
	print '----------------------\nBagging', directory + "."	
	with open(BAGIT_INST_PATH) as bb_path:
		path = bb_path.read()

	os.chdir(path)
	try:
		if get_ext() == '.bat':
			subprocess.check_call([os.path.join(path, 'bag'), 'baginplace', directory], shell=True)
			return True
		elif get_ext() == '.sh':
			p = subprocess.Popen(['./bag','baginplace',directory])
			p.wait()
			stdout, stderr = p.communicate()
			# if nothing goes wrong, stdout and stderr = None
			if stdout:
				print stdout
			if stderr:
				print stderr
			return True
		else:
			print 'Error detecting OS'
			return False
		
	except:
		print "Error: Directory not bagged. Make sure BagIt is installed correctly \
		and the directory path listed in", BAGIT_INST_PATH, "contains bag" + get_ext()
		return False


def get_immediate_subdirectories(directory):
	""" Given a directory name, finds all immediate subdirectories and returns
	the complete directory paths in a list. source: 
	http://stackoverflow.com/a/800201 """
	dirNames = [name for name in os.listdir(directory)
	if os.path.isdir(os.path.join(directory, name))]
	dirList = []
	for d in dirNames:
		dirList.append(os.path.join(directory,d))
	return dirList

def validate_bagit_path():
	""" Validates the path to bag.bat/bag.sh and resets it if needed. """
	print "\nValidating BagIt installation path..."
	# Creates the text file with the bagit path, if need be
	if not os.path.isfile(BAGIT_INST_PATH):
		bb_file = open(BAGIT_INST_PATH, "w")
		bb_file.close()

	# closes file after with statement
	with open(BAGIT_INST_PATH, "r+") as bb_path:
		path = bb_path.read()
	
	# if the path exists and the files are present, return and start bagging
	if path and os.path.exists(path):
		if os.path.isfile(os.path.join(path,'bag')):
			print "Validated.\n"
			return
		else:
			print 'cannot find extension'

	# if not, prompt for new path, write to BAGIT_INST_PATH.txt, and validate
	path = str(raw_input('Enter the BagIt installation path containing bag%s (ex: "C:\\Program Files\\bagit-x.x.x\\bin" or "/Program Files/bagit-x.x.x/bin"): '%get_ext())) 
	# if there are extra quoting characters, remove them
	if '"' in path or "'" in path:
		path=''.join(shlex.split(path))
	bb_file = open(BAGIT_INST_PATH, "w")
	bb_file.write(path.strip())
	bb_file.close()
	validate_bagit_path()

def get_ext():
	""" Based on the operation system, returns the correct file extension for. """
	if 'Windows' in platform.system() or 'win32' == sys.platform:
		return '.bat'
	else:
		return '.sh'
	
def usage_message():
	print "BagBatch Version",VERSION
	print "Usage:\tpython bagbatch.py <dir>"
	print "\t<dir> is the parent directory of the subdirectories to bag"
	print "\tBAGIT_INST_PATH.txt will contain the installation path to bag%s" %get_ext()

def main():
	if len(sys.argv) <= 1 or not os.path.exists(sys.argv[1]):
		return usage_message()

	validate_bagit_path()

	dirToBag = sys.argv[1]
	print "----------------------\nCreating bags for all directories in", 
	print dirToBag + ".\n----------------------"
	success = True
	for d in get_immediate_subdirectories(dirToBag):
		# calls 'bag baginplace <dir>' for each directory
		if not call_bag_baginplace(d):
			success = False
		os.chdir(BAGBATCH_DIR)
	if success:
		print "----------------------\n----------------------\nBags Complete.\n----------------------"
	else:
		print "----------------------\n----------------------\nBags not complete: Error with bags.\n----------------------"
main()