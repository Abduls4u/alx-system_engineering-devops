# debug task 1
exec { 'fix-limit' :
  command => "sed -i 's/nofile [0-9]/nofile 65535/g' /etc/security/limits.conf",
  path    => '/bin/',
}
