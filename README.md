# Optimización de Rutas Aéreas en Tiempo Real: Pipeline de Datos en AWS para Aeroméxico   
 
En el negocio de la aviación, la capacidad de monitorear y optimizar rutas de vuelo en tiempo real es crucial para maximizar la rentabilidad, mejorar la satisfacción del cliente, y tomar decisiones estratégicas informadas. Este proyecto se ha diseñado con el objetivo de proporcionar a Aeroméxico un sistema avanzado de análisis y visualización de datos en tiempo real, que permite un control integral sobre el desempeño de sus rutas aéreas.
 
A través de un pipeline de datos robusto, construido utilizando los servicios líderes de AWS como Kinesis Data Streams, Kinesis Data Analytics, S3, AWS Glue, y Athena, procesamos grandes volúmenes de datos de vuelos en tiempo real. Este sistema captura, transforma y almacena la información relevante, desde detalles operacionales hasta métricas financieras y de satisfacción del cliente. 

El resultado es un dashboard dinámico, desarrollado en Tableau e integrado en una web app con Streamlit, que ofrece una visualización intuitiva y detallada de cada ruta de vuelo. Además, se implementan alertas automatizadas mediante SNS y CloudWatch, garantizando que los equipos de Aeroméxico puedan reaccionar rápidamente ante cualquier variación crítica en el rendimiento de sus operaciones.

Este proyecto no solo facilita el análisis de la eficiencia y rentabilidad de las rutas, sino que también sienta las bases para una gestión proactiva y orientada a la mejora continua, colocando a Aeroméxico a la vanguardia de la innovación en la industria aérea.


## Infraestructura en AWS

Esta arquitectura está diseñada para optimizar las rutas aéreas de Aeroméxico en tiempo real, utilizando análisis de datos en streaming. Permite a la compañía analizar la eficiencia de sus rutas, detectar oportunidades de mejora, y reaccionar rápidamente a cambios en la demanda o en la operación. También proporciona herramientas para visualizar la información clave y tomar decisiones basadas en datos para mejorar la satisfacción del cliente y la rentabilidad de las rutas.

![diagram](https://github.com/diegovillatoromx/aeromexico-flight-insights/blob/main/aeromexico-pipeline.png)

### 1. Ingesta de Datos
#### Streaming de Datos (Kafka):

Brokers en Múltiples AZs: La arquitectura de Kafka está configurada con múltiples brokers distribuidos en diferentes Zonas de Disponibilidad (AZs) para garantizar alta disponibilidad y tolerancia a fallos. Cada broker recibe datos en tiempo real desde varias fuentes externas.
Firehose y S3: Los datos recibidos por Kafka se enrutan a Amazon Kinesis Data Firehose para ser transformados y almacenados en un bucket de Amazon S3, denominado "STO Raw". Este S3 es la primera capa de almacenamiento crudo que permite una captura fiable y persistente de los datos.

#### Datos desde RDS:

Glue para ETL: Un proceso ETL (Extract, Transform, Load) es gestionado por AWS Glue, que extrae datos desde una instancia de Amazon RDS. Estos datos también se transforman y se cargan en el mismo bucket de S3 ("STO Raw").
#### Ingesta desde otro S3:

Lambda para Procesamiento: Otra fuente de ingesta proviene de un bucket S3 diferente. Un AWS Lambda se activa para procesar los datos y almacenarlos en el bucket "STO Raw". Este enfoque asegura que los datos desde diferentes fuentes confluyen en el mismo punto de almacenamiento para análisis unificado.

### 2. Procesamiento y Transformación de Datos
#### Kinesis Data Analytics:

- Integración con Kafka: Amazon Kinesis Data Analytics consume datos directamente desde los brokers de Kafka para realizar análisis en tiempo real. Las transformaciones y agregaciones se ejecutan en esta capa para preparar los datos para análisis más profundos.
- Output a Data Streams: Los datos transformados se envían a Amazon Kinesis Data Streams para ser consumidos por otros servicios.

#### AWS Lambda y SNS para Semaforización de Datos:

Lectura de Data Streams: Un AWS Lambda se suscribe a Kinesis Data Streams para leer los datos procesados. Basado en reglas predefinidas (por ejemplo, umbrales de semaforización), Lambda genera alertas o notificaciones utilizando Amazon SNS (Simple Notification Service).
Registro de Eventos en DynamoDB: Cada vez que Lambda se activa y procesa un evento, este se registra en Amazon DynamoDB. Esto permite llevar un historial detallado y consultar los eventos cuando sea necesario.
3. Almacenamiento y Monitoreo
Almacenamiento en Amazon S3 ("STO Raw"):

Datos Persistentes: Todos los datos, ya sean en crudo desde Kafka, procesados desde Kinesis Data Firehose, o extraídos desde RDS y otros S3, se almacenan de manera persistente en "STO Raw". Este bucket actúa como el depósito central de datos sin procesar para análisis posterior.
Glue Crawlers y Redshift:

Catálogo de Datos: AWS Glue Crawlers se ejecutan sobre los datos en S3 para catalogar y crear metadatos. Estos datos catalogados se cargan luego en Amazon Redshift para análisis ad-hoc y creación de informes avanzados.
CloudWatch para Monitoreo:

Métricas y Alertas: Amazon CloudWatch monitorea todos los componentes del sistema, desde los brokers de Kafka hasta las funciones Lambda y el rendimiento de Redshift. Se configuran alarmas para cualquier anomalía detectada, asegurando que el equipo pueda reaccionar rápidamente a cualquier fallo en el sistema.
4. Resiliencia y Escalabilidad
Alta Disponibilidad:

Redundancia en Kafka: La configuración multi-AZ de Kafka asegura que incluso si una AZ falla, los brokers en las otras AZs pueden continuar operando sin interrupciones.
Respaldos en S3: Todos los datos críticos son respaldados en S3, lo que no solo garantiza la persistencia, sino que también permite una fácil recuperación en caso de fallos en otros sistemas.
Escalabilidad Dinámica:

Auto Scaling: Los servicios involucrados como Lambda y Kinesis están configurados para escalar automáticamente en respuesta a cambios en la carga de trabajo, asegurando que el sistema pueda manejar picos de tráfico sin degradar el rendimiento.



