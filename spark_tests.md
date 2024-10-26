# Spark Tests

## Setup

### Install python virtual env

#### Install python
```
sudo apt install python3.9
```

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

### Install java

```
java -version
sudo apt-get install openjdk-8-jdk
java -version
```

## Run spark

```
docker-compose up
```

Open UI:
```
http://localhost:8080/
```

Open jupyter notebook:
```
http://localhost:8888
```


## Pyspark applications

### Test: Hello World

Run:
```
kj/bin/python3 applications/application_one.py
```


# Run spark from command line

https://hub.docker.com/_/spark

```
docker run -it spark:python3 /opt/spark/bin/pyspark
```

## Test 1: 

```
from pyspark.sql import Row
dataframe = spark.createDataFrame([
                Row(a=1, b=2., c='string1' ),
                Row(a=2, b=3., c='string2' ),
                Row(a=4, b=5., c='string3' )
            ])
dataframe.show()
exit() 
```



# References

Spark compatibility matrix: https://sparkbyexamples.com/spark/spark-versions-supportability-matrix/

Spark docker image to use: https://hub.docker.com/_/spark
