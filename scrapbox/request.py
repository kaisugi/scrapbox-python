import requests
import scrapbox

def make_request(method, url, params):
    request_func = getattr(requests, method, None)
    if request_func is None:
        raise TypeError('Unknown method: %s' % (method,))

    kwargs = {
        'headers': {
            'User-Agent': scrapbox.USER_AGENT
        }
    }
    params = dict(params, **kwargs)

    result = request_func(url, params)
    return result