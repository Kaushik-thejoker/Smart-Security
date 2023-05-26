import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from loger import log

def upload_image(file_path, destination_path):
    log("cloud update begin",status=True)
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
    'storageBucket': 'smart-security-ef383.appspot.com'
    })
    try:
        bucket = storage.bucket()
        print("started")
        blob = bucket.blob(destination_path)
        blob.upload_from_filename(file_path)
        # Make the image publicly accessible (optional)
        blob.make_public()
        # Get the public URL of the image
        image_url = blob.public_url
        log(f"updated cloud link: {image_url}",status=True)
    except Exception as e:
            log(f"Error uploading image to Firebase Storage: {str(e)}", status=True)