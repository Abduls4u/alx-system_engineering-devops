# Increases the file limit by nullifying the set default using
exec { 'fix-limit' :
  command => 'sed -i s/ULIMIT/#ULIMIT/g /etc/default/nginx',
  path    => '/bin/',
}
exec { 'restart-nginx' :
  command => 'sudo service nginx restart',
  path    => '/usr/bin/',
  require => Exec['fix-limit'],
}
