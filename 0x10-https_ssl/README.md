## 0x10 - HTTPS SSL
This project covers understanding HTTPS and SSL.

### Project files
1. 0-world_wide_web - Displays information about subdomains including destination IP
2. 1-haproxy_ssl_termination - Contains HAproxy configuration to enable HAproxy:
	- listen on port TCP 443
	- accept SSL traffic
	- serve encrypted traffic that will return the root of my web server
	- return 'Holberton School' when querying the root of my domain name
