# Kills a process named 'killmenow'
exec {'kill_running_script':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/bin',
  onlyif  => '/usr/bin/pgrep killmenow'
}
