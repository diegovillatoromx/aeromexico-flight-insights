import aws_cdk as cdk 
from aws_cdk import aws_msk as msk 
from aws_cdk import aws_kinesisfirehose as firehose
from aws_cdk import aws_s3 as s3
 
class KafkaToFirehoseStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ... (Código existente para crear el clúster Kafka)

        # Crear un bucket S3 para almacenar los datos
        bucket = s3.Bucket(self, "KafkaDataBucket")

        # Crear una delivery stream de Kinesis Data Firehose
        delivery_stream = firehose.CfnDeliveryStream(self, "KafkaDeliveryStream",
            delivery_stream_name="KafkaToS3",
            s3_destination_configuration=firehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                role_arn="arn:aws:iam::your-account-id:role/your-firehose-role",  # Reemplazar con el ARN de tu rol
                bucket_arn=bucket.bucket_arn,
                prefix="kafka-data/"
            )
        )

        # Crear reglas de punto final para cada tópico y enviar los datos a Firehose
        topics = ["vuelos", "operaciones", "avion", "pasajeros", "carga", "meteorologia"]
        for topic in topics:
            try:
                cluster.add_stream(
                    stream_name=f"{topic}-firehose",
                    target_arn=delivery_stream.attr_arn
                )
            except Exception as e:
                print(f"Error al crear la regla de punto final para el tópico {topic}: {e}")
                raise
