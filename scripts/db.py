import os
import subprocess

print("Running python script..")


# Change directory to the location of db.sql
os.chdir('../sql/')
  
# Perform git diff
result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD', 'db.sql'], stdout=subprocess.PIPE)
diff_output = result.stdout.decode('utf-8')

print(diff_output)

# Extract additions in the current uncommitted changes
new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

# Print the list of newly added lines
for line in new_lines:
    print(line)