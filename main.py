from classes.openFileToImport import OpenFleToImport
from classes.executeFile import ExecuteFile
from classes.log import Log
import datetime

start = datetime.datetime.now()
Log().save_to_logfile("Start on: {}\n".format(start.strftime("%Y-%m-%d %H:%M:%S")))
file_list = OpenFleToImport().list_folder_files()
ExecuteFile(file_list).execute_file()
end = datetime.datetime.now()
Log().save_to_logfile("End on: {}\n".format(end.strftime("%Y-%m-%d %H:%M:%S")))
