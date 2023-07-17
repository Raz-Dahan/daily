#!/bin/bash

gcloud compute instances delete "test" --zone "us-central1-a" --project "named-signal-392608" --quiet &
gcloud container clusters delete "nasa-cluster" --project "named-signal-392608" --zone "us-central1-a" --quiet &
echo DONE.