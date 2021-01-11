import sentry_sdk

from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)



def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }

    environ2 = " "

    for key, value in environ.items():
        value=environ[key]
        text=f"<p>{key}: {value}</p>"
        environ2 += text

    payload = (
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Alpha</title>"
        '<meta charset="utf-8">'
        "</head>"
        "<body>"
        "<h1>Project Beta11</h1>"
        "<hr>"
        f"{environ2}"
        "</body>"
        "</html>"
    )


    start_response(status, list(headers.items()))

    yield from [payload.encode()]
