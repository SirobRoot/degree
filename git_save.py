import subprocess
import sys

def run_git_workflow(message):
    try:
        # 1. Add all changes
        subprocess.run(["git", "add", "."], check=True)
        # 2. Commit with your message
        subprocess.run(["git", "commit", "-m", message], check=True)
        # 3. Push to 