from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import boto3

app = Flask(__name__, instance_relative_config=False)
app.config.from_object(os.environ['APP_SETTINGS'])

s3 = boto3.client(
   "s3",
   aws_access_key_id=app.config['S3_KEY'],
   aws_secret_access_key=app.config['S3_SECRET']
)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format(app.config["S3_LOCATION"], file.filename)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'user_file' not in request.files:
            return "No selected file."

        file = request.files["user_file"]

        if file.filename == '':
            return "No selected file."

        if file and allowed_file(file.filename):
            file.filename = secure_filename(file.filename)
            output = upload_file_to_s3(file, app.config["S3_BUCKET"])
            return str(output)
        else:
            return "File not supported."
    else:
        return render_template("index.html")
