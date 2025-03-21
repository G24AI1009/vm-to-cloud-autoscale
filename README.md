This project implements an automated scaling mechanism that monitors a local Ubuntu Virtual Machine (VM) for CPU and RAM usage. When usage exceeds 75%, it automatically deploys an AWS EC2 instance using the Boto3 SDK. The EC2 instance can optionally run a Flask application, demonstrating seamless scalability and load distribution.

Prerequisites:

AWS Account: Ensure you have an active AWS account.​
AWS CLI: Install and configure the AWS Command Line Interface.​
Python 3.6+: Ensure Python is installed on your local machine.​
Boto3 and Psutil: Install these Python libraries using pip.

Setup Instructions:

1. Clone the Repository:
   git clone https://github.com/your-username/vm-to-cloud-autoscale.git
   cd vm-to-cloud-autoscale

2. Create and Activate Virtual Environment:
   python3 -m venv myenv
   source myenv/bin/activate

3. Install Dependencies:
   pip install -r requirements.txt

4. Configure AWS Credentials:
   aws configure

5. Provide your AWS Access Key, Secret Key, and default region when prompted.

6. Update Script with AWS Details:

   Open monitor_and_scale.py.​
  
   Replace placeholders with your AMI ID, Key Pair Name, Security Group ID, and desired AWS region.

7. Run the Monitoring Script:
   python monitor_and_scale.py

8. Optional: Deploy Flask Application on EC2
   To deploy a Flask application on the newly launched EC2 instance:

9. Edit User Data Script: Modify user_data_script.sh to include your Flask application setup.​

10. Ensure Script Execution: The monitor_and_scale.py script reads user_data_script.sh and passes it as user data during EC2 
    instance launch.

11. Testing the Setup: yes > /dev/null &

12. Terminate CPU Load Simulation: killall yes




