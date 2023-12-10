# Utility Scripts

## Overview

This repository contains a collection of utility scripts designed to automate various tasks and streamline common processes. Each script is organized based on its intended functionality, providing a modular and organized structure for ease of use.

## Scripts

### 1. [InitGithub](init-github.py)

#### Description
The `InitGithub` script automates the initialization of a Git repository with specific configurations. It takes input parameters such as the host, repository path, repository name, Github user email, and Github user name. The script executes a series of Git commands, including initializing a new Git repository, adding a remote origin, creating a README file with a header based on the provided repository name, and staging the README file for the initial commit.

### Usage

To initialize a new GitHub repository, use the following command:

```bash
python init-github.py <path> '{"host": "github.com", "repo_path": "marcus.a/example.git", "repo_name": "example", "email": "marcus.a@example.com", "name": "Marcus Aurelius"}'
