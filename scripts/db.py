import os
import subprocess

print("Running python script...")

print("Current directory:")
result = subprocess.run(["pwd"], capture_output=True, text=True)
print(result.stdout)

print("Listing files in current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

print("Changing directory to 'sql' and staying there")
os.chdir('../sql')

print("Current directory after change:")
result = subprocess.run(["pwd"], capture_output=True, text=True)
print(result.stdout)

print("Listing files in new current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)


#Perform git diff
result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD', 'db.sql'], stdout=subprocess.PIPE)
diff_output = result.stdout.decode('utf-8')

print(diff_output)

# # Extract additions in the current uncommitted changes
# new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

# # Print the list of newly added lines
# for line in new_lines:
#     print(line)