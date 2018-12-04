import re
from config import config


class TestDocumentLIne():
    def __init__(self, line):
        self.line = line
        self.pattern = config().get('local_settings','regular_expression')

    def test_line(self):
        status = re.match(self.pattern, self.line)
        if status:
            return True
        else:
            return False