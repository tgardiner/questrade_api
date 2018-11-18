import os
import json
import time
from urllib import request

TOKEN_PATH = os.path.expanduser('~/.questrade.json')


class Auth:
    def __init__(self, **kwargs):
        if 'config' in kwargs:
            self.config = kwargs['config']
        else:
            raise Exception('No config supplied')
        if 'token_path' in kwargs:
            self.token_path = kwargs['token_path']
        else:
            self.token_path = TOKEN_PATH
        if 'refresh_token' in kwargs:
            self.__refresh_token(kwargs['refresh_token'])

    def __read_token(self):
        try:
            with open(os.path.expanduser(self.token_path)) as f:
                str = f.read()
                return json.loads(str)
        except IOError:
            raise('No token provided and none found at {}'.format(TOKEN_PATH))

    def __write_token(self, token):
        with open(os.path.expanduser(self.token_path), 'w') as f:
            json.dump(token, f)

    def __refresh_token(self, token):
        req_time = int(time.time())
        r = request.urlopen(self.config['Auth']['RefreshURL'].format(token))
        if r.getcode() == 200:
            token = json.loads(r.read().decode('utf-8'))
            token['expires_at'] = str(req_time + token['expires_in'])
            self.__write_token(token)

    def __get_valid_token(self):
        try:
            self.token_data
        except AttributeError:
            self.token_data = self.__read_token()
        finally:
            if time.time() + 60 < int(self.token_data['expires_at']):
                return self.token_data
            else:
                self.__refresh_token(self.token_data['refresh_token'])
                self.token_data = self.__read_token()
                return self.token_data

    @property
    def token(self):
        return self.__get_valid_token()
