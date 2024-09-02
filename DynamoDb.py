import boto3

client = boto3.client("dynamodb", region_name = 'ap-south-1')

def create_table():

    table = client.create_table(
        TableName = 'users',
        KeySchema = [
            {
                'AttributeName':'username',
                'KeyType':'HASH'
            },
            {
                'AttributeName':'last_name',
                'KeyType':'RANGE'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName':'username',
                'AttributeType':'S'
            },
            {
                'AttributeName':'last_name',
                'AttributeType':'S'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits':5,
            'WriteCapacityUnits':5
        }
    )

    return table

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

def put_item():

    table = dynamodb.Table('users')

    response = table.put_item(
        Item={
            'username': 'Tarun',
            'first_name': 'Tarun',
            'last_name': 'sai',
            'age': 25
        }
    )

def get_item():
    table = dynamodb.Table('users')

    response = table.get_item(
        Key = {
            'username':'Tarun',
            'last_name':'sai'
        }
    )

    # print(response)
    Item = response['Item']
    print(Item)

def update_item():

    table = dynamodb.Table('users')
    table.update_item(
    Key={
        'username': 'Tarun',
        'last_name': 'sai'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
    )

def delete_key():

    table = dynamodb.Table('users')

    response = table.delete_item(
        Key = {
            'username':'Tarun',
            'lastname': 'sai'
        }
    )

if __name__ == "__main__":
    create_table()
    put_item()
    get_item()
    update_item() 
    get_item()
    delete_key()

