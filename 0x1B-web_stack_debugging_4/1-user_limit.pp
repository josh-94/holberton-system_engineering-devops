#Using Puppet to Change the OS configuration so that it is possible to login with the holberton user opening bigger limit files.
exec {'sed':
    command  => "sed -i 's/holberton hard nofile 5/holberton hard nofile 100/' /etc/security/limits.conf",
    provider =>  shell
}
exec {'sed':
    command  => "sed -i 's/holberton soft nofile 4/holberton soft nofile 100/' /etc/security/limits.conf",
    provider => shell
}
