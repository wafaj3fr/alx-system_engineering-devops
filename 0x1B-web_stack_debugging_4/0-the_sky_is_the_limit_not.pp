exec { 'fix':
	command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
	path => '/usr/local/bin/:/bin/',
}
exec { 'nginx-restart':
	command => '/etc/init.d/nginx reastart',
	path => '/etc/init.d/',
}
