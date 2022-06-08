#Using Puppet to Change the OS configuration so that it is possible to login with the holberton user opening bigger limit files.
exec {'sed':
    command  => 'sed -e "s/5/15/g" -e "s/4/14/g" /etc/security/limits.conf',
    provider =>  shell,
}
