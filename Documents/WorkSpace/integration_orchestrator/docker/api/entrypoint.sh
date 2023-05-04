#!/bin/bash

# Start the run once job.
echo "Docker container has been started"

crontab ./app/cron/scheduler.txt
cron -f