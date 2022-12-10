# config ssh config file
$str = "Host 54.236.25.236
        User ubuntu
        IdentityFile ~/.ssh/school
        IdentitiesOnly yes"

file { '/home/vagrant/.ssh/config':
  ensure  => 'present',
  content => $str
}
