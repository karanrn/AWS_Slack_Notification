import requests
import json


def lambda_handler(event, context):
    # TODO implement
    webhook_url = 'https://hooks.slack.com/services/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'
    
    sns_data = json.loads(event["Records"][0]["Sns"]["Message"])
    slack_data = {}
    slack_data["text"] = sns_data["AlarmName"]
    data = "*AlarmDescription*: " + sns_data["AlarmDescription"] + "\n"
    data = data + "*AWSAccountId*: " + sns_data["AWSAccountId"] + "\n"
    data = data + "*Region*: " + sns_data["Region"] + "\n"
    data = data + "*StateChangeTime*: " + sns_data["StateChangeTime"] + "\n"
    
    if(len(sns_data["Trigger"]["Dimensions"])):
        data = data + "*Dimensions*: " + "\n"
        data = data + ">*name*: " + sns_data["Trigger"]["Dimensions"][0]["name"] + "\n"
        data = data + ">*value*: " + sns_data["Trigger"]["Dimensions"][0]["value"] + "\n"
        
    data = data + "*MetricName*: " + sns_data["Trigger"]["MetricName"] + "\n"
    data = data + ">*Statistic*: " + sns_data["Trigger"]["Statistic"] + "\n"
    data = data + ">*ComparisonOperator*: " + sns_data["Trigger"]["ComparisonOperator"] + "\n"
    data = data + ">*Period*: " + str(sns_data["Trigger"]["Period"]) + "\n"
    data = data + ">*Threshold*: " + str(sns_data["Trigger"]["Threshold"])
    
    slack_data["attachments"] = [
        {
            "color": "#FF0000",
            "text": data
        }
    ]

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    
    
    # if response.status_code != 200:
    #     raise ValueError(
    #         'Request to slack returned an error %s, the response is:\n%s'
    #         % (response.status_code, response.text)
    #     )
    
