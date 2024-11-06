"""A package to automatically generate python API package from a SPARQL endpoint VoID description."""

__version__ = "0.0.1"

from .settings import Settings, parse_settings
from .api import Api
