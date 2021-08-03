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
                    {
                        'AttributeName': 'name',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'timestamp',
                        'KeyType': 'RANGE'
                    }
                ],
                AttributeDefinitions = [
                    {
                        'AttributeName': 'name',
                        'AttributeType': 'S'
                    },
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

    #return all messages in the database
    def getMessages(self):
        try:
            messages = self.table.scan()
        except:
            return('Could not connect to database')

        return ([[m['name'], m['message'], m['timestamp']] for m in messages['Items']])

    def insertNewMessage(self, name, message):
        messageObj = {
            'message': message,
            'name': name,
            'timestamp': str(datetime.today())
        }

        try:
            self.table.put_item(Item = messageObj)
        except:
            print('Could not insert message to database')