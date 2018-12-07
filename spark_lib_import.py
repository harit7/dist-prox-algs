'''
Created on 21-Aug-2015

@author: harit
'''
#SPARK_HOME = "/home/harit.vishwakarma/spark-1.5.0-bin-hadoop2.6/"
version = "1.5.1"
SPARK_HOME = "/home/harit.vishwakarma/spark-"+version+"-bin-hadoop2.6/"

PYSPARK_HOME = SPARK_HOME + "python/"
PYSPARK_CSV_HOME = PYSPARK_HOME + "pyspark/pyspark-csv/"

import os
import sys

os.environ['SPARK_HOME'] = SPARK_HOME
sys.path.append(PYSPARK_HOME)
sys.path.append(PYSPARK_HOME+"lib/py4j-0.8.2.1-src.zip")
sys.path.append(PYSPARK_CSV_HOME)

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SQLContext
    import pyspark_csv as pycsv
#    print sys.path
    print("Spark "+version+" libraries imported successfully.")

except ImportError as e:
    print("Spark libraries could not be imported!", e)
    sys.exit(1)

def getDefaultSparkContext():
    conf =  SparkConf(). \
            setAppName("filter").\
            setMaster("local[16]").\
            set("spark.executer.memory","64g").\
            set("spark.driver.memory","64g").\
	    set("spark.driver.maxResultSize","2g").\
            set("spark.driver.allowMultipleContexts","true")
            
    sc  = SparkContext(conf=conf)
     
    sc.addPyFile(PYSPARK_CSV_HOME+'pyspark_csv.py')

    return sc

def getSparkSQLContext(sc):
    return SQLContext(sc)
