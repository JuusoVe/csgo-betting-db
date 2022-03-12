from os import getenv
import boto3
import uuid

# Create SQS client
sqs = boto3.client(
    "sqs",
    region_name="eu-central-1",
    aws_access_key_id="AKIAQH4F5HTKJXT6VQWK",
    aws_secret_access_key="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",
)

queue_url = (
    "https://sqs.eu-central-1.amazonaws.com/016923835604/csgo-betting-db-tasks.fifo"
)


async def add_scrape_to_queue(resource, id):
    """Adds a scrape task to AWS SQS queue. Prints the response MessageId on success.

    Parameters:
        resource (str): The type of resource to scrape, ie. "team"
        id (int): ID to identify the resource within the type ie. "1234" for hltv_id

    Returns:
        response (Response): SQS Response
    """

    print("in function add_scrape_to_queue")
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageAttributes={
            "Type": {"DataType": "String", "StringValue": resource},
            "ID": {"DataType": "Number", "StringValue": id},
        },
        MessageBody=("Scrape request for resource " + resource + " with ID: " + id),
        MessageGroupId="hltv_scrape",
        MessageDeduplicationId=str(uuid.uuid4()),
    )
    print("Message added to queue, received id: " + response["MessageId"])
    return response
