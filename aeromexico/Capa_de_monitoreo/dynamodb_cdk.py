import * as cdk from 'aws-cdk-lib';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';

export class DynamoDBStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const table = new dynamodb.Table(this, 'MyTable', {
      tableName: 'my-table',
      attributeDefinitions: [
        {
          AttributeName: 'id',
          AttributeType: dynamodb.AttributeType.STRING,
        },
      ],
      keySchema: [
        {
          AttributeName: 'id',
          KeyType: dynamodb.KeyType.HASH,
        },
      ],
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
    });
  }
}