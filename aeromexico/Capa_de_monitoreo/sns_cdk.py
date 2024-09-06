import * as cdk from 'aws-cdk-lib';
import * as sns from 'aws-cdk-lib/aws-sns';

export class SNSStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const topic = new sns.Topic(this, 'MyTopic', {
      topicName: 'my-topic',
    });

    topic.addSubscription(new sns.EmailSubscription('example@email.com'));
  }
}