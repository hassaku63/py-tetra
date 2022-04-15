from typing import NamedTuple
from requests import Session
from .api_objects import (
    ProcessModel,
    ProcessInstance,
)


class BasicAuth(NamedTuple):
    email: str
    password: str


class Api(object):
    def __init__(self, subdomain: str, auth: BasicAuth) -> None:
        self._subdomain = subdomain
        self._auth = auth
        self._session = Session()
        self._session.auth = auth
        self.process_model = ProcessModel(subdomain=self._subdomain, session=self._session)
        self.process_instance = ProcessInstance(subdomain=self._subdomain, session=self._session)

    @property
    def subdomain(self):
        return self._subdomain
