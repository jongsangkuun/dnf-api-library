from urllib.parse import quote, quote_plus


def convert_url_encode(url: str):
    strip_url = url.strip()

    encoded_url = quote_plus(strip_url)
    return encoded_url
