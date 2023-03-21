Descriptions of what each script is doing:

	0-hello_world		this is a bash script that will output "Hello, World" when executed.
	1-confused_smiley	this is a script that will output the string "(Ôo)' when executed.
	2-hellofile		this is a script that will output the contents of the '/etc/passwd' file when executed. 
	3-twofiles 		this a script that will output the contents of both the '/etc/passwd' file and the '/etc/hosts' file.
	4-lastlines		this script will output the last 10 lines (-n specifies number of lines to display) of the '/etc/passwd' file.
	5-firstlines		this script will output the first 10 lines (-n specifies number of lines to display) of the '/etc/passwd' file.
	6-third_line		this script extracts the third line of a file named 'iacta' using the 'head' and 'tail' commands.
	7-file			this script uses 'echo' command to write the string "Best School" to a file with a complex name: "*\''"Best School"'\*\\*$?*****:)" using the > operator to redirect the output.
	8-cwd_state		this script uses the 'ls' command with the '-la' option to list all files and directories in the current directory, including hidden files, and redirect the output to a file named 'ls_cwd_content'.
	9-duplicate_last_line	this script uses the 'tail' command with the '-n 1' option to display the last line of the file named 'iacta', and then appends the line to the end of the same file using the '>>' operator.
	10-no_more_js		a script that uses the 'find' command to search for all files with the extension '.js' in the current directory and all its subdirectories, and then deletes them using the '-delete' option (the '.' in the find command specifies the current directory. The '-type f' option specifies that only regular files should be considered, and the '-name "*js"' option specifies that only files with the '.js' extension should be considered.
	11-directories		using the find command to search all directories, the '.' specifies the current directory as the starting point of the search. The '-mindepth 1' specifies that only directories at least one level deep should be considered to exclude the starting directory. The '-type d' option specifies that only directories should be considered. The '-not -path "'*/\.*'" excluding hidden directories starting with a dot.
	12-newest_files		lists the files in the current directory sorted by modification time using the 'ls -t' command, and then displays the first 10 files using the 'head -10' command.
	13-unique		sorts the input lines using the 'sort' command, then displays only the unique lines using the 'uniq -u' command. (assuming input is provided through a pipe through standard input and '-u' options makes 'uniq' display only the unique lines, discarding all duplicate lines.
	14-findthatword		searches for the string "root" in file '/etc/passwd' using the 'grep' command.
	15-countthatword	searches for the string "bin" in the file '/etc/passwd' and counts the number of matching lines using the '-c' option.
	16-whatsnext		script that searches for the string "root" in the file '/etc/passwd' using the 'grep' and displays the three lines that follow each matching line using the '-A' option.
	17-hidethisword		script that searches for lines in the file '/etc/passwd' that do not contain the string "bin" using the 'grep' command and displays the matching lines using the '-v' option.
	18-letteronly		script that searches for lines in the file '/etc/ssh/sshd_config' that start with an alphabetic character using the 'grep' command, and then displays the matching lines (The ^ character represents the start of the line, and [[:alpha:]] represents any alphabetic character).
	19-AZ			script uses the 'tr' command to replace all occurrences of the characters 'A' and 'c' with 'Z' and 'e', respectively, in its input.
	20-hiago		script uses the 'tr' command to delete all occurrences of the characters 'c' and 'C' in its input.
	21-reverse		script that uses the 'rev' command to reverse the order of characters in its input.
	22-users_and_homes	script that extracts the user names and home directories from the '/etc/passwd' file using the 'cut' command and sorts them alphabetically using the 'sort' command (the "-d':'" specifies that the fields in the 'passwd' file delimited by colons. The '-f1.6' only the first and sixth field should be extracted. The output of 'cut' is then pipes to 'sort' which sorts if alphabetically before printing it).
	100-empty_casks		script that searches for empty files or directories in the current directory and subdirectories and prints their names to the terminal (The 'find' command uses '.' to search for files and directories in the current directory. The '-empty' option specifies to only match empty files and directories. The "-printf '%f\n'" only the names of the empty files and directories should be printed each on a separate line).
	101-gifs		this script will search for files with a .gif extension in the current directory and its subdirectories, extract their names and sort them alphabetically, case-insensitively. The final output will be a list of .gif file names (without the extension) in alphabetical order, with each name on a separate line.
	102-acrostic		a script that takes the first character of each line of input and concatenates them into a single string.
	103-the_biggest_fan	when you run this script, it will count the frequency of each word in the input (assuming the input is a list of words), and output the top 10 most frequent words in descending order of frequency. The output will be a list of words, with one word per line.
