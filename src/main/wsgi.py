import sentry_sdk

from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

import os
x = os.environ

def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }

    payload = (
        b"<!DOCTYPE html>"
        b"<html>"
        b"<head>"
        b"<title>Alpha</title>"
        b'<meta charset="utf-8">'
        b"</head>"
        b"<body>"
        b"<h1>Project Beta11</h1>"
        b"<hr>"
        b"<p>This is a main project.</p>"
        b"</body>"
        b"</html>"
    )
    payload = payload.format(x)

    f = payload.decode()

    h = f.replace('<p>This is a main project.</p>', '<p>This is a main project1.{}</p>').format(x)

    b = h.encode()

    payload = b


    start_response(status, list(headers.items()))

    yield payload
