from pyspark.sql import SparkSession
from pyspark.sql import Row

class ProjectOne:
    def run(self):
        # create spark session
        spark = SparkSession.builder \
            .appName("PySpark project") \
            .master("spark://172.19.0.3:7077") \
            .getOrCreate()
        
        dataframe = spark.createDataFrame([
                Row(a=1, b=2., c='string1' ),
                Row(a=2, b=3., c='string2' ),
                Row(a=4, b=5., c='string3' )
            ])

        # show
        dataframe.show()

        # count
        dataframe.count()

        # select
        spark.sql( "SELECT * FROM dataframe" ).collect()

        dataframe.printSchema()


