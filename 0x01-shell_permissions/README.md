I'm learning shell permissions, this is fun

0-iam_betty, switches current user to user betty

1-who_am_i, prints effective username of the current user

2-groups, prints all groups the current user is a part of

3-new_owner, changes owner of file hello to betty

4-empty, creates an empty file hello

5-execute, adds execute permission to owner of file hello

6-multiple_permissions, adds execute permission to owner and group owners and adds read permission to other users

7-everybody, adds execution permission to owner, group owner and others without commas in the command

8-James_Bond, sets no permission to owner and group owner, and all permissions to others

9-John_Doe, set mode of file hello to -rwxr-x-wx

10- 10-mirror_permissions, sets the mode of the file hello the same as olleh’s mode

11-directories_permission, adds execute permission to all subdirectories in the current directory for owner, group owner and others

12-directory_permissions, creates a directory called my_dir with permissions 751 in the working directory

13-change_group,  changes the group owner to school for the file hello

100-change_owner_and_group, changes the owner to vincent and the group owner to staff for all the files and directories in the working directory

101-symbolic_link_permissions, changes the owner and the group owner of _hello to vincent and staff respectively.

101-symbolic_link_permissions, script that changes the owner and the group owner of _hello to vincent and staff respectively.

102-if_only, script that changes the owner of the file hello to betty only if it is owned by the user guillaume
