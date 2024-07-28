import os
import subprocess
import logging
import re
import difflib
from colorama import Fore


from google.cloud import spanner
from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
from google.cloud.spanner_v1 import DirectedReadOptions, param_types
from google.cloud.spanner_v1.data_types import JsonObject


GOOGLE_APPLICATION_CREDENTIALS=os.environ['GOOGLE_APPLICATION_CREDENTIALS']


instance_id = "demo-instance"
database_id = "demo-database"
OPERATION_TIMEOUT_SECONDS = 300

from google.api_core.exceptions import AlreadyExists

#To be Tested 
def create_tables(instance_id, database_id, ddl):
    """Creates a database and tables for sample data."""
    try:
        from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

        print(Fore.MAGENTA + "Waiting for operation to complete...")
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api

        database_path = database_admin_api.database_path(spanner_client.project, instance_id, database_id)
        
        current_ddl = database_admin_api.get_database_ddl(request={"database": database_path}).statements

        for stmt in ddl:
            table_name = stmt.split()[2]  # Assumes the ddl statement is `CREATE TABLE table_name (columns etc.)`
            if any(table_name in cur_stmt for cur_stmt in current_ddl):
                print(Fore.YELLOW + f"Table `{table_name}` already exists, skipping creation.")
                continue  # Skip this ddl statement

            request = spanner_database_admin.UpdateDatabaseDdlRequest(database=database_path, statements=[stmt])
            operation = database_admin_api.update_database_ddl(request)

           
            operation.result(OPERATION_TIMEOUT_SECONDS)

            print(Fore.GREEN + f"Executed DDL on table `{table_name}` on database {database_id} on instance {instance_id}")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise e


def get_new_sql_lines(path_to_sql_file):
    # Get previous version of file
    previous_version = subprocess.check_output(["git", "show", "HEAD:"+path_to_sql_file]).decode().split('\n')

    # Get current version of file
    with open(path_to_sql_file, "r") as file:
        current_version = file.readlines()

    d = difflib.Differ()
    diff = d.compare(previous_version, current_version)

    new_lines = []

    # Extract new lines from diff
    for line in diff:
        if line.startswith('+ '):
            # Append line to new_lines without the '+ '
            new_lines.append(line[2:])

    # Join new lines together into a single string, and return
    return ''.join(new_lines)


def main():
    os.chdir('../sql')
    new_sql_commands = get_new_sql_lines("./db.sql")
    if new_sql_commands:
       
        # Split the commands into a list of DDL statements
        ddl_statements = [stmt.strip() for stmt in new_sql_commands.split(';') if stmt.strip()]  # Discard the last split as it will be an empty string

        print(Fore.CYAN + "Starting execution of DDLs...")
        create_tables(instance_id, database_id, ddl_statements)
    else:
        print(Fore.RED + "Empty SQL file, stopping execution.")
    

if __name__ == "__main__":
    main()