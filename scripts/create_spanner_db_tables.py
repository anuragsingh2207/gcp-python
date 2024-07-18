import os
import subprocess
import argparse
import base64
import datetime
import decimal
import json
import logging
import time

from google.cloud import spanner
from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
from google.cloud.spanner_v1 import DirectedReadOptions, param_types
from google.cloud.spanner_v1.data_types import JsonObject


OPERATION_TIMEOUT_SECONDS = 240

print("Running python script...")

print("Current directory:")
result = subprocess.run(["pwd"], capture_output=True, text=True)
print(result.stdout)

print("Listing files in current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

print("Changing directory to 'sql' and staying there")
os.chdir('../sql')

print("Current directory after change:")
result = subprocess.run(["pwd"], capture_output=True, text=True)
print(result.stdout)

print("Listing files in new current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)


# Get diff between the latest commit and the previous commit
print("Print newly added lines with special character...")
result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD^', 'db.sql'], stdout=subprocess.PIPE)
diff_output = result.stdout.decode('utf-8')

# Print the diff output
print(diff_output)

print("Listing files in new current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)


print("Print newly added lines...")
# Extract additions in the current uncommitted changes
new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

# Print the list of newly added lines
for line in new_lines:
    print(line)

instance_id="demo-instance"
database_id="demo-database"


def create_database(instance_id, database_id):
    """Creates a database and tables for sample data."""
    from google.cloud.spanner_admin_database_v1.types import \
        spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.CreateDatabaseRequest(
        parent=database_admin_api.instance_path(spanner_client.project, instance_id),
        create_statement=f"CREATE DATABASE `{database_id}`",
        extra_statements=new_lines
    )

    operation = database_admin_api.create_database(request=request)

    print("Waiting for operation to complete...")
    database = operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created database {} on instance {}".format(
            database.name,
            database_admin_api.instance_path(spanner_client.project, instance_id),
        )
    )