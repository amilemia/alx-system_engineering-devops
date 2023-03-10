Descriptions of what each script is doing:

	0-iam_betty			assuming user betty exists switch the current user to the user betty, using 8 characters for the command.
	1-who_am_i			print the username of the current user.
	2-groups			print all the groups the current user is part of.
	3-new_owner			change the owner of the file hello to the user betty.
	4-empty				creat an empty file called hello.
	5-execute			add execute permission to the owner of the file hello.
	6-multiple_permissions		add execute permission to the owner and the group and read permission to the other users, on file hello.
	7-everybody			add execute permission to the owner, the group and the other users, on file hello.
	8-James_Bond			set permission of the file hello to: Owner - no permission, Group - no permission, Other users - all the permissions.
	9-John_Doe			set permission of the file hello to: -rwxr-x-wx without using commas.
	10-mirror_permissions		set permission of the file hello the same as olleh permission.
	11-directories_permissions	add execute permission to all subdirectories of the current directory for the owner, the group and all other users without changing regular files.
	12-directory_permissions	create a directory called my_dir with permissions 751 (u+rwx,g-w,o-rw) in the working directory.
	13-change_group			change the group owner to school for the file hello in the working directory.
	100-change_owner_and_group	change the owner to vincent and the group to staff for all the files and directories in the working directory.
	101-symbolic_link_permissions	change the owner and the group of file _hello (symbolic link) in working directory to vincent and staff respectively.
	102-if_only			change the owner of the file hello in the working directory to betty only if the owner is guillaume.
	103-Star_Wars			play the StarWars IV episode in the terminal.
