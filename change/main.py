import requests
import os
import json
from utils.exception import *

class ChangeManager:
    SERVICE_NOW_URL = ""
    API_ENDPOINT = "/api/sn_chg_rest/change/standard/"
    API_VERSIONED_ENDPOINT = "/api/sn_chg_rest/{version}/change/standard/"
    __API_KEY = ""
    HEADERS = {"Accept" : "application/json", "Authorization" : "BASIC {}".format(__API_KEY)}

    def __init__(self, env):
        self.env = env
        self.templates_file = '{}_templates.json'.format(env)
        super()

    def get_template_id(self, template_name):
        template_id = None
        template_fields = dict()
        if os.path.exists(self.templates_file):
            templates = load_json(self.templates_file)
        else:
            template_fetch_url = ''.join(self.SERVICE_NOW_URL,
                                         self.API_ENDPOINT,
                                         'template?sysparm_query=active=true^ORDERBYnumber')
            response = requests.get(template_fetch_url, headers=self.HEADERS)

            # Check for HTTP codes other than 200
            if response.status_code != 200: 
                raise CRCreationError('Status: {}, Headers: {}, Error Response: {}'.
                                    format(response.status_code, response.headers, response.content))
            templates = response.content
            dump_json(templates, self.templates_file)
        for result in templates['result']:
            if 'template' in result and 
                result['template']['display_value'] == template_name:
                template_id = result['template']['value']
                template_fields = result.keys()
                template_fields.remove('template')
                template_fields.remove('sys_id')

        return {'template_id': template_id, 'template_fields': template_fields}

    def create_cr(self, template_name=None, headers={}, params={}):
        if headers:
            self.HEADERS.update(headers)
        
        tdata = self.get_template_id(template_name)
        template_id = tdata['template_id']
        template_fields = tdata['template_fields']
        if not template_id:
            raise TemplateIdMissing('Template id is not found')

        cr_url = self.SERVICE_NOW_URL + self.API_ENDPOINT + template_id
        print("CR URL: {}".format(cr_url))
        cr_response = requests.post(cr_url, headers=self.HEADERS, params=params)

        # Check for HTTP codes other than 200
        if response.status_code != 200: 
            raise CRCreationError('Status: {}, Headers: {}, Error Response: {}'.
                                  format(response.status_code, response.headers, response.content))

        return response.content

def load_json(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def dump_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file)

