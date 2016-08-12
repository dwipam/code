from pyspark import SparkContext
from pyspark.sql import SQLContext
import pandas as pd


sc = SparkContext("local","r")
sqlcontext = SQLContext(sc)
x = pd.DataFrame({'id':123,'name':'xyz'},index=[1])
r = sqlcontext.createDataFrame(x)
r.show()
