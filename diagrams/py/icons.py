from urllib.request import urlretrieve

RMQ_ICON = "icon_images/rabbitmq.png"
RMQ_ICON_URL = "https://jpadilla.github.io/rabbitmqapp/assets/img/icon.png"


def download_icon(icon_path: str, icon_url: str):
    # Download the image to be used into a Custom Node class
    urlretrieve(icon_url, icon_path)
