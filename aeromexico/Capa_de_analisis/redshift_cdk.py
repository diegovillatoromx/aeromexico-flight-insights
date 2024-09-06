import * as cdk from 'aws-cdk-lib';
import * as redshift from 'aws-cdk-lib/aws-redshift';

export class RedshiftStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Crea un cluster de Amazon Redshift
    const cluster = new redshift.Cluster(this, 'MyRedshiftCluster', {
      clusterName: 'my-redshift-cluster',
      masterUsername: 'admin',
      masterUserPassword: cdk.SecretValue.unsafePlainText('password'),
    });
  }
}