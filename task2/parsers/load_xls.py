from io import BytesIO

import requests


def load_xls_bytes(url: str) -> BytesIO:
    response = requests.get(url)
    response.raise_for_status()
    return BytesIO(response.content)