# AWS_Slack_Notification
Slack integration with AWS for Cloudwatch alarms via SNS topic

# Function lamdba_handler 
It is lambda function which posts requests recieved from SNS topic.

webhook_url is http link that connects to slack.
https://api.slack.com/incoming-webhooks

The program is for Cloudwatch alarms to be sent to Slack.

All the alarms will be sent to SNS topics and above code should created as lambda in AWS.
And we need to add lambda as subscriber to SNS topics.
https://docs.aws.amazon.com/sns/latest/dg/welcome.html

And now whenever Cloudwatch alarm is triggered we get alarms as notifications in Slack.

