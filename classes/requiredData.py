class GetRequiredDataFormFile():
    def __init__(self, line):
        self.line = line

    def get_id_and_status(self):
        line_array = self.line.split(" ")
        id = line_array[0]
        status = line_array[1]
        return [id, status]
