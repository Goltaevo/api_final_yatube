# api_final
api final

### web resource where you can share your thoughts about stuff and world

### Features:

- users can create account
- users can create and edit posts
- users can view posts of other users
- users can add comments to posts
- users can subscribe/ unsubscribe to/from other users


### Authors

Evgeny Asminin

### Installation Notes:

Clone repo and change directory:

```
git clone https://github.com/Goltaevo/api_final_yatube.git
```

```
cd api_final_yatube
```

Create and activate venv:

```
python3 -m venv env
```

```
source env/bin/activate
```

Upgrade pip if necessary:

```
python3 -m pip install --upgrade pip
```

Deploy venv according to requirements.txt:

```
pip install -r requirements.txt
```

Deploy migrations:

```
python3 manage.py migrate
```

Launch project server:

```
python3 manage.py runserver
```

API documentation available in [ReDoc](https://redocly.github.io/redoc/#operation/addPet) on endpoint:

```
http://127.0.0.1:8000/redoc/
```
