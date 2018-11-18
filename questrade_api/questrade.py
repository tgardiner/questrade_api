import os
import json
from datetime import datetime, timedelta, timezone
import configparser
import urllib
from questrade_api.auth import Auth

CONFIG_PATH = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'questrade.cfg')


class Questrade:
    def __init__(self, **kwargs):
        if 'config' in kwargs:
            self.config = self.__read_config(kwargs['config'])
        else:
            self.config = self.__read_config(CONFIG_PATH)
        if 'refresh_token' in kwargs:
            self.auth = Auth(
                refresh_token=kwargs['refresh_token'], config=self.config)
        elif 'token_path' in kwargs:
            self.auth = Auth(
                token_path=kwargs['token_path'], config=self.config)
        else:
            self.auth = Auth(config=self.config)

    def __read_config(self, fpath):
        config = configparser.ConfigParser()
        with open(os.path.expanduser(fpath)) as f:
            config.read_file(f)
        return config

    @property
    def __base_url(self):
        return self.auth.token['api_server'] + self.config['Settings']['Version']

    def __build_get_req(self, url, params):
        if params:
            url = self.__base_url + url + '?' + urllib.parse.urlencode(params)
            return urllib.request.Request(url)
        else:
            return urllib.request.Request(self.__base_url + url)

    def __get(self, url, params=None):
        req = self.__build_get_req(url, params)
        req.add_header(
            'Authorization',
            self.auth.token['token_type'] + ' ' +
            self.auth.token['access_token']
        )
        try:
            r = urllib.request.urlopen(req)
            return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            return json.loads(e.read().decode('utf-8'))

    def __build_post_req(self, url, params):
        url = self.__base_url + url
        return urllib.request.Request(url, data=json.dumps(params).encode('utf8'))

    def __post(self, url, params):
        req = self.__build_post_req(url, params)
        req.add_header(
            'Authorization',
            self.auth.token['token_type'] + ' ' +
            self.auth.token['access_token']
        )
        try:
            r = urllib.request.urlopen(req)
            return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            return json.loads(e.read().decode('utf-8'))

    @property
    def __now(self):
        return datetime.now().astimezone().isoformat('T')

    def __days_ago(self, d):
        now = datetime.now().astimezone()
        return (now - timedelta(days=d)).isoformat('T')

    @property
    def time(self):
        return self.__get(self.config['API']['time'])

    @property
    def accounts(self):
        return self.__get(self.config['API']['Accounts'])

    def account_positions(self, id):
        return self.__get(self.config['API']['AccountPositions'].format(id))

    def account_balances(self, id):
        return self.__get(self.config['API']['AccountBalances'].format(id))

    def account_executions(self, id, **kwargs):
        return self.__get(self.config['API']['AccountExecutions'].format(id), kwargs)

    def account_orders(self, id, **kwargs):
        if 'ids' in kwargs:
            kwargs['ids'] = kwargs['ids'].replace(' ', '')
        return self.__get(self.config['API']['AccountOrders'].format(id), kwargs)

    def account_order(self, id, order_id):
        return self.__get(self.config['API']['AccountOrder'].format(id, order_id))

    def account_activities(self, id, **kwargs):
        if 'startTime' not in kwargs:
            kwargs['startTime'] = self.__days_ago(1)
        if 'endTime' not in kwargs:
            kwargs['endTime'] = self.__now
        return self.__get(self.config['API']['AccountActivities'].format(id), kwargs)

    def symbol(self, id):
        return self.__get(self.config['API']['Symbol'].format(id))

    def symbols(self, **kwargs):
        if 'ids' in kwargs:
            kwargs['ids'] = kwargs['ids'].replace(' ', '')
        return self.__get(self.config['API']['Symbols'].format(id), kwargs)

    def symbols_search(self, **kwargs):
        return self.__get(self.config['API']['SymbolsSearch'].format(id), kwargs)

    def symbol_options(self, id):
        return self.__get(self.config['API']['SymbolOptions'].format(id))

    @property
    def markets(self):
        return self.__get(self.config['API']['Markets'])

    def markets_quote(self, id):
        return self.__get(self.config['API']['MarketsQuote'].format(id))

    def markets_quotes(self, **kwargs):
        if 'ids' in kwargs:
            kwargs['ids'] = kwargs['ids'].replace(' ', '')
        return self.__get(self.config['API']['MarketsQuotes'], kwargs)

    def markets_options(self, **kwargs):
        return self.__post(self.config['API']['MarketsOptions'], kwargs)

    def markets_strategies(self, **kwargs):
        return self.__post(self.config['API']['MarketsStrategies'], kwargs)

    def markets_candles(self, id, **kwargs):
        if 'startTime' not in kwargs:
            kwargs['startTime'] = self.__days_ago(1)
        if 'endTime' not in kwargs:
            kwargs['endTime'] = self.__now
        return self.__get(self.config['API']['MarketsCandles'].format(id), kwargs)
