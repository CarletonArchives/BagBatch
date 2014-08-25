BagIt batch processing in Python
================================

bagbatch.py  
    Written to run BagIt on multiple directories at once.  
    August 2014  


## BagIt and bagbatch.py
BagIt is a Java-based program that creates archival bags of files following 
the BagIt standard developed by the Library of Congress. It is used to store a 
directory's master copies, web copies, and metadeta or to verify that files 
have been transfered from one computer to another properly. By default, BagIt 
only processes one directory at a time. bagbatch.py was written to process an 
entire parent directory with folders ready for bagging on both Mac and Windows.



## Requirements and setup
 - BagIt
 - Java
 - Python 2.7

[Carlpedia - BagIt](https://wiki.carleton.edu/display/carl/BagIt) has steps on setting 
up Java and BagIt.

##### Opening Command Prompt (Windows) and Terminal (Mac)
###### Windows 7
Start/All Programs/Accessories/Command Prompt  
To see a list of folders, type `dir` and press enter. This lists all the directories (folders) in the current directory. To navigate to one of those directories, enter `cd FolderName` and use quotes around the folder name if the name contains spaces, such as `cd "Folder Name"`. To navigate backwards, type `cd ..`.
  
###### Mac
Applications/Utilities/Terminal  
To see a list of folders, type `ls` and press enter. This lists all the directories (folders) in the current directory. To navigate to one of those directories, enter `cd FolderName` and use quotes around the folder name if the name contains spaces, such as `cd "Folder Name"`. To navigate backwards, type `cd ..`. 

##### BagIt

BagIt can be downloaded from the [Library of Congress on GitHub](https://github.com/LibraryOfCongress/bagit-java). Adapted from the readme file for BagIt 4.9.0 (see the link above for the most recent information):
 * Unzip bagit-java-master. From this new folder, unzip bagit-x.x.x-src.zip. In the resulting 'bagit-x.x.x/bin' subdirectory, you will find bag.sh (Mac) and bag.bat (Windows) scripts that are used to invoke the commandline interface.

##### Java

Java must be installed. To check if Java is installed, type `java -version` 
in the terminal (Mac) or command prompt (Windows). If 
Java is not installed, download it from [java.com](https://www.java.com/). 

###### Setting up the JAVA_HOME environment variable
The Java runtime environment (JAVA_HOME) must be set up correctly for BagIt to run.  
###### Windows 7   
Step 1:  
Click Start/Control Panel. Enter into the search bar 'environment variable' and select *Edit environment variables for your account*. Or, to do it manually: Start/Control Panel/System and Security/System/Advanced system settings/Environment variables.
Step 2:  
In the Environment Variables window, under *System variables*, check that a variable named JAVA_HOME exists. If so, the variable is already set up. If not, continue with step 3.
Step 3:  
Keeping those windows open, click Start/Control Panel and search for 'Java'. If nothing is found, Java has not been installed correctly. In the Java Control Panel, select the Java tab and then *view*. Under path, copy all but the \bin\javaw.exe part at the end of the path. It should look similar to C:\Program Files\Java\jre7.  
Step 4:  
Back in the Environment Variables window, create a new system variable with the name JAVA_HOME and with the copied path as the value.  
  
###### Mac
BagIt must already be installed.
Step 1:  
Open the terminal by going to Applications/Utilities/Terminal.  
Step 2:  
Type nano ~/bagit/bin/bag, which will open a text editor.
Step 3:  
Edit the line #JAVA_HOME= to equal the direct path to the version of Java you are running. For example, the line may look like: #JAVA_HOME=/usr/lib/jvm/java-6-sun  
Step 4:  
Edit the line MAXMEM=512m and change it to MAXMEM=2048m
Step 5:  
Hit Control O and Return to save your changes and Control X to exit.  

##### Python

Python must be installed to run bagbatch.py. Enter `python` into the terminal 
or command prompt to see if Python is setup for terminal/command line use. If 
not, make sure Python is installed (if it isn't, download version 2.7 from 
python.org). [Python documentation for setting up the interpreter](https://docs.python.org/2.7/tutorial/index.html)



## Using bagbatch.py
##### Overview

1. Using the terminal or command prompt, navigate to the directory containing 
bagbatch.py
2. Enter `python bagbatch.py <dir>` where <dir> is the parent directory 
containing the subdirectories to be bagged


##### Detailed Instructions

1. Open the [terminal](http://www.westwind.com/reference/os-x/commandline/navigation.html) or [command prompt](http://ss64.com/nt/cd.html) and navigate to the directory containing bagbatch.py. For example, if it's in a folder on the desktop, enter "cd Desktop/folder".
2. Enter `python bagbatch.py <dir>`. `<dir>` is the 
directory that contains all the subdirectories that need to be bagged. Type 
the path in or drag-and-drop the folder from the Finder/Explorer menu. Press 
enter and the current status will be printed to the screen. If prompted for 
the directory containing bag.sh (Mac) or bag.bat (Windows), enter the 
installation directory. This end of this folder name will look like 
`"\bagit-VERSION\bin"`. Depending on the size of the files, it may take a while 
to bag. The program is done once "Bags complete" is printed.



## Changing the BagIt installation path used by bagbatch.py 
##### Overview

 - Option 1: Delete BAGIT_INST_PATH.txt and run bagbatch.py. Enter the 
 location of the new installation.
 - Option 2: Manually edit BAGIT_INST_PATH.txt to the location of the new 
 installation


##### Detailed Instructions

BAGIT_INST_PATH.txt contains the path to BagIt's bag installation. This path 
will look similar to `"C:/Program Files/bagit-VERSION/bin"` or `"/Program Files/
Archival/bagit-4.9.0/bin"`. 
- Do NOT use `".../src/assembly/bin"`, use `".../bagit-x.x.x-bin/bagit-x.x.x/bin"` instead.  
Each time bagbatch.py runs, it 
will validate this path, checking to see that the directory and bag.sh (Mac) 
or bag.bat (Windows) exists. If the directory does not exists or it does not 
contain bag.sh or bag.bat, it will prompt for the correct path.  

If a new 
version of BagIt is installed and the old version is not removed, 
BAGIT_INST_PATH.txt must be manually edited. Either delete the file and run 
bagbatch.py and let it prompt for the installation directory, entering the new 
installation this time, or enter in the path to the new installation.
