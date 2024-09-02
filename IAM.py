import boto3

iam_client = boto3.client("iam")

def create_user(username):
    response = iam_client.create_user(
        UserName = username
    )

    return response

def attach_user_policy(username, Arn):
    response = iam_client.attach_user_policy(
        UserName = username,
        PolicyArn = Arn
    )

    return response

def detach_user_policy(username, Arn):
    response = iam_client.detach_user_policy(
        UserName = username,
        PolicyArn = Arn
    )

    return response

def delete_user(username):
    response  = iam_client.delete_user(
        UserName = username
    )

    return response

def create_group(groupname):
    response = iam_client.create_group(
        GroupName = groupname
    )

    return response

def add_user_to_group(groupname, username):
    response = iam_client.add_user_to_group(
        GroupName = groupname,
        UserName = username
    )

    return response

def attach_group_policy(groupname, Arn):
    response = iam_client.attach_group_policy(
        GroupName = groupname,
        PolicyArn = Arn
    )

    return response

def detach_group_policy(groupname, Arn):
    response = iam_client.detach_group_policy(
        GroupName = groupname,
        PolicyArn = Arn
    )

    return response

def remove_user_from_group(group_name, user_name):
    response = iam_client.remove_user_from_group(
        GroupName = group_name,
        UserName = user_name
    )
    return response

def delete_group(groupname):
    response = iam_client.delete_group(
        GroupName =  groupname
    )

    return response

def main():
    user_1 = create_user('test1')
    user_2 = create_user('test2')
    del_user = delete_user('test2')
    group_1 = create_group('test_group_1')
    add_user = add_user_to_group('test_group_1', 'test1')
    group_2 = create_group('test_group_2')
    rm_usr = remove_user_from_group('test_group_1', 'test1')
    del_group = delete_group('test_group_2')

if __name__ == "__main__":
    main()