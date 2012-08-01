# -*- coding:utf-8 -*-
'''
Created on 2011/03/05

@author: nasu
'''
import json
import urllib
import urllib2
from settings import ATND_API_EVENTS_URL, ATND_API_USERS_URL, API_TYPE
from models import AtndAPI

__author__ = "Nasu Susumu (nasu@eggplant.org.uk)"
__version__ = '0.1'
__license__ = "GNU LGPL Version 3"
__all__ = ['get_atnd']

###################
# public
##################


def get_atnd(api_type_case, param={}):
    """
    この関数で ATND の結果を受け取る。
    基本的にatnd4pを使用する時はこの関数以外使用しなくて良い。
    API(ATND) オブジェクトを返却する。
    """
    if api_type_case not in API_TYPE:
        raise ATNDApiTypeError('%d:指定したAPIのタイプは存在しません。' % (api_type_case))
    atend_json = _get_json(eval("ATND_API_%s_URL" % (API_TYPE[api_type_case])),
                           _make_query(param))
    atnd = _parse_json(atend_json)
    return atnd

###################
# private
##################


def _get_json(api_url, query):
    '''
    ATND API を実行して、JSON を取得する
    '''
    try:
        response = urllib2.urlopen("%s?%s" % (api_url, query))
        #response = urllib2.urlopen(api_url, query)
        return json.load(response, 'utf-8')
        '''
        try except を使わず
        pythonのエラー処理に任せた方が逆に良いのかもしれないけど
        エラーを纏めても良いが念のため分けて書く。
        '''
    except urllib2.HTTPError, error:
        raise error
    except urllib2.URLError, error:
        raise error
    except IOError, error:
        '''
        入出力のエラーは最後に捕捉
        '''
        raise error


def _make_query(param={}):
    '''
    パラメータから urllib.urlencode を作成する。一つの Key に複数の値がある場合、カンマ区切りにする
    '''
    import re
    p = re.compile(r'^\s+$')
    param['format'] = 'json'  # formatはjson形式で固定
    cleaned_param = {}
    for key, value in param.items():
        if value:
            if (isinstance(value, list) or
                isinstance(value, tuple)):
                cleaned_param[key.strip()] = ",".join([str(v).strip() for v in value
                                                       if v and not p.search(str(v))]
                                                      )
            elif isinstance(value, str):
                cleaned_param[key.strip()] = value.strip()
            elif isinstance(value, int):
                cleaned_param[key.strip()] = value
    # ATND用に カンマをエスケープしないように urllib.always_safe を上書き
    urllib.always_safe = urllib.always_safe + ","
    return urllib.urlencode(cleaned_param)


def _parse_json(atnd_json):
    '''
    JSONデータ を ATND オブジェクトに変更する。
    '''
    # json オブジェクトにerrorキーが含まれていたらATNDParameterError
    if 'error' in atnd_json:
        raise ATNDParameterError("ATND Request Parameter Error : %s" % (atnd_json['error']['message']))
    return AtndAPI(atnd_json)

###################
#Eception
##################


class ATNDParameterError(Exception):
    """
    APIの実行結果のjosnに error キーが含まれていたら エラーを出す。
    """
    pass


class ATNDApiTypeError(Exception):
    """
    type（現状はイベント:EVENTS、出欠確認:USERS）以外の 提供していないAPIのタイプ を指定したらエラーを出す。
    """
    pass

