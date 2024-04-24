# instal and configure nginx
exec { 'apt-update':
  command     => 'apt-get -y update',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}
exec { 'apt-get':
  command => 'apt-get -y install nginx',
  path    => '/usr/bin:/bin',
  require => Exec['apt-update'],
}

-> file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file_line { 'add_redirect':
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'server_name _;',
  line   => '    location /redirect_me {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}',
  notify => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File_line['add_redirect'],
}
