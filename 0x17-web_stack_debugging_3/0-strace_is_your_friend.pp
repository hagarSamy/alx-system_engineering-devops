# Fixes extension problem in php file

exec {'Fix_php':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    # path    => '/usr/local/bin/:/bin/',
    }
