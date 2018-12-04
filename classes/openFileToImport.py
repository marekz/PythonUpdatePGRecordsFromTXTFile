import os
from config import config


class OpenFleToImport():
    def __init__(self):
        self.path = config().get('local_settings','input_dir')

    def list_folder_files(self):
        return os.listdir(self.path)
