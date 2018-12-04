from config import config
import datetime


class Log():
    def __init__(self):
        self.logfile = config().get('local_settings','log_file')

    def save_to_logfile(self, message):
        file = open(self.logfile, 'a')
        file.write(message+"\n")
        file.close()
        return True

    def date_now(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

