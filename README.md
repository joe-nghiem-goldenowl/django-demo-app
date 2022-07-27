## Install requirements

```
pip install -r requirements.txt
```

## Commands
### Start server
```python
python manage.py runserver
```
### Run celery
#### Celery beat
```python
celery -A demo beat -l info -S django
```
#### Celery worker
```python
celery -A demo worker -l info [-P eventlet]
```
### Unit test
First, you need to collect static files using this command:
```python
python manage.py collectstatic
```
Then, run the unit tests
```python
coverage run --source='.' manage.py test backend
```
View report by
```python
coverage report
```
## Heroku
Heroku deploy at [here](https://django-demoo.herokuapp.com/)