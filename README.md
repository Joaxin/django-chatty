# django-chatty

![](django-chatty.png)

This is a basic django chat app using *Django channels* from https://channels.readthedocs.io/en/latest/tutorial/part_4.html and inspired from [Justchat](https://github.com/justdjango/justchat).

You need to install the packages as follows:

```
python -m pip install --upgrade pip
pip install -U channels
pip install -U channels_redis
```
OR

```
pip install -r requirements.txt
```

Then run it,

```
virtualenv env
source dj/bin/activate
cd src
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
python manage.py runserver
```

### Docker

Make sure you have a redis instance running,

```bash
## INSTALL DOCKER
wget -qO- https://get.docker.com/ | sh
sudo usermod -aG docker yourusername # add user group 
sudo service docker start
## INSTALL REDIS
# docker search redis
docker pull redis
docker run -p 6379:6379 -d redis:latest
```

```
docker images
```

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
redis               latest              f7302e4ab3a8        3 weeks ago         98.2MB
```

for windows user, plz install:
https://github.com/docker/toolbox/releases



```
git rm -r --cached .
```

