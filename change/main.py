import requests
from utils.exception import *

class ChangeManager:
    SERVICE_NOW_URL = ""
    API_ENDPOINT = "/api/sn_chg_rest/change/standard/"
    API_VERSIONED_ENDPOINT = "/api/sn_chg_rest/{version}/change/standard/"
    __API_KEY = ""
    HEADERS = {"Accept" : "application/json", "Authorization" : "BEARER {}".format(__API_KEY)}

    def __init__(self):
        super()

    def create_cr(self, template_id=None, headers={}, params={}):
        if headers:
            self.HEADERS.update(headers)
        if not template_id:
            raise TemplateIdMissing('Template id is not passed')

        cr_url = self.SERVICE_NOW_URL + self.API_ENDPOINT + template_id
        print("CR URL: {}".format(cr_url))
        cr_response = requests.post(cr_url, headers=self.HEADERS, params=params)

        # Check for HTTP codes other than 200
        if response.status_code != 200: 
            raise CRCreationError('Status: {}, Headers: {}, Error Response: {}'.
                                  format(response.status_code, response.headers, response.content))

        return response.content

