import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_ids = []

    # Get EC2 instances with tag AutoStartStop=True
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:AutoStartStop',
                'Values': ['true']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['running', 'stopped']
            }
        ]
    )

    # Collect instance IDs
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_ids.append(instance_id)

    # If no instances found
    if not instance_ids:
        print("No instances found with tag AutoStartStop=True")
        return {
            'status': 'No instances found'
        }

    # Get action from EventBridge: start or stop
    action = event.get('action', 'stop').lower()

    if action == 'start':
        ec2.start_instances(InstanceIds=instance_ids)
        print(f"Started instances: {instance_ids}")

    elif action == 'stop':
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {instance_ids}")

    else:
        print("Invalid action. Use 'start' or 'stop'.")

    return {
        'action': action,
        'instances': instance_ids
    }