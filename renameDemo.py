import os

def rename_files_in_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if '-demo.py' in filename:
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, 'demo.py')
                os.rename(old_path, new_path)
                print(f"Renamed {old_path} to {new_path}")

if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.realpath(__file__))
    rename_files_in_directory(root_directory)
