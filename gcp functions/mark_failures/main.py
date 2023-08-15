from google.cloud import storage

def rename_newest_object(request):
    bucket_name = "chart-packages"
    extension = ".tgz"

    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()
    zipped_blobs = [blob for blob in blobs if blob.name.endswith(extension)]

    newest_blob = max(zipped_blobs, key=lambda x: x.updated)

    new_name = "FAILURE-" + newest_blob.name
    new_blob = bucket.rename_blob(newest_blob, new_name)

    print(f"Renamed {newest_blob.name} to {new_blob.name}")

    return "Function executed successfully"
