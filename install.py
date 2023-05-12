#!/usr/bin/env python3
import os
import sys

# First, check if pip is installed
try:
    import pip
except ImportError:
    print("pip is not installed. Installing pip...")
    os.system("sudo apt-get update && sudo apt-get install -y python3-pip")
    print("pip installed successfully!")
    # Exit script so the user can run it again and continue the installation process
    sys.exit()

# Install dependencies using pip
print("Installing required dependencies...")
os.system("sudo pip3 install flask flask-cors flask-ngrok")
print("Dependencies installed successfully!")

# Clone the Raspberty Server repository and enter the directory
print("Cloning Raspberty Server repository...")
os.system("git clone https://github.com/Raspberty/raspberty-server.git")
os.chdir("raspberty")
print("Repository cloned and directory entered successfully!")

# Create a virtual environment and activate it
print("Creating virtual environment...")
os.system("sudo pip3 install virtualenv")
os.system("virtualenv venv")
os.system("source venv/bin/activate")
print("Virtual environment created and activated successfully!")

# Install Raspberty Server and database
 Raspberty Server...")
os.system("pip3 install -r requirements.txt")
os.system("flask db init")
os.system("flask db migrate")
os.system("flask db upgrade")
print("Raspberty Server installed successfully!")

# Deactivate virtual environment
print("Deactivating virtual environment...")
os.system("deactivate")
print("Virtual environment deactivated successfully!")

print("Raspberty Server installation comb#!/usr/bin/env python3
import os
import sys

# First, check if pip is installed
try:
    import pip
except ImportError:
    print("pip is not installed. Installing pip...")
    os.system("sudo apt-get update && sudo apt-get install -y python3-pip")
    print("pip installed successfully!")
    # Exit script so the user can run it again and continue the installation process
    sys.exit()

# Install dependencies using pip
print("Installing required dependencies...")
os.system("sudo pip3 install flask flask-cors flask-ngrok")
print("Dependencies installed successfully!")

# Clone the Raspberty Server repository and enter the directory
print("Cloning Raspberty Server repository...")
os.system("git clone https://github.com/hoaquyingvn/raspberty.git")
os.chdir("raspberty-server")
print("Repository cloned and directory entered successfully!")

# Create a virtual environment and activate it
print("Creating virtual environment...")
os.system("sudo pip3 install virtualenv")
os.system("virtualenv venv")
os.system("source venv/bin/activate")
print("Virtual environment created and activated successfully!")

# Install Raspberty Server and database
print("Installing Raspberty Server...")
os.system("pip3 install -r requirements.txt")
os.system("flask db init")
os.system("flask db migrate")
os.system("flask db upgrade")
print("Raspberty Server installed successfully!")

# Deactivate virtual environment
print("Deactivating virtual environment...")
os.system("deactivate")
print("Virtual environment deactivated successfully!")

print("Raspberty Server installation completed!")
