from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings

import os

def upload_images(dirname: str, post_id: int, images: list[UploadedFile]):
    user_directory = os.path.join(settings.BASE_DIR, "media/users", dirname)

    if not os.path.exists(user_directory):
        os.makedirs(user_directory)

    saved_images = []
    tweet_id = str(post_id)

    for image in images:
        fs = FileSystemStorage(location=os.path.join(user_directory, tweet_id))
        filename = fs.save(image.name, image)
        file_url = fs.url(os.path.join(f"users/{dirname}", tweet_id, filename))
        
        saved_images.append(file_url)

    return saved_images