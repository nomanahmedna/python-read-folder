import os

def list_and_save_folders(folder_path, output_file):
    # Get a list of all folders in the specified folder
    folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    # Display the list of folders
    print("List of folders:")
    for folder in folders:
        print(folder)

    # Save the list of folders to a text file
    with open(output_file, 'w') as file:
        for folder in folders:
            file.write(folder + '\n')

if __name__ == "__main__":
    # Replace 'your_folder_path' with the path of the folder you want to scan
    folder_path = 'C:/Users/User 1/Downloads'

    # Replace 'output.txt' with the desired name of the output text file
    output_file = 'output.txt'

    list_and_save_folders(folder_path, output_file)
