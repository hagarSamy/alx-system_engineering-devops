# Configures SSH for no password and specifying IdentityFile

file_line { 'identityfile':
    path => '/etc/ssh/ssh_config',
    line => '    IdentityFile ~/.ssh/school',
}

file_line { 'passwordauth':
    path => '/etc/ssh/ssh_config',
    line => '    PasswordAuthentication no',
}
