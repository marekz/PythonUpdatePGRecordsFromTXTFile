from classes.testDocumentLine import TestDocumentLIne
from classes.requiredData import GetRequiredDataFormFile
from classes.dbConnect import DbConnect
from classes.dbOperations import DbOperations


class ParseFile():
    def __init__(self, file):
        self.file = file
        self.db_conn = DbConnect().conn()

    def parse_file(self):
        input_file = open(self.file)
        file_content = input_file.readlines()
        connect = DbOperations(self.db_conn)
        for line in file_content:
            line = line.strip(' \t\n\r')
            file_status = TestDocumentLIne(line).test_line()
            if file_status:
                data_record =  GetRequiredDataFormFile(line).get_id_and_status()

                record = connect.check_records(data_record)
                updateRecord = connect.update_record(record)

        self.db_conn.commit()
        self.db_conn.close()
        input_file.close()

        return True
