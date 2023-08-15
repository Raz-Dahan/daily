from google.cloud import storage

def delete_oldest_objects(data, context):
    bucket_name = data['bucket']
    
    # Initialize the storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    # List all objects in the bucket
    blobs = bucket.list_blobs()
    
    # Sort blobs by creation time (oldest first)
    blobs_sorted = sorted(blobs, key=lambda x: x.time_created)
    
    # Delete excess objects if there are more than 20
    excess_count = len(blobs_sorted) - 20
    if excess_count > 0:
        for blob in blobs_sorted[:excess_count]:
            blob.delete()

    print(f"Deleted {excess_count} objects from {bucket_name}.")
