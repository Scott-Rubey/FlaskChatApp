import boto3
from datetime import datetime

class dynamo():
    def __init__(self):
        self.database = boto3.resource('dynamodb', region_name = 'us-east-1')
        self.table = self.database.Table('chatMessages')

        #attempt to load the table from dynamodb
        try:
            self.table.load()
        #if table not found, create one
        except:
            self.database.create_table(
                TableName = 'chatMessages',
                KeySchema = [
                    #{
                    #    'AttributeName': 'message',
                    #    'KeyType': 'HASH'
                    #},
                    {
                        'AttributeName': 'timestamp',
                        'KeyType': 'RANGE'
                    }
                ],
                AttributeDefinitions = [
                    #{
                    #    'AttributeName': 'message',
                    #    'AttributeType': 'S'
                    #},
                    {
                        'AttributeName': 'timestamp',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput = {
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1
                }
            )

    def getMessages(self):
        try:
            messages = self.table.scan()
        except:
            return('Could not connect to database')

        return ([[m['timestamp'], m['message']] for m in messages['Items']])

    #TODO: implement POST...where?...look at sign.py
    def insertNewMessage(self, message):
        messageObj = {
            'timestamp': str(datetime.today()),
            'message': message
        }

        try:
            self.table.put_item(Item = messageObj)
        except:
            return False

        return True