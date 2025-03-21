## 一、赛题概述

**用户数据D：tianchi_mobile_recommend_train_user**

在2014.11.18~2014.12.18内用户的购买行为

|     特征      |           字段说明           |                          提取说明                          | 缺失值 |
| :-----------: | :--------------------------: | :--------------------------------------------------------: | ------ |
|    user_id    |            用户id            |                 抽样&字段脱敏（非真实ID）                  | 0      |
|    item_id    |            商品id            |                    字段脱敏（非真实ID）                    | 0      |
| behavior_type |     用户对商品的行为类型     | 包括浏览、收藏、加购物车、购买，对应取值分别是1、2、3、4。 | 0      |
| user_geohash  | 用户位置的空间标识，可以为空 |                 由经纬度通过保密的算法生成                 | 68.3%  |
| item_category |         商品分类标识         |                    字段脱敏（非真实ID）                    | 0      |
|     time      |           行为时间           |                       精确到小时级别                       | 0      |

数据尺寸：12256906 * 6

数据类型：dataframe



**商品数据P：tianchi_mobile_recommend_train_item**

后台中存在的可购买的商品子集

|     特征      |           字段说明           |          提取说明          | 缺失值 |
| :-----------: | :--------------------------: | :------------------------: | ------ |
|    item_id    |           商品标识           | 抽样&字段脱敏（非真实ID）  | 0      |
| item_ geohash | 商品位置的空间标识，可以为空 | 由经纬度通过保密的算法生成 | 67.2%  |
| item_category |         商品分类标识         |    字段脱敏（非真实ID）    | 0      |

数据尺寸：480723 * 3

数据类型：dataframe

**提交目标**

对D中所有用户，预测其在2014.12.19购买的P中商品（一件）的数据。输出结果包含两列，分别是user_id和item_id, 以tab分隔。





## *一些可复用的函数

**plot_value_counts:** 对df对象的指定一列进行统计数目并按value升序plot出来

改进：现在只能指定一个，可以改进一下变成支持输入任意个列并输出任意个图，并且都是排列好的