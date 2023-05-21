import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from loger import log
def upload_image(file_path, destination_path):
    log("cloud update bugin",status=True)
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
    'storageBucket': 'test-b5fb1.appspot.com'
    })
    bucket = storage.bucket()
    print("started")
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)
    # Make the image publicly accessible (optional)
    blob.make_public()
    # Get the public URL of the image
    image_url = blob.public_url
    log(f"updated cloud link: {image_url}",status=True)