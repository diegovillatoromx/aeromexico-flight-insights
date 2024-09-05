import aws_cdk as cdk
from aws_cdk import aws_glue as glue
from aws_cdk import aws_rds as rds
from aws_cdk import aws_s3 as s3

class GlueCrawlerStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Crear un bucket S3 para almacenar los datos
        bucket = s3.Bucket(self, "MyBucket")

        # Crear una base de datos RDS
        db_instance = rds.DatabaseInstance(self, "MyDBInstance",
            engine=rds.DatabaseInstanceEngine.MYSQL,
            instance_type=rds.InstanceType.BURSTABLE2_MICRO
        )

        # Crear un Glue Crawler para leer datos de la base de datos RDS
        crawler = glue.Crawler(self, "MyCrawler",
            database_name="aerolinea",
            table_name="Vuelos",
            schedule=glue.Schedule.cron(minute="0", hour="12"),
            targets=[glue Targets.database(
                database_name="aerolinea",
                table_name="Vuelos"
            )],
            role=glue.Role(self, "MyCrawlerRole",
                assumed_by=glue.ServicePrincipal("glue.amazonaws.com")
            )
        )

        # Agregar un target S3 al Glue Crawler
        crawler.add_target(glue Targets.s3(
            bucket=bucket,
            path="data/"
        ))

        # Crear un Glue Job para transformar y cargar los datos en S3
        job = glue.Job(self, "MyJob",
            script=glue.Code.from_asset("script.py"),
            role=glue.Role(self, "MyJobRole",
                assumed_by=glue.ServicePrincipal("glue.amazonaws.com")
            ),
            allocated_capacity=10
        )

        # Agregar el Glue Job al Glue Crawler
        crawler.add_job(job)