#Using Puupet to debugg nginx server by increasing the ULIMIT which handle the amount of requests and responses.
exec {'sed':
    command  => 'sed -i "s/15/500/g" /etc/default/nginx & sudo service nginx restart',
    provider =>  shell,
}
