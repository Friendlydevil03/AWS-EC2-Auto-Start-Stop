import boto3

# Update region & instance ID
REGION = "ap-south-1" #your region
INSTANCE_IDS = ['i-0b6fda8837abee2e0']  # Replace with your EC2 instance ID

ec2 = boto3.client('ec2', region_name=REGION)

def start_instances():
    print("Starting EC2 instances...")
    ec2.start_instances(InstanceIds=INSTANCE_IDS)
    print("Instances started:", INSTANCE_IDS)

def stop_instances():
    print("Stopping EC2 instances...")
    ec2.stop_instances(InstanceIds=INSTANCE_IDS)
    print("Instances stopped:", INSTANCE_IDS)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 start-stop-ec2.py start|stop")
        exit()

    action = sys.argv[1].lower()

    if action == "start":
        start_instances()
    elif action == "stop":
        stop_instances()
    else:
        print("Invalid command. Use: start or stop")
