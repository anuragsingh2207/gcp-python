import os
import subprocess
import logging
import re


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
    os.chdir('../sql')

    # Get diff between latest and previous commit
    result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD^', 'db.sql'], stdout=subprocess.PIPE)
    diff_output = result.stdout.decode('utf-8')

    print("Fetching & Printing newly added DDLs...")
    
    # Combine the DDL statements into single lines
    ddl_statements = [statement.strip() for statement in diff_output.split('"""\n') if statement.strip()]

    # Print the list of newly added lines
    for statement in ddl_statements:
        print(statement)

    # remove the first three characters and last three characters which are `"""` from each DDL statement.
    ddl_statements = [ddl[3:-3] for ddl in ddl_statements]
    
    if ddl_statements:
        print("Starting execution of DDLs")
        create_tables(instance_id, database_id, ddl_statements)
    else:
        print("No new lines provided, stopping execution.")


def main():
    fetch_ddls()

if __name__ == "__main__":
    main()