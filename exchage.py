#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
参看 https://pay.weixin.qq.com/wiki/doc/api/external/jsapi_sl.php?chapter=9_15&index=10
'''
try:
    import requests
except ImportError:
    print 'you need run:'
    print 'sudo pip install requests'
    raise
import hashlib


def dictToXml(params):
    """
    """
    xml = "<xml>"
    for k, v in params.items():
        v = v.encode('utf8')
        k = k.encode('utf8')
        xml += '<' + k + '>' + v + '</' + k + '>'
    xml += "</xml>"
    return xml


def createSignature(params):
    '''
    http://mp.weixin.qq.com/wiki/17/2d4265491f12608cd170a95559800f2d.html#.E7.AC.AC.E4.BA.8C.E6.AD.A5.EF.BC.9A.E9.AA.8C.E8.AF.81.E6.9C.8D.E5.8A.A1.E5.99.A8.E5.9C.B0.E5.9D.80.E7.9A.84.E6.9C.89.E6.95.88.E6.80.A7

    1. 将参数进行字典序排序
    2. 将参数字符串拼接成一个字符串进行sha1加密
    3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
    '''
    l_params = [v for v in params.values()]
    l_params.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, l_params)
    print sha1
    signature = sha1.hexdigest()
    print signature
    return signature


def query(appid, mch_id, fee_type, date, sub_mch_id=None):
    params = locals()
    params['sign'] = createSignature(params)
    xml = dictToXml(params)
    r = requests.post("https://api.mch.weixin.qq.com/pay/queryexchagerate", verify=False, data=params)
    print r.text

if __name__ == '__main__':
    query('wxa35c0aebbd19420f', '1375346702', 'THB', '20170223', '17138771')
