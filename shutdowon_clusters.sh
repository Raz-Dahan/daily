#!/bin/bash

gcloud container clusters delete "prod-cluster" --project "named-signal-392608" --zone "us-central1-a" --quiet &
gcloud container clusters delete "test-cluster" --project "named-signal-392608" --zone "us-east1" --quiet &