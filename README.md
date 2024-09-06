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

- Lectura de Data Streams: Un AWS Lambda se suscribe a Kinesis Data Streams para leer los datos procesados. Basado en reglas predefinidas (por ejemplo, umbrales de semaforización), Lambda genera alertas o notificaciones utilizando Amazon SNS (Simple Notification Service).
- Registro de Eventos en DynamoDB: Cada vez que Lambda se activa y procesa un evento, este se registra en Amazon DynamoDB. Esto permite llevar un historial detallado y consultar los eventos cuando sea necesario.
### 3. Almacenamiento y Monitoreo
#### Almacenamiento en Amazon S3 ("STO Raw"):

- Datos Persistentes: Todos los datos, ya sean en crudo desde Kafka, procesados desde Kinesis Data Firehose, o extraídos desde RDS y otros S3, se almacenan de manera persistente en "STO Raw". Este bucket actúa como el depósito central de datos sin procesar para análisis posterior.

#### Glue Crawlers y Redshift:
- Catálogo de Datos: AWS Glue Crawlers se ejecutan sobre los datos en S3 para catalogar y crear metadatos. Estos datos catalogados se cargan luego en Amazon Redshift para análisis ad-hoc y creación de informes avanzados.

#### CloudWatch para Monitoreo:

- Métricas y Alertas: Amazon CloudWatch monitorea todos los componentes del sistema, desde los brokers de Kafka hasta las funciones Lambda y el rendimiento de Redshift. Se configuran alarmas para cualquier anomalía detectada, asegurando que el equipo pueda reaccionar rápidamente a cualquier fallo en el sistema.
### 4. Resiliencia y Escalabilidad

#### Alta Disponibilidad:

- Redundancia en Kafka: La configuración multi-AZ de Kafka asegura que incluso si una AZ falla, los brokers en las otras AZs pueden continuar operando sin interrupciones.
- Respaldos en S3: Todos los datos críticos son respaldados en S3, lo que no solo garantiza la persistencia, sino que también permite una fácil recuperación en caso de fallos en otros sistemas.
#### Escalabilidad Dinámica:

- Auto Scaling: Los servicios involucrados como Lambda y Kinesis están configurados para escalar automáticamente en respuesta a cambios en la carga de trabajo, asegurando que el sistema pueda manejar picos de tráfico sin degradar el rendimiento.




## Arquitectura Completa con CloudFormation, CodePipeline, Docker, y Kubernetes
#### 1. Aprovisionamiento de la Infraestructura con CloudFormation
##### CloudFormation Templates:

###### Infraestructura de AWS:
- VPC y Subnets: Se crea una VPC (Virtual Private Cloud) con subnets en diferentes AZs. Esto incluye subnets para los brokers de Kafka, Kinesis Data Analytics, RDS, Lambda, etc.
- MSK Cluster (Kafka): CloudFormation aprovisiona un Amazon MSK (Managed Streaming for Apache Kafka) Cluster con brokers distribuidos en múltiples AZs.
- Kinesis Data Analytics: Se configura un Amazon Kinesis Data Analytics que recibe datos de Kafka para su procesamiento en tiempo real.
- S3 Buckets: Los buckets S3 necesarios para almacenar datos crudos (STO Raw) y datos procesados son creados y configurados.
- Glue Jobs y Crawlers: Los trabajos y crawlers de AWS Glue se configuran para catalogar datos en S3 y prepararlos para su análisis en Redshift.
- RDS Instance: Se crea y configura una instancia de Amazon RDS para la ingesta de datos desde bases de datos relacionales.
- Lambda Functions: Las funciones Lambda para el procesamiento de eventos, integración con SNS, y la ingesta desde otros buckets S3 se definen en el template.
- DynamoDB Tables: Las tablas de DynamoDB para registrar eventos de Lambda también se configuran.
- CloudWatch Alarms: Las alarmas y métricas de CloudWatch para monitorear el sistema se configuran para supervisar la salud y el rendimiento de todos los componentes.
- Deploy: Con un solo comando de CloudFormation, toda la infraestructura se aprovisiona de manera automática, asegurando consistencia y reproducibilidad.

#### 2. Integración y Entrega Continua con CodePipeline
##### CodePipeline:

###### Fuente de Código:
GitHub Repository: El código fuente para todas las funciones Lambda, configuraciones de Kafka, Glue Jobs, y cualquier otro script se aloja en un repositorio de GitHub.
Build:
CodeBuild con Docker: AWS CodeBuild se utiliza para construir imágenes Docker para las aplicaciones y servicios personalizados. Las imágenes Docker se generan a partir de Dockerfiles en el repositorio de GitHub.
Deploy:
Implementación con CloudFormation: Las plantillas de CloudFormation generadas en la fase de build se despliegan automáticamente en AWS. Si hay alguna actualización en la infraestructura, CodePipeline se encargará de implementar los cambios de manera controlada.
Implementación de Contenedores en Kubernetes: CodePipeline también integra la implementación continua de contenedores en un clúster de Kubernetes.
Entornos de Prueba y Producción:

Pruebas Automatizadas: Se ejecutan pruebas automatizadas en un entorno de pruebas antes de desplegar en producción, asegurando que cualquier cambio en el código o la infraestructura sea validado antes de afectar al entorno productivo.
3. Contenedorización con Docker
Docker:

Imágenes Docker:
Aplicaciones Customizadas: Las aplicaciones y microservicios se contenedorizan utilizando Docker. Por ejemplo, las funciones Lambda que requieren dependencias específicas pueden ser empaquetadas en imágenes Docker.
Procesos de ETL y Analítica: Los trabajos ETL personalizados o cualquier otro proceso de datos intensivo también se pueden encapsular en contenedores Docker.
Almacenamiento en ECR:

Elastic Container Registry (ECR): Las imágenes Docker se almacenan en Amazon ECR, desde donde se pueden desplegar en cualquier entorno.
4. Orquestación de Contenedores con Kubernetes
Kubernetes:

Clúster de Kubernetes en EKS:
Amazon EKS: Se utiliza Amazon Elastic Kubernetes Service (EKS) para gestionar los contenedores. Kubernetes orquesta el despliegue, la escalabilidad y la gestión de los contenedores Docker en un clúster distribuido.
Auto-Scaling: Kubernetes se configura para escalar automáticamente los pods basados en la carga de trabajo, garantizando que los servicios puedan manejar aumentos en el tráfico sin problemas de rendimiento.
Implementación Rolling: Kubernetes facilita las implementaciones rolling, permitiendo que las nuevas versiones de las aplicaciones se desplieguen sin tiempo de inactividad.
Integración con AWS:

ALB (Application Load Balancer): Un ALB se coloca frente al clúster de Kubernetes para manejar el tráfico entrante y distribuirlo entre los diferentes pods.
IAM Roles para Pods: Los roles de IAM se asignan a los pods para permitir un acceso seguro y controlado a otros servicios de AWS, como S3, DynamoDB, y SNS.
5. Monitoreo y Gestión Continua
CloudWatch y Prometheus:

CloudWatch: CloudWatch sigue siendo la herramienta principal para la monitorización del rendimiento de los servicios de AWS. Además, puedes integrar Prometheus para la monitorización de métricas específicas de Kubernetes y aplicaciones dentro de los contenedores.
Grafana: Para la visualización de métricas tanto de CloudWatch como de Prometheus, Grafana puede ser implementado, proporcionando dashboards en tiempo real para todo el sistema.
