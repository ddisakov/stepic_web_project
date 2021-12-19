import multiprocessing

bind = "127.0.0.1:8080"

worker = 2
errorlog ='/home/isakov/box/web/logs/gunicorn/error.log'
accesslog = '/home/isakov/box/web/logs/gunicorn/access.log'

proc_name = 'gunicorn_hello'
