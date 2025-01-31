# Setting Up Your Development Environment

This guide will help you set up your development environment, including installing essential tools, using the command line, and leveraging package managers and containerization. It also covers screen sharing in Google Meet and using Google Colab for cloud-based coding.

## Table of Contents
- [Screen Sharing in Google Meet](#screen-sharing-in-google-meet)
- [The Command Line](#the-command-line)
  - [What is the Command Line?](#what-is-the-command-line)
  - [Why Use the Command Line?](#why-use-the-command-line)
  - [Finding the Command Line](#finding-the-command-line)
  - [Common Commands](#common-commands)
  - [Absolute and Relative Paths](#absolute-and-relative-paths)
  - [Navigating Directories](#navigating-directories)
- [Setting Up Your Development Environment](#setting-up-your-development-environment)
  - [Installing VS Code](#installing-vs-code)
  - [Installing Python](#installing-python)
  - [Configuring VS Code for Python](#configuring-vs-code-for-python)
- [Package Managers](#package-managers)
- [Containerization](#containerization)
- [Google Colab](#google-colab)
- [Next Steps](#next-steps)

## Screen Sharing in Google Meet
Google Meet is the primary tool for video calls between students and mentors. You’ll often need to share your screen during calls to:

- Debug code.
- Get help with installations.
- Show your coding environment.

### Steps to Share Your Screen
#### Windows (Chrome Browser)
1. Join a Google Meet call.
2. Click **"Present now"** at the bottom.
3. Choose:
   - **Your entire screen**: Shares everything.
   - **A window**: Shares a specific application.
   - **A tab**: Shares a single Chrome tab (includes audio by default).
4. Click **"Share"**.

#### macOS
Follow this guide to enable screen sharing permissions.

## The Command Line
The command line is a text-based interface for interacting with your computer. It’s faster and more powerful than graphical interfaces (GUIs) for many tasks.

### What is the Command Line?
A text-based interface for executing commands. Available on all operating systems:

- **Windows**: Command Prompt or PowerShell.
- **macOS/Linux**: Terminal.

### Why Use the Command Line?
- **Efficiency**: Perform tasks faster than with a GUI.
- **Automation**: Write scripts to automate repetitive tasks.
- **Remote Access**: Use tools like SSH to control remote servers.
- **Advanced Control**: Access system settings and configurations not available in GUIs.

### Finding the Command Line
- **Windows**: Search for **PowerShell** or **Command Prompt** in the Start menu.
- **macOS/Linux**: Open **Terminal** from the Applications folder or search for it.

### Common Commands
| Description          | Windows (PowerShell) | macOS/Linux (Terminal) |
|----------------------|---------------------|------------------------|
| Show current directory | `pwd` | `pwd` |
| Change directory | `cd` | `cd` |
| List files | `dir` | `ls` |
| Create a directory | `mkdir` | `mkdir` |
| Remove a file/directory | `rm` | `rm` |
| Move/rename files | `mv` | `mv` |
| Copy files | `cp` | `cp` |
| Clear the screen | `cls` | `clear` |
| Exit the terminal | `exit` | `exit` |

### Absolute and Relative Paths
- **Absolute Path**: The full path from the root directory (e.g., `/home/user/docs/file.txt` or `C:\Users\Name\docs\file.txt`).
- **Relative Path**: The path relative to your current directory (e.g., `docs/file.txt` if you’re in `/home/user`).

### Navigating Directories
Use `cd` to change directories:
```sh
cd Desktop  # Navigate to the Desktop
cd ..       # Move up one level
cd ../../   # Move up two levels
```

Use `mkdir` to create a new directory:
```sh
mkdir my_folder  # Creates a folder named my_folder
```

## Setting Up Your Development Environment
Follow these steps to set up your coding environment.

### Installing VS Code
1. Download and install **VS Code**.
2. Open VS Code and install the **Python extension** from the Extensions Marketplace.

### Installing Python
1. Download and install **Python**.
2. Verify the installation:
   ```sh
   python --version  # Ensure Python 3.x is installed
   ```

### Configuring VS Code for Python
1. Open VS Code.
2. Create a new file (`Ctrl+N`) and save it with a `.py` extension.
3. Write a simple Python script:
   ```python
   print("Hello, World!")
   ```
4. Run the script by pressing `F5` or clicking **Run** in the Debug menu.

## Package Managers
Package managers simplify installing and managing software libraries.

### Common Package Managers
#### Python: `pip`
Install a package:
```sh
pip install numpy
```

#### JavaScript: `npm`
Install a package:
```sh
npm install express
```

## Containerization
Containerization tools like Docker allow you to create isolated environments for your applications.

### Why Use Docker?
- Ensures consistency across different systems.
- Simplifies dependency management.

### Installing Docker
1. Download and install **Docker**.
2. Verify the installation:
   ```sh
   docker --version
   ```

## Google Colab
Google Colab is a free cloud-based platform for running Python code, ideal for machine learning and data science projects.

### Getting Started
1. Go to **Google Colab**.
2. Create a new notebook.
3. Write and execute Python code directly in your browser.

## Next Steps
- Experiment with the command line to build confidence.
- Explore VS Code’s debugging features.
- Learn more about Docker and containerization.
- Use Google Colab for collaborative coding and machine learning projects.
