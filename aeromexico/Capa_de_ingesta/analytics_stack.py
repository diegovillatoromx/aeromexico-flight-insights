import aws_cdk as cdk
from aws_cdk import aws_kinesisanalytics as kda
from aws_cdk import aws_iam as iam 

class KinesisAnalyticsStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, env=cdk.Environment(region='us-east-1'), **kwargs)

        # Create a Kinesis Data Analytics application
        analytics_app = kda.Application(self, "MyAnalyticsApp",
            application_name="my-analytics-app"
        )

        # Create a Kinesis Data Analytics SQL query
        query = kda.SqlQuery(self, "MyQuery",
            application=analytics_app,
            query="""
                SELECT 
                    data->>'id' AS id,
                    data->>'temperature' AS temperature,
                    data->>'humidity' AS humidity
                FROM 
                    MyInputStream
                WHERE 
                    data->>'temperature' > 25
            """
        )

        # Create a Kinesis Data Analytics input
        input_stream = kda.Input(self, "MyInputStream",
            kinesis_stream=cdk.Fn.import_value("MyKinesisStreamArn")
        )

        # Add the input to the query
        query.add_input(input_stream)

        # Create a Kinesis Data Analytics output
        output_stream = kda.Output(self, "MyOutputStream",
            kinesis_stream=cdk.Fn.import_value("MyOutputStreamArn")
        )

        # Add the output to the query
        query.add_output(output_stream)
