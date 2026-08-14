import os

# Get the current working directory
current_directory = '/vinci'
print(f"Current Directory: {current_directory}")

# List all files and folders in the current directory
print("\nContents of the directory:")
for item in os.listdir(current_directory):
    print(item)
