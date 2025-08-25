import os

def sort_files_by_name(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return sorted(files)

def sort_files_by_size(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return sorted(files, key=lambda f: os.path.getsize(os.path.join(directory, f)))

def sort_files_by_modified_time(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return sorted(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))

if __name__ == "__main__":
    dir_path = input("Enter directory path: ")
    print("Files sorted by name:")
    print(sort_files_by_name(dir_path))
    print("\nFiles sorted by size:")
    print(sort_files_by_size(dir_path))
    print("\nFiles sorted by last modified time:")
    print(sort_files_by_modified_time(dir_path))