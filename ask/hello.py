def app(environ, start_response):
    """Simplest possible application object"""
    res = 'You are at hello app'
    #res = '\n'.join(environ['QUERY_STRING'].split('&'))
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [bytes(res, encoding='utf-8')]