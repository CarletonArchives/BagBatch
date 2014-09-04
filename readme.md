BagIt batch processing in Python
================================
Version 1.1.2  
Updated September 4, 2014  

[__BagIt and bagbatch.py__](https://github.com/SahreeK/BagBatch#bagit-and-bagbatchpy)  
[__Requirements and setup__](https://github.com/SahreeK/BagBatch#requirements-and-setup)  
- [BagIt](https://github.com/SahreeK/BagBatch#bagit)  
- [Java](https://github.com/SahreeK/BagBatch#java)  
- - - [Setting up the JAVA HOME environment variable](https://github.com/SahreeK/BagBatch#setting-up-the-java_home-environment-variable)  
- - - - - - - [Windows 7](https://github.com/SahreeK/BagBatch#windows-7)  
- - - - - - - [Mac](https://github.com/SahreeK/BagBatch#mac)  
- [Python](https://github.com/SahreeK/BagBatch#python)  
- - - [Installation Details: Windows 7](https://github.com/SahreeK/BagBatch#installation-details-windows-7)  
- - - [Installation Details: Mac](https://github.com/SahreeK/BagBatch#installation-details-mac)  
- [Opening Command Prompt and Terminal](https://github.com/SahreeK/BagBatch#opening-command-prompt-windows-and-terminal-mac)  
- - - [Windows 7](https://github.com/SahreeK/BagBatch#windows-7-1)  
- - - [Mac](https://github.com/SahreeK/BagBatch#mac-1)  
[__Using bagbatch.py__](https://github.com/SahreeK/BagBatch#using-bagbatchpy)  
- [Overview](https://github.com/SahreeK/BagBatch#overview)  
- [Detailed Instructions](https://github.com/SahreeK/BagBatch#detailed-instructions)  
[__Setting up a new version of Bagit__](https://github.com/SahreeK/BagBatch#setting-up-a-new-version-of-bagit)  
- [Overview](https://github.com/SahreeK/BagBatch#overview-1)  
- [Detailed Instructions](https://github.com/SahreeK/BagBatch#detailed-instructions-1)  
[__Troubleshooting__](https://github.com/SahreeK/BagBatch#troubleshooting)  
- [Java](https://github.com/SahreeK/BagBatch#java-1)  
- [Python](https://github.com/SahreeK/BagBatch#python-1)  
- [BagBatch](https://github.com/SahreeK/BagBatch#bagbatch)  
- [Bagit](https://github.com/SahreeK/BagBatch#bagit-1)  


## BagIt and bagbatch.py
BagIt is a Java-based program that creates archival bags of files following 
the [BagIt standard](https://github.com/LibraryOfCongress/bagit-java) developed by the Library of Congress. It is used to store a 
directory's master copies, web copies, and metadeta or to verify that files 
have been transfered from one computer to another properly. By default, BagIt 
only processes one directory at a time. bagbatch.py was written to process an 
entire parent directory with folders ready for bagging on both Mac and Windows.

## Requirements and setup
 - Windows 7 or Mac OS
 - BagIt
 - Java
 - Python 2.7

Follow the instructions below to setup the above programs. For additional information, check out [Carlpedia - BagIt](https://wiki.carleton.edu/display/carl/BagIt), which has links to tutorials and examples.  

If you have an older or newer version of Windows, the directions below may not apply.

### BagIt

BagIt can be downloaded from the [Library of Congress on GitHub](https://github.com/LibraryOfCongress/bagit-java). Adapted from the readme file for BagIt 4.9.0 (see the link above for the most recent information):

 - Unzip bagit-java-master. From this new folder, unzip bagit-x.x.x-src.zip. In the resulting 'bagit-x.x.x/bin' subdirectory, you will find bag.sh (Mac) and bag.bat (Windows) scripts that are used to invoke the command line interface.

### Java

Java 6 or 7 must be installed. To check if Java is installed, type `java -version` 
in [Terminal (Mac) or Command Prompt (Windows)](https://github.com/SahreeK/BagBatch#opening-command-prompt-windows-and-terminal-mac). If 
Java is not installed, download it from [java.com](https://www.java.com/). BagBatch has been tested with Java 7. 

###### Setting up the JAVA_HOME environment variable
The Java runtime environment (JAVA_HOME) must be set up correctly for BagIt to run. Follow the steps for your operating system below.  

###### Windows 7   
1. Click Start/Control Panel. Enter into the search bar 'environment variable' and select *Edit environment variables for your account*. Or, to do it manually: Start/Control Panel/System and Security/System/Advanced system settings/Environment variables.  
2. In the Environment Variables window, under *System variables*, check that a variable named JAVA_HOME exists. If so, the variable is already set up. If not, continue with step 3.  
3. Keeping those windows open, click Start/Control Panel and search for 'Java'. If nothing is found, Java has not been installed correctly. In the Java Control Panel, select the Java tab and then *view*. Under path, copy all but the \bin\javaw.exe part at the end of the path. It should look similar to C:\Program Files\Java\jre7.  
4. Back in the Environment Variables window, create a new system variable with the name JAVA_HOME and with the copied path as the value. Click Ok 
  
###### Mac
BagIt must already be installed.   

1. Open the terminal by going to Applications/Utilities/Terminal.  
2. Type `nano ~/bagit/bin/bag`, which will open a text editor.  
3. Edit the line `#JAVA_HOME=` to equal the direct path to the version of Java you are running. For example, the line may look like: `#JAVA_HOME=/usr/lib/jvm/java-6-sun`  
4. Edit the line `MAXMEM=512m` and change it to `MAXMEM=2048m`  
5. Hit Control O and Return to save your changes and Control X to exit.  

### Python

Python 2.7 must be installed to run bagbatch.py. Mac OS X, Mavericks and Mountian Lion have Python 2.7 already installed. 
Enter `python` into [Terminal 
or Command Prompt](https://github.com/SahreeK/BagBatch#opening-command-prompt-windows-and-terminal-mac) to see if Python is setup for terminal/command line use. If 
not, make sure Python is installed (if it isn't, download version 2.7 from 
python.org). [Python 2.7 documentation for setting up the interpreter](https://docs.python.org/2.7/tutorial/index.html)

###### Installation Details: Windows 7
Python must be able to run from Command Prompt or Terminal. The Python environment variable must be created, similar to how the JAVA_HOME variable was setup.  

1. Find the installation folder for Python 2.7, which is usually C:\Python27.  
2. Click Start/Control Panel. Enter into the search bar 'environment variable' and select *Edit environment variables for your account*. Or, to do it manually: Start/Control Panel/System and Security/System/Advanced system settings/Environment variables.  
3. In the Environment Variables window, under *System variables*, select the `Path` variable and click Edit.  
4. To the end of the value field, add a semicolon if need be and add `C:\Python27;C:\Python27\Scripts`.

###### Installation Details: Mac
[Getting and installing Python](http://docs.python-guide.org/en/latest/starting/install/osx/)

### Opening Command Prompt (Windows) and Terminal (Mac)
###### Windows 7
Start/All Programs/Accessories/Command Prompt  
To see a list of folders, type `dir` and press enter. This lists all the directories (folders) in the current directory. To navigate to one of those directories, enter `cd FolderName` and use quotes around the folder name if the name contains spaces, such as `cd "Folder Name"`. To navigate backwards, type `cd ..`. [More tutorials](http://ss64.com/nt/cd.html).
  
###### Mac
Applications/Utilities/Terminal  
To see a list of folders, type `ls` and press enter. This lists all the directories (folders) in the current directory. To navigate to one of those directories, enter `cd FolderName` and use quotes around the folder name if the name contains spaces, such as `cd "Folder Name"`. To navigate backwards, type `cd ..`. [More tutorials](http://www.westwind.com/reference/os-x/commandline/navigation.html).


## Using bagbatch.py
##### Overview

1. Using the terminal or command prompt, navigate to the directory containing 
bagbatch.py
2. Enter `python bagbatch.py <command>` or `python bagbatch.py <command> <dir>` where `<dir>` is the parent directory containing the subdirectories to be bagged.  
Commands are as follows:  

 - baginplace: Creates a bag-in-place.  The source must be a directory on a filesystem and may already have a data directory.
 - update: Updates the manifests and (if it exists) the bag-info.txt for a bag.
 - verifyvalid: Verifies the validity of a bag.


##### Detailed Instructions

1. Open [Terminal or Command Prompt](https://github.com/SahreeK/BagBatch#opening-command-prompt-windows-and-terminal-mac) and navigate to the directory containing bagbatch.py. For example, if it's in a folder on the desktop, enter "cd Desktop/folder".  
2. If prompted for the directory containing bag.sh (Mac) or bag.bat (Windows), navigate to the installation directory. This folder name will look like 
`bagit-VERSION`.
3. Enter `python bagbatch.py <command>` using an [accepted command](https://github.com/SahreeK/BagBatch#overview). Press 
enter and the current status will be printed to the screen.  
Or manually enter the directory: Enter `python bagbatch.py <command> <dir>` where `<dir>` is the 
directory that contains all the subdirectories that need to be bagged. Type 
the path in or drag-and-drop the folder from the Finder/Explorer menu. Press enter.

4. Depending on the size of the files, it may take a while 
to bag. The program is done once "Bags complete" is printed.


## Setting up a new version of BagIt
##### Overview
The BagIt installation path used by bagbatch.py must be manually deleted or changed.

 - Option 1: Delete `BAGIT_INST_PATH.txt` and run bagbatch.py. Enter the location of the new installation.
 - Option 2: Manually edit `BAGIT_INST_PATH.txt` to the location of the new installation


##### Detailed Instructions

`BAGIT_INST_PATH.txt` contains the path to BagIt's bag installation. This path 
will look similar to `"C:/Program Files/bagit-VERSION/bin"` or `"/Program Files/
Archival/bagit-4.9.0/bin"`.

 - Do NOT use `".../src/assembly/bin"`. Use `".../bagit-x.x.x-bin/bagit-x.x.x/bin"` instead.

Each time bagbatch.py runs, it 
will validate this path, checking to see that the directory and bag.sh (Mac) 
or bag.bat (Windows) exists. If the directory does not exists or it does not 
contain bag.sh or bag.bat, it will prompt for the correct path.  

If a new 
version of BagIt is installed and the old version is not removed, 
`BAGIT_INST_PATH.txt` must be manually edited. Either delete the file and run 
bagbatch.py and let it prompt for the installation directory, entering the new 
installation this time, or enter in the path to the new installation.


## Troubleshooting
If getting errors in Terminal or Command Prompt such as

    Error occurred during initialization of VM  
    Could not reserve enough space for object heap  
    Error: Could not create the Java Virtual Machine.

Try restarting your computer. If the problem persists, follow these directions ([Mac](https://wiki.carleton.edu/display/carl/Bagit#Bagit-Setting$JAVA_HOMEandincreasingmemory), [Windows](https://wiki.carleton.edu/display/carl/Bagit#Bagit-DownloadandinstallBagit)) to increase the amount of memory Java can access for BagIt.

### Java
 - Is Java (version 6 or 7) installed? BagBatch has been tested with Java 7.
 - Is Java correctly setup for Terminal or Command Prompt usage? Enter `java -version` in Terminal or Command Prompt to check the version. 
 - Is the JAVA_HOME environment variable setup correctly? [Follow these setup instructions](https://github.com/SahreeK/BagBatch#setting-up-the-java_home-environment-variable).  
 - If that does not work, try uninstalling and reinstalling Java, following [Java's download instructions](https://www.java.com/en/).

### Python
 - Is Python 2.7 installed?
 - Is Python correctly setup for Terminal or Command Prompt usage? Enter `python` in Terminal or Command Prompt to check the version. 
 - For Windows, check to see if the Python environment variable is [setup correctly](https://github.com/SahreeK/BagBatch#installation-details-windows-7). 
 - If that does not work, try uninstalling and reinstalling Python 2.7, following [Python's download instructions](https://www.python.org/).

### BagBatch
 - Check your version of BagBatch by entering `python bagbatch.py`.

### BagIt
Download BagIt 4.x.x from the [Library of Congress on GitHub](https://github.com/LibraryOfCongress/bagit-java).  

 - Is BagIt downloaded?
 - Which version of BagIt? BagBatch has been tested with BagIt 4.4 and BagIt 4.9.0.