import os


def check_path(path: str):
    if not os.path.isabs(path):
        path = os.path.abspath(path)
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            return path
        except Exception as exc:
            print(f'{exc.__class__.__name__}: {exc}')
    return path
