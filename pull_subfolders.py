import os
import subprocess

# Start from the current directory
start_dir = '.'

# Iterate over all directories and subdirectories
for dirpath, dirnames, filenames in os.walk(start_dir):
    # Check if the .git directory exists
    if '.git' in dirnames:
        # Get the directory name
        dir_name = os.path.basename(dirpath)

        # Get the current branch
        branch_output = subprocess.check_output(['git', 'branch'], cwd=dirpath).decode('utf-8')
        for line in branch_output.split('\n'):
            if '*' in line:
                branch = line.strip('*').strip()
                break

        # Print the directory name and current branch
        print(f'{dir_name}: {branch}')

        # Execute git pull
        subprocess.Popen(['git', 'pull'], cwd=dirpath)
