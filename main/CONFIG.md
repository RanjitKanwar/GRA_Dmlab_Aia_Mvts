# Listing of the NRT-HARP-Processor config file lines

## TOC

* [Return to README](./README.md)
* [LOGGING](#markdown-header-logging)
* [RUNTIME](#markdown-header-runtime)

***


## LOGGING

This set of values is for configuration of logging of the process. We must have each of the sub values within the  __
LOGGING__  tag. If they are not present, the configuration will fail. They do not need to be in any particular order
though.

	[LOGGING]
	log_path = /app/log
	log_file = nrt-harp-downloader.log
	log_file_size_bytes = 1048576
	log_backups = 5
	level = DEBUG

### log_path

	log_path = /app/log

This is the location within the container that the process will write the log file. This is provided so it can be set to
a location that is mapped outside the container to a location of the users choosing. Doing such mapping makes the log
file avialable outside of the container.

### log_file

	log_file = nrt-harp-downloader.log

This provides the naming convention for the set of rolling log files. The most current log file will be named as the
provided file name, and the rollover files will be numbered 1 to the number of backup files specified.

### log_file_size_bytes

	log_file_size_bytes = 10485760

This provides how large the log file will be allowed to grow in bytes prior to it being rolledover to a backup file and
a new empty file is started for fresh logging.

### log_backups

	log_backups = 5

This provides how many backup log files to keep after rollover has taken place. Each time a new file is created, the old
files are rolled over up to this number of times before they are simply deleted.

### level

	level = DEBUG

This provides the level of logging to perform. The levels available are  __DEBUG__ ,  __INFO__ , or  __ERROR__ . **
Note**: These are case sensitive! In the  __DEBUG__  mode, the most amount of information is provided, including stack
traces of errors that occur. In the  __INFO__  mode, slightly less information is recoreded, like times of start and
completion of the scheduled processing task but stack traces of errors are not recorded. In the  __ERROR__  mode, the
least amount of information is recorded. In this, only the error information is recorded, this includes what method the
error was captured in and what information the error provided, but no stack trace.

[Return to TOC](#markdown-header-toc)

***

## RUNTIME

This set of values is for configuration of the runtime frequency of the various sub-processes within this process. We
must have each of the sub values within the  __RUNTIME__  tag. If they are not present, the configuration will fail.
They do not need to be in any particular order though.

	[RUNTIME]
	lib_path=./lib/bin
    lib_name=libsepmvts4swa.so
	cadence_hours=1
    batch_size=10

### cadence_hours

	cadence_hours=1

This provides how frequently the information will be downloaded processed, in hours.

### batch_size

    batch_size=10

This provides the number of time steps to process in the same asynchronous batch. This allows for multiple requrests
to be made to the API for magnetogram data at the same time and processing data that has been returned while waiting for
additional data to be returned.

### lib_path

	lib_path=./lib/bin

This provides the location within the container that the compiled C++ library, that is used for performing parameter
calculations, is located. This is set in the makefile of the repository, so there is not really any reason to ever
change this. The build process of this image should place the compiled library in the location provided, and there is
nothing within this config file that would change that location. This was only included in the config file so that the
location can be easily changed if ever changes are made in the computational library location.

### lib_name

    lib_name=libsepmvts4swa.so

The name of the compiled C++ library that is to be loaded for performing parameter calculations. Just like the path,
this is set in the makefile of the repository, so there is not really any reason to ever change this.

[Return to Top](#top)

***

[Return to README](./README.md)

***
***

## Acknowledgment

This work was supported by NASA Grant Award No. 80NSSC22K0272.

***

This software is distributed using the [GNU General Public License, Version 3](./LICENSE.txt)

![GPLv3](./images/gplv3-88x31.png)

***

© 2023 Dustin Kempton, Berkay Aydin, Piet Martens

[Data Mining Lab](https://dmlab.cs.gsu.edu/)

[Georgia State University](https://www.gsu.edu/)