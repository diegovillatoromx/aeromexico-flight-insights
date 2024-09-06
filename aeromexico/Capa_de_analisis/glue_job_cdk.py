import * as cdk from 'aws-cdk-lib';
import * as glue from 'aws-cdk-lib/aws-glue';

export class GlueJobStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Crea un job de AWS Glue
    const job = new glue.Job(this, 'MyGlueJob', {
      script: glue.Script.fromAsset('glue-script.py'),
      type: glue.JobType.PYTHON_SHELL,
      role: new iam.Role(this, 'MyGlueRole', {
        assumedBy: new iam.ServicePrincipal('glue.amazonaws.com'),
      }),
    });
  }
}