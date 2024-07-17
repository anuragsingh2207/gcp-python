import os
import subprocess

# Get diff between the latest commit and current uncommitted changes
result = subprocess.run(['git', 'diff', 'HEAD', '/sql/db.sql'], stdout=subprocess.PIPE)
diff_output = result.stdout.decode('utf-8')

# Extract additions in the current uncommitted changes
new_commands = [line[1:] for line in diff_output.splitlines() if line.startswith('+')]

# Read the old SQL file
with open('/sql/db.sql', 'r') as f:
    sql_file = f.read()

# Split the file into separate queries
old_commands = sql_file.split(';')

# Compare and get a list of new queries
added_queries = list(set(new_commands) - set(old_commands))

# Print the list of newly added queries
for query in added_queries:
    print(query)
