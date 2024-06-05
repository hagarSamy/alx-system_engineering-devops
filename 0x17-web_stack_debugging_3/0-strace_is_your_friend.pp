# Fixes extension problem in php file

exec {'Fix_php':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    # the search path that Puppet uses to locate the command `sed`
    path    => '/usr/local/bin/:/bin/',
    }
