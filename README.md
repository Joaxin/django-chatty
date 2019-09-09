# django-chatty

This is a basic django chat app using *Django channels* from https://channels.readthedocs.io/en/latest/tutorial/part_4.html

```
python -m pip install --upgrade pip
pip install -U channels
pip install -U channels_redis
```

```
git rm -r --cached .
```
for windows
https://github.com/docker/toolbox/releases

```
python manage.py migrate

```


```
virtualenv env
source env/bin/activate
cd src
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
# docker run -p 6379:6379 -d redis:2.8
python manage.py runserver
```
