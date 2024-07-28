import os
import subprocess
import logging
import re
import difflib


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

def get_new_sql_lines(path_to_sql_file):
    # Get unified diff for added lines
    diff_output = subprocess.check_output(
        ["git", "diff", "-U0", "HEAD~1", path_to_sql_file]
    ).decode()

    sql_commands = []
    sql_command = ""

    # Extract new SQL lines from diff
    for line in diff_output.split('\n'):
        if line.startswith('+') and not line.startswith('+++'):
            # Append line to command without the '+'
            sql_command += ' ' + line[1:].strip()

            if line.strip().endswith(';'):
                # End of command. Append to list if not empty.
                if sql_command.strip():
                    sql_commands.append(sql_command.strip())
                sql_command = ""

    # If there was no semicolon at the end of the last command append it
    if sql_command.strip():
        sql_commands.append(sql_command.strip())

    return sql_commands


def main():
    os.chdir('../sql')
    new_sql_commands = get_new_sql_lines("./db.sql")
    if new_sql_commands:
        print("Printing newly added sql lines ...")
        print(new_sql_commands)

        print("Starting execution of DDLs")
        create_tables(instance_id, database_id, new_sql_commands)
    else:
        print("No new lines provided, stopping execution.")
    

if __name__ == "__main__":
    main()