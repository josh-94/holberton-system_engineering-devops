#Using Puppet to Change the OS configuration so that it is possible to login with the holberton user opening bigger limit files.
exec {'sed':
    command  => 'sed -i "s/holberton soft nofile.*/holberton soft nofile 9000 /"  /etc/security/limits.conf',
    provider =>  shell
}
exec {'sed':
    command  => 'sed -i "s/holberton hard nofile.*/holberton hard nofile 9000/ /etc/security/limits.conf',
    provider => shell
}
