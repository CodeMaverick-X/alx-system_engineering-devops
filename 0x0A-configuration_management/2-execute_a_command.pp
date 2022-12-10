#a manifest to kill a process named killmenow
exec { '/usr/bin/pkill':
  command => '/usr/bin/pkill killmenow',
}
