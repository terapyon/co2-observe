import boto3

from config import DYNAMODB_TABLE


def create_table():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.create_table(
        TableName=DYNAMODB_TABLE,
        KeySchema=[
            {"AttributeName": "date", "KeyType": "HASH"},  # Partition key
            {"AttributeName": "time", "KeyType": "RANGE"},  # Sort key
        ],
        AttributeDefinitions=[
            {"AttributeName": "date", "AttributeType": "S"},
            {"AttributeName": "time", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    return table


if __name__ == "__main__":
    """
    export AWS_PROFILE=profile-name
    python create_dynamodb_table.py
    """
    table = create_table()
    print("Created table.")
