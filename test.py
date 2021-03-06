import boto
import time
s3 = boto.connect_s3()

# Create a new bucket. Buckets must have a globally unique name (not just
# unique to your account).
bucket = s3.create_bucket('boto-demo-%s' % int(time.time()))

# Create a new key/value pair.
key = bucket.new_key('mykey')
key.set_contents_from_string("Hello World!")

# Sleep to ensure the data is eventually there.
time.sleep(2)

# Retrieve the contents of ``mykey``.
print key.get_contents_as_string()
'Hello World!'

# Delete the key.
key.delete()
# Delete the bucket.
bucket.delete()