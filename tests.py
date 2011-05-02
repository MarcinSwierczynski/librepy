import unittest, os
from epub_gen import EpubGenerator
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

class TestEpubGenerator(unittest.TestCase):
    def setUp(self):
        destination_dir = 'test'
        self.destination_path = os.path.join(settings.OUTPUT_DIR, destination_dir)

        self.epub_generator = EpubGenerator(destination_dir)
        self.epub_generator.generate_epub()

    def test_generate_mimetype(self):
        mimetype_file_path = os.path.join(self.destination_path, settings.MIMETYPE_FILE_NAME)
        with open(mimetype_file_path) as file:
            mimetype_file_content = file.read()
            self.assertTrue(mimetype_file_content == settings.MIMETYPE_FILE_CONTENT)

    def test_generate_meta_inf_dir(self):
        meta_inf_dir_path = os.path.join(self.destination_path, settings.META_INF_DIR)
        self.assertTrue(os.path.exists(meta_inf_dir_path))
        self.assertTrue(os.path.isdir(meta_inf_dir_path))

    def test_generate_ops_dir(self):
        ops_dir_path = os.path.join(self.destination_path, settings.OPS_DIR)
        self.assertTrue(os.path.exists(ops_dir_path))
        self.assertTrue(os.path.isdir(ops_dir_path))
