from schematics.types import BaseType
from schematics.transforms import blacklist

from . import MockableDictType as DictType
from .models import Model


class DebugMixin(Model):
    """Model that has a 'debug' field and a 'debug' role which allows it to be
    displayed.
    """

    debug = DictType(BaseType)

    class Options:
        roles = {
            'default': blacklist('debug'),
            'debug': blacklist()
        }