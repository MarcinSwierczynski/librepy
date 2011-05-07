import os
import settings
from environment import loader

class SerializablePublication(object):
    """ Encapsulates serialization methods """

    def __init__(self, template):
        self.template = template

    def serialize(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.__repr__())

    def __repr__(self):
        return self._get_stream().render(settings.SERIALIZATION_METHOD)

    def _get_stream(self):
        template = loader.load(self.template)
        return template.generate(**self.to_dict())

    def to_dict(self):
        """ Returns dict with all values necessary for template """
        return self.__dict__

class Publication(SerializablePublication):
    """ Publication that can be converted to appropriate format, ie. EPUB """

    def __init__(self, title, language, identifier, subject=None, description=None, creator=None, publisher=None,
                 date=None, items=None):
        self.title = title
        self.language = language
        self.identifier = identifier
        self.subject = subject
        self.description = description
        self.creator = creator
        self.publisher = publisher
        self.date = date
        self.items = items

    def to_dict(self):
        values = super(Publication, self).to_dict()
        values['text_items'] = self._get_text_items()
        return values

    def _get_text_items(self):
        return [item for item in self.items if item.type=='application/xhtml+xml']

class Item(SerializablePublication):
    """ Part of the publication. Can be XHTML (ex. chapter text), image (ex. cover) or CSS style. """
    def __init__(self, id, file, type, content=None):
        super(Item, self).__init__(settings.TEXT_ITEM_TEMPLATE)

        self.id = id
        self.file = file
        self.type = type
        self.content = content
