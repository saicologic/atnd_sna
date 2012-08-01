# -*- coding:utf-8 -*-
'''
Created on 2011/03/11

@author: nasu
'''

class Model(object):
    """
    ATNDのモデルの基底クラス
    """
    def __init__(self, json):
        for attr,value in json.items():
            setattr(self,attr,value)


class AtndUser(Model):
    '''
    ATNDのイベントの出席ユーザオブジェクトモデル ⇒ イベントに紐づく
    '''
    def __init__(self,json):
        '''
        Eventのオブジェクトを受け取り属性に設定する。
        '''
        super(AtndUser,self).__init__(json)


class AtndEvent(Model):
    '''
    ATNDのイベントオブジェクトモデル
    '''
    def __init__(self,json):
        '''
        Eventのオブジェクトを受け取り属性に設定する。 ⇒ AtndAPI に紐づく
        '''
        super(AtndEvent,self).__init__(json)
        if 'users' in json:
            users = [AtndUser(user) for user in json['users']] 
            self.users = users 


class AtndAPI(Model):
    '''
    ATND（全体）のオブジェクトモデル
    '''
    def __init__(self,json):
        '''
        ATNDのオブジェクトを受け取り属性に設定する。
        '''
        super(AtndAPI,self).__init__(json)
        if 'events' in json:
            events = [AtndEvent(event) for event in json['events']]
            self.events = events




