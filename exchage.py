#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
https://pay.weixin.qq.com/wiki/doc/api/external/jsapi_sl.php?chapter=9_15&index=10
'''
try:
    import requests
except ImportError:
    print 'you need run:'
    print 'sudo pip install requests'
    raise
from hashlib import md5
import xmltodict

import six


def toText(value, encoding='utf-8'):
    """将 value 转为 unicode，默认编码 utf-8

    :param value: 待转换的值
    :param encoding: 编码
    """
    if not value:
        return ''
    if isinstance(value, six.text_type):
        return value
    if isinstance(value, six.binary_type):
        return value.decode(encoding)
    return six.text_type(value)


def dictToXml(params):
    """
    """
    xml = "<xml>"
    for k, v in params.items():
        v = v.encode('utf8')
        k = k.encode('utf8')
        xml += '<%s><![CDATA[%s]]></%s>' % (k, v, k)
    xml += "</xml>"
    return xml


def createSign(api_key, params):
    """
    create by bigzhu at 16/02/10 15:13:12 生成签名，用于微信支付
    """
    # 将键值对转为 key1=value1&key2=value2
    key_az = sorted(params.keys())
    pair_array = []
    for k in key_az:
        v = params.get(k, '').strip()
        v = v.encode('utf8')
        k = k.encode('utf8')
        pair_array.append('%s=%s' % (k, v))

    stringA = '&'.join(pair_array)

    stringSignTemp = stringA + '&key=' + api_key  # api_key, API密钥，需要在商户后台设置
    return (md5(stringSignTemp).hexdigest()).upper()


def query(appid, mch_id, fee_type, date, key, sub_mch_id=None):
    params = locals()
    if sub_mch_id is None:
        del params['sub_mch_id']
    key = params.pop('key')
    # params['sign'] = createSign('Rlym2016YM9999999999999999999999', params)
    params['sign'] = createSign(key, params)
    xml = dictToXml(params)
    r = requests.post("https://api.mch.weixin.qq.com/pay/queryexchagerate", data=xml, stream=True)
    text = r.raw.read()
    print text
    msg = xmltodict.parse(toText(text))['xml']

if __name__ == '__main__':
    pass
