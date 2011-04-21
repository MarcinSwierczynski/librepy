import settings
from genshi.template.loader import TemplateLoader

loader = TemplateLoader(settings.TEMPLATES_DIRS)
