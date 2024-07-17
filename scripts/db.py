import os
import subprocess

print("Running python script..")

# Get the current branch name from the GITHUB_REF env variable
branch_name = os.getenv('GITHUB_REF').split('/')[-1]
print("Branch Name: " + branch_name)

# Get diff between the latest commit on the branch and current uncommitted changes
result = subprocess.run(['git', 'diff', '--unified=0', f'origin/{branch_name}', '../sql/db.sql'], stdout=subprocess.PIPE)
diff_output = result.stdout.decode('utf-8')
print("Diff Output: " + diff_output)

# Extract additions in the current uncommitted changes
new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]
print("Newlines fetched...")
# Print the list of newly added lines
for line in new_lines:
    print(line)
