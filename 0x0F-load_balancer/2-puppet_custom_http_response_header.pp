#Puppet that creates a custom HTTP header response.
exec {'header':
  command => 'sudo apt-get update -y,
	      sudo apt-get install nginx -y,
	      sudo sed -i "s/^server\s{/server {\n\tadd_header X-Served-By $HOSTNAME;/1" /etc/nginx/sites-available/default
	      sudo service nginx restart',
  path    => '/usr/bin'
}
