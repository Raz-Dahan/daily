#!/bin/bash

gcloud functions deploy rename-newest-object \
    --runtime python311 \
    --trigger-http \
    --allow-unauthenticated \
    --entry-point rename_newest_object \

gcloud functions deploy rename-newest-object --runtime python311 --trigger-http --allow-unauthenticated --entry-point rename_newest_object
