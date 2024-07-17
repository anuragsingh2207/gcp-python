import os
import subprocess

print("Running python script..")

# Get the branch name from GitHub environment variable
branch_name = os.getenv('GITHUB_HEAD_REF')

# If running this script locally, GITHUB_HEAD_REF will not be set. 
# Fallback to HEAD, so it still works for local testing
if not branch_name:
    branch_name = 'HEAD'

print(f"Getting diff for branch {branch_name}")

# Get diff between the latest commit of the pull request branch and current uncommitted changes
result = subprocess.run(['git', 'diff', '--unified=0', f'origin/{branch_name}', '../sql/db.sql'], 
                        stdout=subprocess.PIPE)
diff_output = result.stdout.decode('utf-8')

# Extract additions in the current uncommitted changes
new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

# Print the list of newly added lines
for line in new_lines:
    print(line)
