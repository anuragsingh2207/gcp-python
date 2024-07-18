import os
import subprocess

print("Running python script...")

print(" current directory")
result3 = subprocess.run(["pwd"], capture_output=True, text=True)
print(result3.stdout)

print("Listing files in current directory")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

print("Changing directory and Listing files in current directory")
command_string = "cd .. && ls -l"
result1 = subprocess.run(command_string, capture_output=True, text=True, shell=True)
print(result1.stdout)

print(" current directory")
result4 = subprocess.run(["pwd"], capture_output=True, text=True)
print(result3.stdout)


print("Again Listing files in current directory")
result2 = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result2.stdout)




# Perform git diff
# result = subprocess.run(['git', 'diff', '--unified=0', 'HEAD', 'db.sql'], stdout=subprocess.PIPE)
# diff_output = result.stdout.decode('utf-8')

# print(diff_output)

# # Extract additions in the current uncommitted changes
# new_lines = [line[1:] for line in diff_output.splitlines() if line.startswith('+') and not line.startswith('+++')]

# # Print the list of newly added lines
# for line in new_lines:
#     print(line)