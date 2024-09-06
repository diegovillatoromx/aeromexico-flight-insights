import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Obtiene las opciones de la ejecución del job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Crea un contexto de Spark y Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Lee los datos de las tres fuentes en S3
data1 = spark.read.parquet("s3://bucket1/data1/")
data2 = spark.read.parquet("s3://bucket2/data2/")
data3 = spark.read.parquet("s3://bucket3/data3/")

# Une los datos en un solo DataFrame
data = data1.union(data2).union(data3)

# Ordena los datos por una columna específica
data = data.orderBy("columna_orden")

# Carga los datos en Amazon Redshift
data.write.format("jdbc") \
    .option("url", "jdbc:redshift://cluster-name:5439/database") \
    .option("dbtable", "schema.tabla") \
    .option("user", "usuario") \
    .option("password", "contraseña") \
    .save()