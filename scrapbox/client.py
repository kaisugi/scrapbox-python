from scrapbox.resource import wrapped_resource
from scrapbox.request import make_request
from functools import partial

class Client(object):
    base_url = "https://scrapbox.io/api"

    def __getattr__(self, name, **kwargs):
        if name not in ("get"):
            raise AttributeError
        return partial(self._request, name, **kwargs)

    def _request(self, method, resource, **kwargs):
        url = self._resolve_resource_name(resource)
        return wrapped_resource(make_request(method, url, kwargs))

    def _resolve_resource_name(self, name):
        name = name.rstrip("/").lstrip("/")
        return '%s/%s' % (self.base_url, name)