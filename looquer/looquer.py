"""
Copyright 2015 Julian J. Gonzalez | SVTCloudSecurity
www.st2labs.com | @ST2Labs | @rhodius | @seguridadxato2

__Author__: Julian J. GOnzalez
__Version__: 0.1


This is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

This is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along it; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

MSOC Manager & Security Team at @SVTCloud
www.svtcloud.com
"""

import json
import requests


class Mrlooquer(object):

    def __init__(self, auth_token=None,
                                endpoint='https://mrlooquer.com/api/v1'):
        self.endpoint = endpoint
        self.session = requests.Session()
        self.session.headers = {
            'content-type': 'application/json',
            'accept': 'application/json',
        }
        self.fdata = {}
        self.query = '?q='
        self.page = '&page='
        self.result = ''
        if auth_token:
            self.token = '&token=' + auth_token

    def get(self, method, params=None):
        r = self.session.get(self.endpoint + method, params=params)
        r.raise_for_status()
        return r

    def post(self, method, params, headers=None):
        r = self.session.post(self.endpoint + method, data=json.dumps(params),
                                                             headers=headers)
        r.raise_for_status()
        return r

    def search(self, q, num_page="1"):
        self.query += q
        self.page += num_page
        r = self.get('/search' + self.query + self.token + self.page)
        self.result = r.json()

    def raw_data(self):
        return self.result
