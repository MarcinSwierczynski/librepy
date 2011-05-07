import shutil, unittest, os
import settings
from epub_gen import EpubGenerator
from models import Publication, Item

class TestEpubGenerator(unittest.TestCase):
    def setUp(self):
        self.publication = Publication(title='Python Programming', language='en', identifier='MS1104')
        self.publication.items = [Item(id='001', file='001.html', type='application/xhtml+xml'),
                                  Item(id='cover', file='cover.png', type='image/png'),
                                  Item(id='002', file='002.html', type='application/xhtml+xml')]

        destination_dir = 'test'
        self.destination_path = os.path.join(settings.OUTPUT_DIR, destination_dir)

        #delete previous dir
        if os.path.exists(self.destination_path):
            shutil.rmtree(self.destination_path)

        self.epub_generator = EpubGenerator(destination_dir, self.publication)
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

        container_file_path = os.path.join(meta_inf_dir_path, settings.CONTAINER_FILE_NAME)
        self.assertTrue(os.path.exists(container_file_path))

        with open(container_file_path) as file:
            self.assertTrue(os.path.join(settings.OPS_DIR, settings.CONTENT_OPF_FILE_NAME) in file.read())

    def test_generate_ops_dir(self):
        ops_dir_path = os.path.join(self.destination_path, settings.OPS_DIR)
        self.assertTrue(os.path.exists(ops_dir_path))
        self.assertTrue(os.path.isdir(ops_dir_path))

        content_opf_path = os.path.join(ops_dir_path, settings.CONTENT_OPF_FILE_NAME)
        self.assertTrue(os.path.exists(content_opf_path))

        with open(content_opf_path) as file:
            content_opf = file.read()
            self.assertTrue(self.publication.title in content_opf)
            self.assertTrue(self.publication.language in content_opf)
            self.assertTrue(self.publication.identifier in content_opf)

            for item in self.publication.items:
                self.assertTrue(item.id in content_opf)
                self.assertTrue(item.file in content_opf)
                self.assertTrue(item.type in content_opf)
