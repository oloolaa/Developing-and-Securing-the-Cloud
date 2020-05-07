# [A File Uploader Based on AWS](https://github.com/oloolaa/Developing-and-Securing-the-Cloud "S3 Uploader")

## Introuction
This is an AWS file uploader for securing the uploaded data in AWS. The application is build by Flask, so you can run these commands under the project's root directory to boot up the application:

```bash
$ export FLASK_APP=app.py
$ flask run
```

## Application Diagram
[![](https://raw.githubusercontent.com/oloolaa/Developing-and-Securing-the-Cloud/master/Application%20Diagram.png "Application Diagram")](https://raw.githubusercontent.com/oloolaa/Developing-and-Securing-the-Cloud/master/Application%20Diagram.png "Application Diagram")


## The parameters
The application builds the connection with the credentials from AWS, so it is recommended to put credentials into a Bash script. Here are the parameters needed to run the application:

```bash
#!/bin/bash

export APP_SETTINGS='<Your setting object>'
export SECRET_KEY='<Optional. This is the secret key for sessions>'
export S3_BUCKET='<Your AWS S3 bucket name>'
export S3_KEY='<Your AWS access key id>'
export S3_SECRET_ACCESS_KEY='<Your AWS secret access key>'
export FLASK_ENV=production
export FLASK_APP=app.py
flask run
```

## References
1. Amazon Web Services (AWS) - Cloud Computing Services: https://aws.amazon.com/
2. Flask | The Pallets Projects: https://palletsprojects.com/p/flask/
3. AWS SDK for Python (Boto3): https://aws.amazon.com/sdk-for-python/
4. Signing AWS API requests - AWS General Reference: https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html
5. AWS Lambda function handler in Python - AWS Lambda:
https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
6. Event message structure - Amazon Simple Storage Service:
https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html
7. AWS Elastic Beanstalk – Deploy Web Applications:
https://aws.amazon.com/elasticbeanstalk/
8. AWS Key Management Service concepts - AWS Key Management Service: https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys
9. AWS Lambda – FAQs: https://aws.amazon.com/lambda/faqs/#AWS_Lambda_functions
