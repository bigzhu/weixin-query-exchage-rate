# 微信查询汇率的 python 封装

## 入参
可以参看 https://pay.weixin.qq.com/wiki/doc/api/external/jsapi_sl.php?chapter=9_15&index=10

| 值         | 说明             |
| ---        | ---              |
| appid      | 公众账号ID       |
| mch_id     | 商户号           |
| fee_type   | 参看下方货币编码 |
| date       | 日期             |
| key        | 币种             |
| sub_mch_id | 子商户号(选填)   |

| 货币编码 | 中文说明   |
|----------|------------|
| CNY      | 人民币     |
| GBP      | 英镑       |
| HKD      | 港币       |
| USD      | 美元       |
| JPY      | 日元       |
| CAD      | 加拿大元   |
| AUD      | 澳大利亚元 |
| EUR      | 欧元       |
| NZD      | 新西兰元   |
| KRW      | 韩元       |
| THB      | 泰铢       |



例子

```python
print query('wx6d5f2djfidj1d0e090e', 'djfidjfi', 'THB', '20170223', 'T5iab0cX9Xem9KP0zLUldjifdifhywEYw7')
```
