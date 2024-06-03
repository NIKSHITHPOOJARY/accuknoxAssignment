import paramiko
from scp import SCPClient
import os
from datetime import datetime

# Configuration
SOURCE_DIRECTORY = "/path/to/source/directory"
REMOTE_USER = "username"
REMOTE_HOST = "remote.server.com"
REMOTE_DIRECTORY = "/path/to/remote/directory"
LOG_FILE = "/path/to/logfile.log"

# Function to create SSH client
def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

# Function to perform the backup
def perform_backup():
    try:
        ssh = create_ssh_client(REMOTE_HOST, 22, REMOTE_USER, 'your_password')
        scp = SCPClient(ssh.get_transport())
        
        # Backup directory
        scp.put(SOURCE_DIRECTORY, recursive=True, remote_path=REMOTE_DIRECTORY)
        
        # Logging success
        with open(LOG_FILE, 'a') as log:
            log.write(f"Backup successful: {datetime.now()}\n")
        
        scp.close()
        ssh.close()
    except Exception as e:
        # Logging failure
        with open(LOG_FILE, 'a') as log:
            log.write(f"Backup failed: {datetime.now()} - {str(e)}\n")

# Perform the backup
perform_backup()
