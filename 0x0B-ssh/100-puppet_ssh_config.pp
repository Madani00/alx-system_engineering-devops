# fix: i forget this comment

file_line {'refuse to authenticate using a password':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  ensure => present,
}

file_line {'SSH client configuration using the private key':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  ensure  => present,
}
