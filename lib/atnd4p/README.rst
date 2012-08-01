==================
atnd4p (ATND API)
==================
:著者: Nasu Susumu
:バージョン: 0.1
:著作権: `LGPLv3`_

.. _`LGPLv3`: http://sourceforge.jp/magazine/07/09/05/017211

--------------
 0: はじめに
--------------
本ライブラリはATND APIのPythonラッパーです。 
本ライブラリを使用する事で取得した結果をPython Objectとして扱う事が出来ます。

インストール手順
^^^^^^^^^^^^^^^^^
PYTHONPATHの通っている場所に配置して下さい。

--------------------
 1: 検索APIの使い方 
--------------------
 イベントサーチAPI を実行します。::

 >>> from atnd4p import *
 >>> query = {}

 query（get_atndの第二引数）は検索条件を指定する為の辞書のオブジェクトです。検索条件として使用出来る語句はイベントサーチAPI の検索クエリのパラメータと一致します。
 一つの検索パラメータに対して、複数の値を渡す場合は、value部分を配列にしてください。::

  >>> query['keyword_or'] = ['google','cloud']
  >>> #query['event_id'] = (1,2)
  >>> query['format'] = 'json'

 get_atndの第一引数はATNDのAPIが提供しているタイプを指定します。 EVENTS: 検索 USERS: 出欠確認 です。::

  >>> atnd = get_atnd("EVENTS",query)
  >>> [event.event_id for event in atnd.events]
  [14006, 13513, 13863, 13993, 13346, 13888, 13981, 13632, 13906, 13907]

-----------------------
 2: 出欠確認APIの使い方
-----------------------
 出欠確認API を実行します。::

 >>> query = {}

 query（get_atndの第二引数）は検索条件を指定する為の辞書のオブジェクトです。
 検索条件として使用出来る語句はイベントサーチAPI の検索クエリのパラメータと一致します。
 一つの検索パラメータに対して、複数の値を渡す場合は、value部分を配列にしてください。
 
 {event_id = 1}
 
 event_id を複数渡したい場合は配列又はタプル にします。
 
 {event_id = [1,2]}
 
 {event_id = (1,2)}::

  >>> query['event_id'] = (1,2)
  >>> atnd = get_atnd("USERS",query)
  >>> [event.event_id for event in atnd.events]
  [1, 2]
  >>> [str(event.event_id) +":" + str(user.user_id) for user in event.users for event in atnd.events]
  ['1:10', '2:10', '1:45', '2:45']
 
----------------------------
 3: ATND API とのマッピング
----------------------------
ATND API のフィールド と models の 属性は 基本的に一対一の関係になります。
詳細はサーチ、出欠のレスポンスフィールドを参考にして下さい。

AtndAPIオブジェクト
^^^^^^^^^^^^^^^^^^^^

**属性**

サーチ： results_returned results_start events(AtndEventの配列)

出欠： results_returned results_start events(AtndEventの配列)

AtndEventオブジェクト
^^^^^^^^^^^^^^^^^^^^^^^

**属性**

サーチ： 各レスポンスのeventが持つフィールドと属性（名前も）が一致する。

出欠： 各レスポンスのeventが持つフィールドと属性（名前も）が一致する。

AtndUserオブジェクト
^^^^^^^^^^^^^^^^^^^^^^^

**属性**

サーチ： なし。（検索の時にはオブジェクトは使われない）

出欠： 各レスポンスのusersが持つフィールドと属性（名前も）が一致する。

--------------
 4: TODO
--------------

* パッケージ化

--------------
 5: 参考サイト
--------------

`API リファレンス`_

`atnd4r`_

`ATND4J`_

.. _`API リファレンス`: http://api.atnd.org/
.. _`atnd4r`: https://github.com/sugamasao/atnd4r
.. _`ATND4J`: http://atnd4j.sourceforge.jp/


 

