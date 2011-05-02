import os, settings
from environment import loader

class EpubGenerator(object):
    """ Generates epub file structure """

    def __init__(self, destination_dir):
        self.destination_path = os.path.join(settings.OUTPUT_DIR, destination_dir)
        self._create_dir_if_needed(self.destination_path)

    def generate_epub(self):
        """ Generate EPUB file """
        self._generate_mime_type()
        self._generate_meta_inf_dir()
        self._generate_ops_dir()
        self._zip_and_change_extension()

    def _generate_mime_type(self):
        """ Generate mimetype file """
        output_path = os.path.join(self.destination_path, settings.MIMETYPE_FILE_NAME)
        with open(output_path, 'w') as file:
            file.write(settings.MIMETYPE_FILE_CONTENT)

    def _generate_meta_inf_dir(self):
        output_path = os.path.join(self.destination_path, settings.META_INF_DIR)
        self._create_dir_if_needed(output_path)

        #generate container file
        content_ops_path = os.path.join(settings.OPS_DIR, settings.CONTAINER_FILE_NAME)
        temlplate = loader.load(settings.CONTAINER_XML_TEMPLATE)
        stream = temlplate.generate(dict(content_ops_path=content_ops_path))
        #TODO save container.xml

    def _generate_ops_dir(self):
        output_path = os.path.join(self.destination_path, settings.OPS_DIR)
        self._create_dir_if_needed(output_path)

    def _zip_and_change_extension(self):
        pass

    def _create_dir_if_needed(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

