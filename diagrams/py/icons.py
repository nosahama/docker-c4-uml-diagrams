from urllib.request import urlretrieve

# Use icons with the python tool
# https://diagrams.mingrammer.com/docs/getting-started/examples#rabbitmq-consumers-with-custom-nodes

RMQ_ICON = 'icon_images/rabbitmq.png'
RMQ_ICON_URL = 'https://jpadilla.github.io/rabbitmqapp/assets/img/icon.png'

SFMC_ICON = 'icon_images/sfmc.png'
SFMC_ICON_URL = 'https://www.salesforce.com/news/wp-content/uploads/sites/3/2021/05/Salesforce-logo.jpg'


def download_icon(icon_path: str, icon_url: str):
    # Download the image to be used into a Custom Node class
    urlretrieve(icon_url, icon_path)

# download_icon(SFMC_ICON, SFMC_ICON_URL)
