import aws_cdk as cdk
from aws_cdk import aws_msk as msk
from aws_cdk import aws_ec2 as ec2
 
class KafkaStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, env=cdk.Environment(region='us-east-1'), **kwargs)

        # Create a VPC with multiple subnets in different availability zones
        vpc = ec2.Vpc(self, "KafkaVpc", max_azs=3)
        subnet_group = vpc.select_subnets(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)

        # Create an MSK cluster with high availability configuration
        kafka_cluster = msk.Cluster(self, "MyKafkaCluster",
            vpc=vpc,
            cluster_name="my-kafka-cluster",
            kafka_version=msk.KafkaVersion.V2_13,
            number_of_broker_nodes=3,
            client_authentication=msk.ClientAuthentication.unauthenticated(),
            encryption_in_transit=msk.EncryptionInTransit.ENABLED,
            enhanced_monitoring=msk.EnhancedMonitoring.DEFAULT,
            broker_node_group_info=msk.BrokerNodeGroupInfo(
                instance_type=ec2.InstanceType("m5.large"),
                ebs_volume_size=1000
            )
        )

        # Create 6 topics with customized configurations
        for topic in ["vuelos", "operaciones", "avion", "pasajeros", "carga", "meteorologia"]:
            msk.Topic(self, f"Topic{topic}",
                cluster=kafka_cluster,
                partitions=3,
                replication_factor=3,
                configuration={
                    "retention.ms": 86400000,  # 1 día
                    "compression.type": "snappy"
                }
            )
