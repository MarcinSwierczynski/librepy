import os
from environment import loader

def create_dir_if_needed(path):
    """ Creates new directory at given location if there is no such directory """
    if not os.path.exists(path):
        os.mkdir(path)

def generate_file_from_template(path, template_name, context, render_method='xml'):
    """ Generate file at given path using template and given context """
    template = loader.load(template_name)
    file_content = template.generate(**context).render(render_method)

    with open(path, 'w') as file:
        file.write(file_content)
