__version__ = '0.5.0'
__all__ = ['Client']

USER_AGENT = 'Scrapbox Python API Wrapper %s' % __version__

from scrapbox.client import Client