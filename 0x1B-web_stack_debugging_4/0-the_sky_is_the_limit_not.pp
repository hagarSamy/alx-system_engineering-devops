# Increasing the ulimit -- that handles processes and requests

file { '/etc/default/nginx':
  ensure  => present,
  content => 'ULIMIT="-n 4096"\n',
  notify  => Service['nginx'],
}
