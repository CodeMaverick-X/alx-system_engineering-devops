#crates a file in /tmp that contains a string
file { '/tmp/school':

  ensure  => 'present',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744'

  }
