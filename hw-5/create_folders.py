import os

PARENT_DIR = os.path.join(os.getcwd(), 'test_folders')


def create_dirs(count: int) -> None:
    """Create need count folders"""
    for dir_number in range(1, count + 1):
        path = os.path.join(PARENT_DIR, f'dir_{dir_number}')
        os.mkdir(path)
        print(f'Dir {dir_number} was created')


def delete_dirs():
    """Delete all dirs in current folder"""
    for folder in os.listdir(PARENT_DIR):
        path = os.path.join(PARENT_DIR, folder)
        print(path)
        if os.path.isdir(path) and path != os.path:
            os.rmdir(path)
