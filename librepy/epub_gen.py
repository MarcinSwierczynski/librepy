"""
Classes designed to generate EPUB files
"""

__author__ = 'Marcin Swierczynski <marcin@swierczynski.net>'

import os, settings
from file_system_helper import create_dir_if_needed, generate_file_from_template

class EpubGenerator(object):
    """
    EPUB file generator.

    :ivar destination_dir: directory to generate EPUB file into
    :ivar publication: :class:`~librepy.models.Publication` object which EPUB file will be based on
    """
    
    def __init__(self, destination_dir, publication):
        self.destination_dir = os.path.join(settings.OUTPUT_DIR, destination_dir)
        create_dir_if_needed(self.destination_dir)

        self.publication = publication

    def generate_epub(self):
        """ Generates epub file structure and produce final archive """
        self._generate_mime_type()
        self._generate_meta_inf_dir()
        self._generate_ops_dir()
        self._zip_and_change_extension()

    def _generate_mime_type(self):
        """ Generate mimetype file """
        output_path = os.path.join(self.destination_dir, settings.MIMETYPE_FILE_NAME)
        with open(output_path, 'w') as file:
            file.write(settings.MIMETYPE_FILE_CONTENT)

    def _generate_meta_inf_dir(self):
        output_path = os.path.join(self.destination_dir, settings.META_INF_DIR)
        create_dir_if_needed(output_path)

        #generate container file
        generate_file_from_template(path=os.path.join(output_path, settings.CONTAINER_FILE_NAME),
                                    template_name=settings.CONTAINER_XML_TEMPLATE,
                                    context=dict(content_ops_path=os.path.join(settings.OPS_DIR,
                                                                               settings.CONTENT_OPF_FILE_NAME)))

    def _generate_ops_dir(self):
        output_path = os.path.join(self.destination_dir, settings.OPS_DIR)
        create_dir_if_needed(output_path)
        
        #generate content.opf file
        self.publication.template = settings.CONTENT_OPF_TEMPLATE
        self.publication.serialize(os.path.join(output_path, settings.CONTENT_OPF_FILE_NAME))

    def _zip_and_change_extension(self):
        pass
