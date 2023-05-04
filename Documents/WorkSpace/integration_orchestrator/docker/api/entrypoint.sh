#!/bin/bash
# Start the run once job.
echo "Docker container has been started"
pwd
crontab ./app/cron/scheduler.txt
crond -f