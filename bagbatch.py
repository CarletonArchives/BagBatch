"""
	bagbatch.py
	Written to run BagIt on multiple directories at once.
	
	BagBatch Version 1.1.4
	Updated September 10, 2014  

	Usage:	python bagbatch.py <command> <dir>
			<command> is the command used on the directory's subdirectories.
				If no command is specified, 'baginplace' is used.
			<dir> is the parent of the subdirectories to run the command on
				If no directory is specified, program will prompt for one.
			BAGIT_INST_PATH.txt will contain the installation path to bag.bat/bag.sh

	Input:		Parent directory with subdirectories to bag, verifyvalid, or
				update.
	Output:		Parent directory with bagged subdirectories.
	Dependency: BAGIT_INST_PATH.txt
		The first time bagbatch.py is run, it will create BAGIT_INST_PATH.txt 
		and prompt for the path of the BagIt installation. Within this folder, 
		there will be a folder named 'bin' containing bag.bat or bag.sh. This 
		path may be "/Applications/bagit-X.X" or "C:\Program Files\bagit-X.X.X". 
		The path will be saved in BAGIT_INST_PATH.txt. Each time bagbatch.py is 
		run, it will validate this location. 
"""

import os, sys, platform
import shlex, subprocess
from tkFileDialog import askopenfilename
import tkFileDialog, Tkinter

VERSION = '1.1.4'
BAGIT_INST_PATH = "BAGIT_INST_PATH.txt"
BAGBATCH_DIR = os.getcwd()

def call_bag_command(directory, command):
	""" Given a single directory, calls bag <command> <dir> using 
	subprocess.check_call() for Windows and subprocess.Popen() for Mac. Errors  
	will be printed out. """
	print '----------------------\n',command + ':', os.path.normpath(directory) + "."	
	with open(BAGIT_INST_PATH) as bb_path:
		path = bb_path.read()

	os.chdir(path)
	try:
		if get_ext() == '.bat':
			subprocess.check_call([os.path.join(path, 'bag'), command, directory], shell=True)
			return True
		elif get_ext() == '.sh':
			p = subprocess.Popen(['./bag', command, directory])
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
		print "Error:", command, "was not successful. Look in the readme for troubleshooting."
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
	""" Validates the path to BagIt installation folder containing bin/bag.bat
	or bin/bag.sh. Prompts for a new path and resets old path if needed. """
	print "\nValidating BagIt installation path..."
	# Creates the text file with the bagit path, if need be
	if not os.path.isfile(BAGIT_INST_PATH):
		bb_file = open(BAGIT_INST_PATH, "w")
		bb_file.close()

	# closes file after with statement
	with open(BAGIT_INST_PATH, "r+") as bb_path:
		path = bb_path.read()
	
	# if the path exists and the files are present, return and start bagging
	path = os.path.normpath(path)
	if path and os.path.exists(path) and not path == '':
		if not 'bin' in path:
			path = os.path.join(path,'bin')
		if os.path.isfile(os.path.join(path,'bag')):
			print "Validated.\n"
			return
		else:
			print 'cannot find extension'

	# if not, prompt for new path, write to BAGIT_INST_PATH.txt, and validate
	message = '\nSelect the BagIt installation folder. This folder may be located in Applications (Mac) or Program Files (Windows). This will resemble bagit-X.X.X where \'X.X.X\' is the version number.'
	path = select_folder(message)
	# if there are extra quoting characters, remove them
	if '"' in path or "'" in path:
		path=''.join(shlex.split(path))
	try:
		path_bin = path + '/bin'
		if not os.path.isfile(path_bin):
			print 'not a valid folder'
	except:
		print 'no bin path'
	bb_file = open(BAGIT_INST_PATH, "w")
	bb_file.write(path_bin.strip())
	bb_file.close()
	validate_bagit_path()

def select_folder(message):
	print message
	root = Tkinter.Tk()
	root.withdraw()
	result = tkFileDialog.askdirectory(parent = root, title = message)
	if not result:
		print '\nExiting bagbatch.py'
		sys.exit()
	return result

def get_ext():
	""" Based on the operation system, returns the correct file extension for. """
	if 'Windows' in platform.system() or 'win32' == sys.platform:
		return '.bat'
	else:
		return '.sh'

def valid_commands():
	return {'baginplace':'Creates a bag-in-place. The source must be a directory on a filesystem and may already have a data directory.',
	'update':'Updates the manifests and (if it exists) the bag-info.txt for a bag.',
	'verifyvalid':'Verifies the validity of a bag.'}

def usage_message():
	print "BagBatch Version",VERSION
	print "Usage:\tpython bagbatch.py <command>"
	print "\tOr:\tpython bagbatch.py <command> <dir>"
	print "\t\t<dir> is the parent dir of the subdirectories"
	print "\tBAGIT_INST_PATH.txt will contain the installation path: bagit-X.X.X"
	print "Valid Commands:"
	for cmd in valid_commands():
		print '\t' + cmd + ': \t' + valid_commands()[cmd]

def main():
	command = 'baginplace'
	if len(sys.argv) == 1:
		return usage_message()
	if len(sys.argv) == 2:
		if sys.argv[1] == 'help' or sys.argv[1] == 'version':
			return usage_message()
		elif not sys.argv[1] in valid_commands():
			print "\nInvalid command given. Using",command,"instead."
		elif sys.argv[1] in valid_commands():
			command = sys.argv[1]
		if os.path.exists(sys.argv[1]):
			dirToBag = sys.argv[1]
		else:
			dirToBag = select_folder('Select the parent folder containing the folders to %s.' %command)
	elif len(sys.argv) == 3:
		if sys.argv[1] in valid_commands():
			command = sys.argv[1]
		if os.path.exists(sys.argv[2]):
			dirToBag = sys.argv[2]
		else:
			print "\nInvalid folder path. Please select the correct folder."
			dirToBag = select_folder('Select the parent folder containing the folders to %s.' %command)						

	validate_bagit_path()
	dirToBag = os.path.normpath(dirToBag)

	print "----------------------\nRunning",command,"for all directories in", 
	print dirToBag + ".\n----------------------"
	success = True
	for d in get_immediate_subdirectories(dirToBag):
		# calls 'bag <dir> <command>' for each directory
		if not call_bag_command(d, command):
			success = False
		os.chdir(BAGBATCH_DIR)
	if success:
		print "\n----------------------\n----------------------\nBags Complete.\n----------------------"
	else:
		print "----------------------\n----------------------\nBags not complete: Error with bags.\n----------------------"
main()