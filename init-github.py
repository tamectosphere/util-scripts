import json
import os
import subprocess
import sys

def wait_for_enter():
    input("Press Enter to continue...")

def run_command(command):
    print(f"Running command: {command}")

    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"Command output: {e.output}")

class InitGithub:
    def run(self, context):
        host = context.get("host")
        repo_path = context.get("repo_path")
        repo_name = context.get("repo_name")

        run_command("git init")
        run_command(f"git remote add origin git@{host}:{repo_path}") 
        run_command(f'echo "# {repo_name}" >> README.md')
        run_command("git add README.md")
        wait_for_enter()

class ConfigGithubUser:
    def run(self, context):
        email = context.get("email")
        name = context.get("name")

        run_command(f"git config user.email {email}")
        run_command(f"git config user.name {name}")
        wait_for_enter()

class PushTheFirstCommit:
    def run(self, _):
        run_command("git add .")
        run_command('git commit -m "Initial commit"')
        run_command("git branch -M main")
        run_command("git push -u origin main")

def get_context(context_str):
    try:
        return json.loads(context_str)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(1)

def main(context_str):
    context = get_context(context_str)

    procedure = [InitGithub, ConfigGithubUser, PushTheFirstCommit]

    for step in procedure:
        step().run(context)

    print("Done!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            'Usage: init-github.py <path> \'{"host": "github.com", "repo_path": "marcus.a/example.git", "repo_name": "example", "email": "marcus.a@example.com", "name": "Marcus Aurelius"}\''
        )
        sys.exit(1)

    cwd = os.getcwd()
    path = sys.argv[1]

    print(f"{cwd}/{path}")

    try:
        os.chdir(f"{cwd}/{path}")
        main(sys.argv[2])

    except OSError as e:
        print(f"Error changing directory: {e}")