import os
import subprocess

print("Running python script..")

print("Listing files in current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

print("Changing directory and Listing files in current directory")
# print current working directory
print(os.getcwd())

# change directory
os.chdir('../sql/')

# print current working directory
print(os.getcwd())




# Perform git diff
# result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD', 'db.sql'], stdout=subprocess.PIPE)
# diff_output = result.stdout.decode('utf-8')

# print(diff_output)

# # Extract additions in the current uncommitted changes
# new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

# # Print the list of newly added lines
# for line in new_lines:
#     print(line)