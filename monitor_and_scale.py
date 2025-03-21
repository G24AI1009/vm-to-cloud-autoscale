# monitor_and_scale.py
import psutil
import time
import boto3
from datetime import datetime

# AWS Configuration - replace with your actual values
AMI_ID = "ami-0aa7d40eeae50c9a9"  # Ubuntu 22.04 x86_64 BIOS AMI (Mumbai region)
INSTANCE_TYPE = "t3.micro"
KEY_NAME = "your-key-name"  # replace with your key pair name
SECURITY_GROUP = "sg-xxxxxxxx"  # replace with your security group ID
REGION = "ap-south-1"

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name=REGION)

def launch_instance():
    print("Launching new AWS EC2 instance...")
    response = ec2.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SecurityGroupIds=[SECURITY_GROUP],
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'AutoScaled-Instance'}]
            }
        ]
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance {instance_id} launched at {datetime.now()}")

def monitor():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        print(f"CPU: {cpu}% | RAM: {ram}%")

        if cpu > 75 or ram > 75:
            launch_instance()
            break

        time.sleep(5)

if __name__ == "__main__":
    monitor()
