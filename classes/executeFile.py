import os
from config import config
from classes.parseFile import ParseFile
import datetime
from classes.log import Log


class ExecuteFile():
    def __init__(self, files):
        self.input = config().get('local_settings','input_dir')
        self.output = config().get('local_settings','output_dir')
        self.files = files

    def execute_file(self):

        for file in self.files:
            full_path = self.input + file
            if os.path.isfile(full_path):
                Log().save_to_logfile("Import pliku : {}".format(full_path))
                parsed_file = ParseFile(full_path).parse_file()
                self.move_file_to_archive(file)

        return True

    def move_file_to_archive(self, file):
        now = datetime.datetime.now()
        current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        input_file = self.input+file
        output_file = self.output+current_date_time+"__"+file
        os.rename(input_file, output_file)
        Log().save_to_logfile("Przenoszenie pliku {} do {}".format(input_file, output_file))

        return True
