sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#gunicorn --bind='0.0.0.0:8000' hello:app

#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql startls
