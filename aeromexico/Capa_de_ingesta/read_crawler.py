import sys
from awsglue.context import GlueContext
from awsglue.job import Job

glue_context = GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)

# Leer datos de la base de datos RDS
df = glue_context.read.format("jdbc").option("url", "jdbc:mysql://<RDS_INSTANCE_ENDPOINT>:3306/aerolinea").option("driver", "com.mysql.cj.jdbc.Driver").option("dbtable", "Vuelos").load()

# Transformar datos
df_transformed = df.select("id", "origen", "destino", "fecha_hora_salida", "fecha_hora_llegada")

# Cargar datos en S3
df_transformed.write.format("parquet").save("s3://my-bucket/data/")