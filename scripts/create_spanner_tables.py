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

def create_tables(instance_id, database_id, ddl):
    """Creates a database and tables for sample data."""
    try:
        from google.cloud.spanner_admin_database_v1.types import \
        spanner_database_admin

        print("Setting up connection with Spanner...")
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api

        request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=ddl      
    )
       
        operation = database_admin_api.update_database_ddl(request)
            
        print("Waiting for operation to complete...")
        database = operation.result(OPERATION_TIMEOUT_SECONDS)

        print("Executed DDLs on database {} on instance {}".format(
            database_id, instance_id
            )
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

def fetch_ddls():
    # print("\nCurrent directory:")
    # result = subprocess.run(["pwd"], capture_output=True, text=True)
    # print(result.stdout)

    # print("\nListing files in current directory")
    # result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    # print(result.stdout)

    # print("\nChanging directory to 'sql' and staying there")
    os.chdir('../sql')

    # print("\nCurrent directory after change:")
    # result = subprocess.run(["pwd"], capture_output=True, text=True)
    # print(result.stdout)

    # print("\nListing files in new current directory")
    # result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    # print(result.stdout)

    # Get diff between the latest commit and the previous commit
    result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD^', 'db.sql'], stdout=subprocess.PIPE)
    diff_output = result.stdout.decode('utf-8')

    # Print the diff output
    # print(diff_output)

    # print("\nListing files in new current directory")
    # result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    # print(result.stdout)

    print("\Fetching & Printing newly added DDLs")
    # Extract additions in the current uncommitted changes
    new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

    # Print the list of newly added lines
    for line in new_lines:
        print(line)

    if new_lines:
        print("Starting execution of DDLs")
        create_tables(instance_id, database_id, new_lines)
    else:
        print("No new lines provided, stopping execution.")

def main():
    fetch_ddls()

if __name__ == "__main__":
    main()