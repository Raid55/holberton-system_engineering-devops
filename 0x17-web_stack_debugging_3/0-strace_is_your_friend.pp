exec { 'fix_bug':
    path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    command  => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php'
}
