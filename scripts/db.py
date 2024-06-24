import os

# Read SQL file
with open('/sql/db.sql', 'r') as f:
    sql_file = f.read()

# Split the file into separate queries
sql_commands = sql_file.split(';')

for command in sql_commands:
    # Let's print each command separately
    print(command)

