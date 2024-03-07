# Set up client SSH configuration file so user can connect without password
file {'~/.ssh/config':
	ensure => file,
	content => 'Host 398697-web-01\n	User=ubuntu\n	HostName=34.224.4.177\n	IdentityFile=~/.ssh/school\n	PasswordAuthentication=no',
	require => File[~/.ssh]
}
