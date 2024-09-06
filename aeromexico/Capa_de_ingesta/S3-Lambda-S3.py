import boto3
import os 
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Configuración de los buckets S3
    source_bucket = 'mi-bucket-origen'
    target_bucket = 'mi-bucket-destino'
    prefix = 'data/'

    # Obtener la lista de objetos en el bucket origen
    objects = s3.list_objects_v2(Bucket=source_bucket, Prefix=prefix)

    # Ordenar los objetos por fecha de última modificación
    objects.sort(key=lambda x: x['LastModified'])

    # Copiar los objetos al bucket destino
    for obj in objects:
        key = obj['Key']
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(CopySource=copy_source, Bucket=target_bucket, Key=key)

        # Agregar metadatos adicionales para mejorar la precisión del crawler de Glue
        metadata = {
            'fecha_carga': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'fuente': 'mi-bucket-origen',
            'tipo_dato': 'csv'
        }
        s3.put_object_tagging(
            Bucket=target_bucket,
            Key=key,
            Tagging={
                'TagSet': [{'Key': k, 'Value': v} for k, v in metadata.items()]
            }
        )

    return {
        'statusCode': 200,
        'statusMessage': 'Datos copiados con éxito'
    }
