# Test
# Example: Simple Search in MrLooquer
# __Author__: Julian J. GOnzalez
# __Version__: 0.1
#
import sys
import os
sys.path.insert(0, str(os.path.dirname(
                       os.path.abspath(__file__)) +
                       os.path.sep + 'looquer' + os.path.sep))
from looquer import Mrlooquer


def show(r, q):

    for key in r:
        if key == 'numPages':
            max_page = r[key]
        if key == 'hits':
            print (('Max Page {}'.format(max_page)))
            for item in r[key]:
                print ((item['domain']))
                print ((item['port']))
                print ((item['ip']))
                if 'ip4' in list(item.keys()):
                    print ((item['ip4']))
                print ((item['date']))
                print ((item['banner']))

if __name__ == "__main__":

    try:
        print (' *********************')
        print (' Testing Mrlooquer API')
        print (' *********************')
        # You must register in mrlooquer.com to get API-KEY
        token = 'you_token_will_be_here'

        n = Mrlooquer(token)
        # Looking for info for Apache
        query = 'apache'
        n.search(query)
        r = n.raw_data()

        print ((show(r, query)))

    except Exception as e:
        import json
        print (' MrLooquer Error')
        print ('')
        if '400' in str(e):
            msg = {'Error': [{"Status": 400,
                              "QuoteExceded": "the quote exceeded"}]}
            msg = json.dumps(msg)
            print (msg)

        if '403' in str(e):
            msg = {'Error': [{"Status": 403,
                              "TokenNotValid": "the token is not valid"}]}
            msg = json.dumps(msg)
            print (msg)
