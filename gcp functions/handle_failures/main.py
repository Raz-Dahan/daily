from google.cloud import storage

def handle_failures(data, context):
    bucket_name = data['bucket']
    
    # Initialize the storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    # List all objects in the bucket
    blobs = bucket.list_blobs()
    
    # Sort blobs by creation time (newest first)
    blobs_sorted = sorted(blobs, key=lambda x: x.time_created, reverse=True)
    
    # Keep track of the count of failure files
    failure_count = 0
    
    # Iterate through the sorted blobs
    for blob in blobs_sorted:
        if blob.name.startswith('FAILURE-'):
            failure_count += 1
            
            # If more than five failures, delete the oldest ones
            if failure_count > 5:
                blob.delete()
                print(f"Deleted failure: {blob.name}")
    
    # Record the current failure if applicable
    failed_package = data['name']
    if failed_package.startswith('FAILURE-'):
        failure_blob = bucket.blob(failed_package)
        failure_blob.upload_from_string('Failure recorded.')
        print(f"Failure recorded for package: {failed_package}")
