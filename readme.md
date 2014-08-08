BagIt batch processing in Python
================================

bagbatch.py
    Written to run BagIt on multiple directories at once.
    August 2014


BagIt and bagbatch.py
---------------------
BagIt is a Java-based program that creates archival bags of files following 
the BagIt standard developed by the Library of Congress. It is used to store a 
directory's master copies, web copies, and metadeta or to verify that files 
have been transfered from one computer to another properly. By default, BagIt 
only processes one directory at a time. bagbatch.py was written to process an 
entire parent directory with folders ready for bagging on both Mac and Windows.



Requirements and setup
----------------------
 - BagIt
 - Java
 - Python 2.7

[Carlpedia - BagIt](https://wiki.carleton.edu/display/carl/BagIt) has steps on setting 
up Java and BagIt.


#### BAGIT

BagIt can be downloaded from the [Library of Congress on GitHub](https://github.com/LibraryOfCongress/bagit-java). Adapted from the readme file for BagIt 4.9.0 (see the link above for the most recent information):
   |  Unzip bagit-java-master. From this new folder, unzip bagit-x.x.x-src.zip.
   |  In the resulting 'bagit-x.x.x/bin' subdirectory, you will find bag.sh 
   |  (Mac) and bag.bat (Windows) scripts that are used to invoke the 
   |  commandline interface.

#### JAVA

Java must be installed and the Java runtime environment (JAVA_HOME) must be 
set up correctly for BagIt. To check if Java is installed, type "java -version"
(without the quotes) in the terminal (Mac) or command prompt (Windows). If 
Java is not installed, download it from java.com. 

#### PYTHON

Python must be installed to run bagbatch.py. Enter "python" into the terminal 
or command prompt to see if Python is setup for terminal/command line use. If 
not, make sure Python is installed (if it isn't, download version 2.7 from 
python.org). [Python documentation for setting up the interpreter](https://docs.python.org/2.7/tutorial/index.html)



Using bagbatch.py
-----------------
#### OVERVIEW

1. Using the terminal or command prompt, navigate to the directory containing 
bagbatch.py
2. Enter "python bagbatch.py <dir>" where <dir> is the parent directory 
containing the subdirectories to be bagged


#### DETAILED INSTRUCTIONS

1. Open the [terminal](http://www.westwind.com/reference/os-x/commandline/navigation.html) or [command prompt](http://ss64.com/nt/cd.html) and navigate to the directory containing bagbatch.py. For example, if it's in a folder on the desktop, enter "cd Desktop/folder".
2. Enter (without the quotes) "python bagbatch.py <dir>". <dir> is the 
directory that contains all the subdirectories that need to be bagged. Type 
the path in or drag-and-drop the folder from the Finder/Explorer menu. Press 
enter and the current status will be printed to the screen. If prompted for 
the directory containing bag.sh (Mac) or bag.bat (Windows), enter the 
installation directory. This end of this folder name will look like 
"\bagit-VERSION\bin". Depending on the size of the files, it may take a while 
to bag. The program is done once "Bags complete" is printed.



Changing the BagIt installation path used by bagbatch.py 
--------------------------------------------------------
#### OVERVIEW

 - Option 1: Delete BAGIT_INST_PATH.txt and run bagbatch.py. Enter the 
 location of the new installation.
 - Option 2: Manually edit BAGIT_INST_PATH.txt to the location of the new 
 installation


#### DETAILED INSTRUCTIONS

BAGIT_INST_PATH.txt contains the path to BagIt's bag installation. This path 
will look similar to "C:/Program Files/bagit-VERSION/bin" or "/Program Files/
Archival/bagit-4.9.0/bin". Do NOT use ".../src/assembly/bin", use 
".../bagit-x.x.x-bin/bagit-x.x.x/bin" instead. Each time bagbatch.py runs, it 
will validate this path, checking to see that the directory and bag.sh (Mac) 
or bag.bat (Windows) exists. If the directory does not exists or it does not 
contain bag.sh or bag.bat, it will prompt for the correct path. If a new 
version of BagIt is installed and the old version is not removed, 
BAGIT_INST_PATH.txt must be manually edited. Either delete the file and run 
bagbatch.py and let it prompt for the installation directory, entering the new 
installation this time, or enter in the path to the new installation.
