import * as cdk from 'aws-cdk-lib';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';

export class CloudWatchStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const logGroup = new logs.LogGroup(this, 'MyLogGroup', {
      logGroupName: 'my-log-group',
      retention: logs.RetentionDays.ONE_WEEK,
    });

    const alarm = new cloudwatch.Alarm(this, 'MyAlarm', {
      alarmName: 'my-alarm',
      comparisonOperator: cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
      evaluationPeriods: 1,
      metricName: 'CPUUtilization',
      namespace: 'AWS/EC2',
      period: cdk.Duration.minutes(5),
      statistic: cloudwatch.Statistic.SUM,
      threshold: 70,
    });
  }
}