import json

def wrapped_resource(response):
    if "image" in response.headers['Content-Type']:
        return response.content

    response_content = response.content.decode(response.encoding or 'utf-8')

    try:
        content = json.loads(response_content)
    except ValueError:
        content = response_content

    return content
