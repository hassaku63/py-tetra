from typing import TypedDict, Optional
from .base import ApiObject


class ProcessModel(ApiObject):
    def list(
        self,
        limit: Optional[int] = 10,
        start: Optional[int] = None,
        category: Optional[str] = None,
        query: Optional[str] = None,
        starred_only: Optional[bool] = None,
        db_file: Optional[str] = None,
    ):
        url = self.endpoint_url + 'API/Admin/ProcessModel/list'
        params = {
            'limit': limit,
            'start': start,
            'category': category,
            'query': query,
            'starred_only': starred_only,
            'db_file': db_file,
        }
        params = {k: v for k, v in params.items() if v is not None}

        resp = self.session.get(
            url=url,
            params=params,
        )
        resp.raise_for_status()

        return resp.json()
