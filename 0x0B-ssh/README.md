#0x0B - SSH
##Introduction
This repository contains my code for the SSH project in the ALX Software
Engineering Programme.

An Ubuntu server was attributed for this project. This server was configured
with my public key created in a
[previous project](https://github.com/NiniolaX/alx-system_engineering-devops/0x04-loops_conditions_and_parsing/0-RSA_public_key.pub)


##Files
This repository contains the following files:
1. 0-use_a_private_key - Uses SSH to connect to the server using the private key
~/.ssh/school with user *ubuntu*.
2. 1-create_ssh_key_pair - Creates an RSA key pair with
	- private key name 'school',
	- 4096 bits in created key, and
	- key protected with a passphrase *betty*.
3. 2-ssh_config - Configures server so user can connect without a password.
