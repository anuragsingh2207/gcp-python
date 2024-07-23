import os
import subprocess
import logging


from google.cloud import spanner
from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
from google.cloud.spanner_v1 import DirectedReadOptions, param_types
from google.cloud.spanner_v1.data_types import JsonObject


GOOGLE_APPLICATION_CREDENTIALS=os.environ['GOOGLE_APPLICATION_CREDENTIALS']


instance_id = "demo-instance"
database_id = "demo-database"
OPERATION_TIMEOUT_SECONDS = 300

from google.api_core.exceptions import AlreadyExists

def create_tables(instance_id, database_id, new_lines):
    try:
        from google.cloud import spanner
        print("Imported library...")

        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)

        database = instance.database(database_id)
        print("Connected to database...")

        operation = database.update_ddl(new_lines)
        print("DDL statements execution started...")

        print("Waiting for operation to complete...")
        operation.result()

        print("DDL statements execution completed")
    except AlreadyExists as e:
        print("Table already exists, no changes were made.")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e


print("\nCurrent directory:")
result = subprocess.run(["pwd"], capture_output=True, text=True)
print(result.stdout)

print("\nListing files in current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

print("\nChanging directory to 'sql' and staying there")
os.chdir('../sql')

print("\nCurrent directory after change:")
result = subprocess.run(["pwd"], capture_output=True, text=True)
print(result.stdout)

print("\nListing files in new current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

# Get diff between the latest commit and the previous commit
print("\nPrint newly added lines with special character...")
result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD^', 'db.sql'], stdout=subprocess.PIPE)
diff_output = result.stdout.decode('utf-8')

# Print the diff output
print(diff_output)

print("\nListing files in new current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

print("\nPrint newly added lines...")
# Extract additions in the current uncommitted changes
new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

print(new_lines )

print("\nPrint newly added lines one at a time")
# Print the list of newly added lines
for line in new_lines:
    print(line)


# Call the create_database function
create_tables(instance_id, database_id, new_lines)