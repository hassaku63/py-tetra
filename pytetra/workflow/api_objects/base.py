from requests import Session


class ApiObject(object):
    BaseUrl = 'https://{}.questetra.net/'

    def __init__(self, subdomain: str, session: Session) -> None:
        self._session = session
        self._subdomain = subdomain

    @property
    def session(self):
        return self._session

    @property
    def subdomain(self):
        return self._subdomain

    @property
    def endpoint_url(self):
        return self.BaseUrl.format(self.subdomain)
