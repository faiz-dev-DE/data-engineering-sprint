#!/bin/bash
# Move into our dedicated sprint workspace directory
cd "$(dirname "$0")"

echo "=== Pipeline Cron Trigger Started ===" >> automation_log.txt
date >> automation_log.txt

# Execute our engineered Python pipeline script
python3 et1_processor.py >> automation_log.txt 2>&1

echo "=== Pipeline Execution Finished ===" >> automation_log.txt
