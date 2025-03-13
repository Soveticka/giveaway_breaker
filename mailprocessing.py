from bs4 import BeautifulSoup

def get_email_body(email):
    soup = BeautifulSoup(email, 'html.parser')
    body = soup.find('body')
    return body.get_text()

def get_link_from_email(email):
    soup = BeautifulSoup(email, 'html.parser')
    link = soup.find('a')
    return link['href']