from typing import Optional, Literal
from .base import ApiObject


class ProcessInstance(ApiObject):
    def list(
        self,
        criteria: Optional[str],
        reportId: Optional[Literal["PROCESS_INSTANCE_STARTED"]] = None,
        limit: Optional[int] = None,
        strat: Optional[int] = None,
    ):
        """API/OR/ProcessInstance/list

        :param criteria: https://questetra.zendesk.com/hc/ja/articles/360002481031-XML-Criteria-for-Process-Instance-Search
        :param reportId: _description_, defaults to None
        :param limit: _description_, defaults to None
        :param strat: _description_, defaults to None
        """
        url = self.endpoint_url + 'API/OR/ProcessInstance/list'
        params = {
            'criteria': criteria,
            'reportId': reportId,
            'limit': limit,
            'strat': strat,
        }
        params = {k: v for k, v in params.items() if v is not None}

        resp = self.session.get(
            url=url,
            params=params,
        )
        resp.raise_for_status()

        return resp.json()
