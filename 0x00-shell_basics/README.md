Descriptions of what each script is doing:

	0-current_working_directory 	prints the absolute path of the current working directory.
	1-listit displays 		the contents list of the current directory.
	2-bring_me_home 		changes the working directory to the user's home directory.
	3-listfiles 			displays current directory contents in a long format.
	4-listmorefilesi		displays current directory content, including hidden files using the long format.
	5-listfilesdigitonly		display current directory contents, in a long format with user and group IDs displayed numerically and hidden files.	
	6-firstdirectory		creates a directory named my_first_directory in the /tmp/ directory.
	7-movethatfile			moves the file betty from /tmp/ to /tmpt/my_first_directory.
	8-firstdelete			delete the file betty in /tmp/my_first_directory.
	9-firstdirdeletion		delete the directory my_first_directory that is in the /tmp/directory.
	10-back				change the working directory to the previous one.
	11-lists			list all the files (even ones with name beginning with a period) in the current directory and parent of the working directory and the /boot directory, in long format.
	12-file_type			print the type of the file name iamafile, which is in the /tmp directory.
	13-symbolic_link		create a symbolic link to /bin/ls named __ls__ in the current working directory.
	14-copy_html			copy all the HTML files from the current working directory to the parent but only copy files that did not exist in the parent directory or were newer than the versions in the parent of the working directory.
	100-lets_move			move all the files beginning with an uppercase letter to the directory /tmp/u assuming it exists.
	101-clean_emacs			delete all files in the current working directory that end with ~ (Emacs).
	102-tree			create the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
	103-commas			lists all the files and directories of the current directory, separated by commas (,). Directory names will end with a slash (/), Files and directories starting with a dot (.) will be listed, The listing will be alpha ordered, except for the directories . and .. which will be listed at the very beginning, Only digits and letters are used to sort; Digits will come first, The listing will end with a new line.
	school.mgc			creates a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
