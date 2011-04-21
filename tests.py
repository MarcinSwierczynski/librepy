import unittest, os
import settings
from models import Publication

class TestPublication(unittest.TestCase):
    def setUp(self):
        self.publication = Publication(title='Python Programming', language='en', identifier='MS1104')

    def test_serialization(self):
        file_name = 'publication.html'
        self.publication.serialize(file_name)

        file_path = os.path.join(settings.OUTPUT_DIR, file_name)
        with open(file_path) as file:
            self.assertTrue(self.publication.title in file.read())
