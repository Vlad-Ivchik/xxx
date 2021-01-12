import random

import sentry_sdk

from framework.dirs import DIR_SRC
from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

def url_processor(path_info):
    urls = {
        'index': home,
        'environ': environment
    }
    return urls[path_info]


def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }
    payload = url_processor(environ["PATH_INFO"])

    start_response(status, list(headers.items()))

    yield payload.encode()

def read_template(template_name: str) -> str:
    dir_templates = DIR_SRC / "main" / "templates"
    template = dir_templates / template_name

    assert template.exists() and template.is_file()

    with template.open("r") as fd:
        content = fd.read()

        return  content


def home():
    template = read_template("index.html")

    random_number = random.randint(-100, 100)
    payload = template.format(
        random_number=random_number,
    )
    return payload


def environment(environ):
    environ2 = " "
    for key, value in environ.items():
        text = f"<tr><td>{key}</td><td>{value}</td></tr>"
        environ2 += text
    template = read_template("index.html")

    payload = template.format(
        environ=environ2,
    )
    return payload
