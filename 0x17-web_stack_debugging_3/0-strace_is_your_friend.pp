#Using Puupet to debugg server.
exec {'sed':
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
    provider =>  shell,
}
