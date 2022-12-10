file { '/tmp/school':

  ensure  => 'present',
  content => 'I Love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744'

  }
