# README

"py-tetra" is a wrapper library of [Questetra BPM Suite](https://questetra.com/).

This package supports to "Workflow API" feature. Learn more about of Specification Workflow API, show [this document](https://online-demo-ja.questetra.net/s/swagger/index.html).

Workflow API Docs: https://online-demo-ja.questetra.net/s/swagger/index.html

## Usage

```python
import json
from pytetra.workflow import Api


api = Api(subdomain='your-tenant-subdomain' , auth=('hassaku63@example.com', 'xxxxxxxxxxxxxxxxxxxxxxxxx'))

resp = api.process_instance.list(
    criteria=json.dumps({
        'processModelInfoId': 779
    }),
    limit=1
)

print(json.dumps(resp))
# example:
# {
#   "count": 1000,
#   "processInstances": [
#     {
#       "activeTokenNodeName": [
#         "xxx"
#       ],
#       "data": null,
#       "processInstanceDebug": false,
#       "processInstanceEndDatetime": null,
#       "processInstanceId": 1234567,
#       "processInstanceIdForView": "p1234567",
#       "processInstanceInitQgroupId": 100,
#       "processInstanceInitQgroupName": "dept-foo",
#       "processInstanceInitQuserId": 100,
#       "processInstanceInitQuserName": "Alice",
#       "processInstanceSequenceNumber": 12345,
#       "processInstanceStartDatetime": "2022-04-11T11:06:36+0900",
#       "processInstanceState": "STARTED",
#       "processInstanceTitle": "Process title",
#       "processModelInfoCategory": "Legal",
#       "processModelInfoId": 779,
#       "processModelInfoName": "Workflow name",
#       "processModelVersion": 33,
#       "starred": false
#     }
#   ]
# }
```

## note

Questetra supports two authn method, "Basic" and "OAuth2". This package supports Basic authn only.

Learn more about Questetra's API: https://questetra.com/blog/questetra-api-list/
