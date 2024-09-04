# Optimización de Rutas Aéreas en Tiempo Real: Pipeline de Datos en AWS para Aeroméxico

En el negocio de la aviación, la capacidad de monitorear y optimizar rutas de vuelo en tiempo real es crucial para maximizar la rentabilidad, mejorar la satisfacción del cliente, y tomar decisiones estratégicas informadas. Este proyecto se ha diseñado con el objetivo de proporcionar a Aeroméxico un sistema avanzado de análisis y visualización de datos en tiempo real, que permite un control integral sobre el desempeño de sus rutas aéreas.

A través de un pipeline de datos robusto, construido utilizando los servicios líderes de AWS como Kinesis Data Streams, Kinesis Data Analytics, S3, AWS Glue, y Athena, procesamos grandes volúmenes de datos de vuelos en tiempo real. Este sistema captura, transforma y almacena la información relevante, desde detalles operacionales hasta métricas financieras y de satisfacción del cliente.

El resultado es un dashboard dinámico, desarrollado en Tableau e integrado en una web app con Streamlit, que ofrece una visualización intuitiva y detallada de cada ruta de vuelo. Además, se implementan alertas automatizadas mediante SNS y CloudWatch, garantizando que los equipos de Aeroméxico puedan reaccionar rápidamente ante cualquier variación crítica en el rendimiento de sus operaciones.

Este proyecto no solo facilita el análisis de la eficiencia y rentabilidad de las rutas, sino que también sienta las bases para una gestión proactiva y orientada a la mejora continua, colocando a Aeroméxico a la vanguardia de la innovación en la industria aérea.


## Infraestructura en AWS

Esta arquitectura está diseñada para optimizar las rutas aéreas de Aeroméxico en tiempo real, utilizando análisis de datos en streaming. Permite a la compañía analizar la eficiencia de sus rutas, detectar oportunidades de mejora, y reaccionar rápidamente a cambios en la demanda o en la operación. También proporciona herramientas para visualizar la información clave y tomar decisiones basadas en datos para mejorar la satisfacción del cliente y la rentabilidad de las rutas.

<img src='https://github.com/diegovillatoromx/aeromexico-flight-insights/blob/main/aeromexico-pipeline.gif' alt="architecture_diagram">
![diagram](https://github.com/diegovillatoromx/aeromexico-flight-insights/blob/main/aeromexico-pipeline.png)

### App Simulation (Simulación de Aplicación):

AWS Cloud9 con AWS CDK: Esta parte de la arquitectura simula la generación de datos en tiempo real, probablemente relacionada con rutas aéreas, pasajeros, costos, ingresos, etc. El entorno de desarrollo AWS Cloud9, junto con AWS CDK (Cloud Development Kit), se utiliza para desplegar y gestionar la infraestructura de la simulación.

### Kafka:

Streams de Kafka: Los datos generados por la simulación son enviados a Kafka, que actúa como un broker de mensajería para manejar el flujo de datos en tiempo real. Kafka permite la ingestión continua de grandes volúmenes de datos y facilita el procesamiento en tiempo real.

### AWS Glue:
Firehose: Los datos de Kafka se envían a través de Amazon Kinesis Data Firehose, que se encarga de cargar, transformar y entregar datos en servicios de destino como Amazon S3 y Amazon Redshift.
AWS Glue: Se utiliza AWS Glue para ETL (Extracción, Transformación y Carga) de los datos en bruto almacenados en S3. AWS Glue cataloga, organiza y prepara los datos para su análisis. Aquí se almacenan en formatos como Parquet, que es eficiente para análisis.

### Amazon S3:

Conjunto de datos y almacenamiento RAW: S3 se utiliza como almacenamiento de datos en diferentes etapas: almacenamiento inicial de datos en bruto, y almacenamiento de datos transformados (por AWS Glue) en formato Parquet o JSON.

### Data Analytics con Kinesis:

Streams: La arquitectura también utiliza Amazon Kinesis Data Analytics para procesar los datos en tiempo real directamente desde Kafka, realizando análisis y agregaciones necesarias.

### Amazon Redshift:

Almacenamiento de datos: Amazon Redshift es el data warehouse donde los datos transformados se almacenan para análisis de alto rendimiento. Redshift permite realizar consultas SQL complejas y análisis de grandes volúmenes de datos.

### Tableau:

Visualización de datos: Tableau se conecta a Amazon Redshift para visualizar los datos analíticos. Aquí es donde se crearán dashboards que muestran rutas aéreas, ingresos, costos, satisfacción del cliente, y otras métricas importantes.

### Lambda, DynamoDB, SNS, y CloudWatch:

AWS Lambda: Se utiliza para ejecutar código en respuesta a eventos, por ejemplo, para procesar y enrutar datos analizados hacia DynamoDB o enviar notificaciones.
DynamoDB: DynamoDB almacena datos procesados de forma eficiente, posiblemente para consultas rápidas o almacenamiento de metadatos.
Amazon SNS (Simple Notification Service): SNS se utiliza para enviar alertas o notificaciones basadas en los análisis en tiempo real.
Amazon CloudWatch: Se utiliza para monitorizar y registrar los eventos del sistema, permitiendo un seguimiento y resolución de problemas en tiempo real.






