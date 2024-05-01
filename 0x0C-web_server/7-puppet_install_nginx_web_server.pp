# Installs and configure an Nginx server using Puppet instead of Bash
exec {'install':
  provider => shell,
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo ufw allow 'Nginx HTTP' ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; echo -e "Ceci n'est pas une page\n" | sudo tee /var/www/html/404.html ; sudo sed -i '/listen 80 default_server/a rewrite ^/redirect_me https://github.com/hagarSamy permanent;' /etc/nginx/sites-available/default ; sudo sed -i "/redirect_me/ a\\\terror_page 404 /404.html;" /etc/nginx/sites-available/default ; sudo service nginx restart',
}
