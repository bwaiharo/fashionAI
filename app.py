from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import boto3
from config import S3_BUCKET,S3_KEY,S3_SECRET
from filters import datetimeformat, file_type

app = Flask(__name__)
Bootstrap(app)
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type

s3 = boto3.resource(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET
)

#list all the buckets currently available
for bucket in s3.buckets.all():
    print(bucket.name)



@app.route('/')
def index():
    return render_template("index.html")
    # return 'Hello There'

@app.route('/files')
def files():
    s3_resource = boto3.resource('s3')
    # my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket = s3_resource.Bucket('mushroommushroomboomboom')
    summaries = my_bucket.objects.all()

    return render_template('files.html', my_bucket=my_bucket, files=summaries)

if __name__ == "__main__":
    app.run()