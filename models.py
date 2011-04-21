import os
import settings
from environment import loader

class SerializablePublication(object):
    """ Encapsulates serialization methods """

    def __init__(self, template_name):
        self.template_name = template_name

    def serialize(self, file_path):
        path = os.path.join(settings.OUTPUT_DIR, file_path)
        with open(path, 'w') as file:
            file.write(self.__repr__())

    def __repr__(self):
        return self._get_stream().render(settings.SERIALIZATION_METHOD)

    def _get_stream(self):
        template = loader.load(self.template_name)
        return template.generate(**self.__dict__)

class Publication(SerializablePublication):
    """ Publication that can be converted to appropriate format, ie. EPUB """
    def __init__(self, title, language, identifier, subject=None, description=None, creator=None, publisher=None,
                 date=None):
        super(Publication, self).__init__(settings.PUBLICATION_TEMPLATE)

        self.title = title
        self.language = language
        self.identifier = identifier
        self.subject = subject
        self.description = description
        self.creator = creator
        self.publisher = publisher
        self.date = date
