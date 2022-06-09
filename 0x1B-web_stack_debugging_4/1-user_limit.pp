#Using Puppet to Change the OS configuration so that it is possible to login with the holberton user opening bigger limit files.
exec {'sed':
    provider => shell,
    command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 50000/g"
	      /etc/security/limits.conf; sudo sed -i "s/holberton soft nofile 4/holberton hard nofile 40000/g" /etc/security/limits.conf'
}
