# This puppet file adds a new configuration for holberton user
# By changing the number of open file limits, for warning and errors..

file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton hard nofile 5000\nholberton soft nofile 4000\n",
}
