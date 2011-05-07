"""
File system helpers.
"""

__author__ = 'Marcin Swierczynski <marcin@swierczynski.net>'

import os
from environment import loader

def create_dir_if_needed(path):
    """ Creates new directory at given location if there is no such directory """
    if not os.path.exists(path):
        os.mkdir(path)

def generate_file_from_template(path, template_name, context, render_method='xml'):
    """
    Generate file at given path using template and given context

    :param path: path where the file will be generated
    :param template_name: name of template which will be used to generate the file content.
                          It must be in templates dir configured in Genshi.
    :param context: dictionary containing values which will be injected into template slots
    :param render_method: document rendering method. See Genshi documentation.
    """

    template = loader.load(template_name)
    file_content = template.generate(**context).render(render_method)

    with open(path, 'w') as file:
        file.write(file_content)
