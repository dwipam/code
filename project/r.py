from pyspark import SparkContext
from pyspark.sql import SparkSession
import pandas as pd

#sc = SparkContext("local","r")
#sqlcontext = SQLContext(sc)i

spark = SparkSession.builder \
	.master("spark://localhost-2.local:7077") \
        .appName("Temp") \
        .config("spark.some.config.option", "some-value") \
	.getOrCreate()
x = pd.DataFrame({'id':2,'name':"TEMP"},index=[0])
spark.createDataFrame(x).write.saveAsTable("temp")
temp = spark.table("temp").toPandas()
spark.sql("drop table temp")
x = pd.DataFrame({'id':2,'name':"TEMP"},index=[0])
x = x.append(temp)
spark.createDataFrame(x).write.saveAsTable("temp")
q.write.saveAsTable("temp")
