#Using Puppet to Change the OS configuration so that it is possible to login with the holberton user opening bigger limit files.
exec {'sed':
    command  => 'sed -i "s/5/15/g  /etc/security/limits.conf',
    provider =>  shell
}
exec {'sed':
    command  => 'sed -i "s/4/14/g" /etc/security/limits.conf',
    provider => shell
}
