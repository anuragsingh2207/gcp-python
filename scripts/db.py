# import os
# import subprocess

# print("Running python script..")

# # Get diff between the latest commit and current uncommitted changes
# result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD', '../sql/db.sql'], stdout=subprocess.PIPE)
# diff_output = result.stdout.decode('utf-8')

# # Extract additions in the current uncommitted changes
# new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

# # Print the list of newly added lines
# for line in new_lines:
#     print(line)


import subprocess

print("Running python script...")


print("Print Current Directory..")
result = subprocess.run(["pwd"], capture_output=True, text=True)
print(result.stdout)

print("Listing files in Current Directory..")
result1 = subprocess.run(["pwd"], capture_output=True, text=True)
print(result1.stdout)


# Get diff between the HEAD and current state
result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD', '../sql/db.sql'], stdout=subprocess.PIPE)
diff_output = result.stdout.decode('utf-8')

# Extract additions in the current uncommitted changes
new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

# Print the list of newly added lines
for line in new_lines:
    print(line)