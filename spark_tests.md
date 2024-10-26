# Spark Tests

## Setup

### Install python virtual env

#### Setup virtual environment 
```
python3 -m venv kj
```

and later install libraries
```
kj/bin/pip install pyspark
kj/bin/pip install pytest
```
#### Activate virtual environment

```
source kj/bin/activate
```

## Run spark

```
docker-compose up
```

Upen UI:
```
http://localhost:8080/
```

## Run pyspark applications

```
kj/bin/python3 applications/application_one.py
```

