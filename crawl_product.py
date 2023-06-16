import requests
import pandas as pd
import time
import random
from tqdm import tqdm
import numpy as np


cookies = {
  "_trackity": "875b2ce4-212f-5cce-04d9-cc6ec84bf2f7",
  "_gcl_au": "1.1.793529080.1679215808",
  "_fbp": "fb.1.1679215808224.1068958507",
  "__uidac": "f163acf12945398651d700901d47bd14",
  "__RC": "5",
  "__R": "3",
  "_hjSessionUser_522327": "eyJpZCI6ImQ0MWUxODRkLTgzMzYtNWQ1Zi1hMmJiLWFhZGYyY2JmMWZmYiIsImNyZWF0ZWQiOjE2NzkyMTU4MDg0ODUsImV4cXVlfQ==",
  "__tb": "0",
  "__IP": "1906395470",
  "TOKENS": "{\"access_token\":\"l6HVuhRjUtfPKE2A8iZIL0Dwb4xYazs5\"}",
  "_gid": "GA1.2.1511626058.1686905968",
  "_hjSession_522327": "eyJpZCI6ImFjMjkwNDY1LTgyOGQtNDlmYy1iYTI1LTgwMzkwOWNhODUwOSIsImNyZWF0ZWQiOjE2ODY5MDU5NzE5MjgsImluU2FtcGxlIjpmYWxzZX0=",
  "_hjAbsoluteSessionInProgress": "0",
  "__iid": "749",
  "__su": "0",
  "delivery_zone": "Vk4wMzkwMDYwMDE=",
  "tiki_client_id": "774354415.1679215804",
  "_hjIncludedInSessionSample_522327": "0",
  "amp_99d374": "Bdfp1skWNI3tqexv6d9H87...1h31q5ut9.1h31r1brn.1a.2k.3u",
  "_ga": "GA1.1.774354415.1679215804",
  "__uif": "__uid%3A1607895402883714693%7C__ui%3A-1%7C__create%3A1640789540",
  "cto_bundle": "zCBANF9hWnFWSnkxRXRYMGNnJTJCUkZGbVpsNVVKOUdQRE1IdWNMWVZ0UDdSbzg5QkV4NHQwd3hmdVFBTlNMbjE0RmwxdTZ0WUIwSENiNWdSaGtDbEtVSElhJTJGQWJyanVDNnhhTmw2dEdlN0JYR2FLSUlmJTJGcldVVDY1Y09VODM1NGNKZzZtUjNUM1R1YVV2S0NkWmdUVmhtJTJGc0MxUSUzRCUzRA",
  "_gat": "1",
  "_ga_GSD4ETCY1D": "GS1.1.1686909427.4.1.1686910516.60.0.0",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://tiki.vn/may-tinh-bang-samsung-galaxy-tab-s6-lite-2022-4gb-64gb-sm-p615-da-kich-hoat-bao-hanh-dien-tu-hang-chinh-hang-p203949614.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.216226_Y.1798546_Z.3602913_CN.Tab-s6-Lite&itm_medium=CPC&itm_source=tiki-ads&spid=203949620',
    'x-guest-token': 'l6HVuhRjUtfPKE2A8iZIL0Dwb4xYazs5',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'platform': 'web',
    'spid': '203949620',
}

def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['sku'] = json.get('sku')
    d['short_description'] = json.get('short_description')
    d['price'] = json.get('price')
    d['list_price'] = json.get('list_price')
    d['price_usd'] = json.get('price_usd')
    d['discount'] = json.get('discount')
    d['discount_rate'] = json.get('discount_rate')
    d['review_count'] = json.get('review_count')
    d['order_count'] = json.get('order_count')
    d['inventory_status'] = json.get('inventory_status')
    d['is_visible'] = json.get('is_visible')
    d['stock_item_qty'] = json.get('stock_item').get('qty')
    d['stock_item_max_sale_qty'] = json.get('stock_item').get('max_sale_qty')
    d['product_name'] = json.get('meta_title')
    d['brand_id'] = json.get('brand').get('id')
    d['brand_name'] = json.get('brand').get('name')
    d['quantity_sold']=json.get('quantity_sold').get('value')
    d['rating_average']=json.get('rating_average')
    return d

list=['do-choi-me-be','dien-thoai-may-tinh-bang','lam-dep-suc-khoe','dien-gia-dung','thoi-trang-nu','thoi-trang-nam','giay-dep-nu','tui-vi-nu','giay-dep-nam','tui-thoi-trang-nam','balo-va-vali','phu-kien-thoi-trang','dong-ho-va-trang-suc','laptop-may-vi-tinh-linh-kien','nha-cua-doi-song','cross-border-hang-quoc-te','bach-hoa-online','thiet-bi-kts-phu-kien-so','voucher-dich-vu','o-to-xe-may-xe-dap','nha-sach-tiki','dien-tu-dien-lanh','the-thao-da-ngoai','may-anh','san-pham-tai-chinh-bao-hiem']
list2=[2549,1789,1520,1882,931,915,1703,976,1686,27616,6000,27498,8371,1846,1883,17166,4384,1815,11312,8594,8322,4221,1975,1801,54042]
df=pd.DataFrame({'urlkey':list,'category':list2})


for i in range(25):
    df_id = pd.read_csv("C:/Users/ACER/Downloads/id/product_id{}.csv".format(i))
    p_ids = df_id.id.to_list()

    results=[]
    for pid in tqdm(p_ids,total=len(p_ids)):
        reponse=requests.get('https://tiki.vn/api/v2/products/{}'.format(pid),headers=headers,params=params,cookies=cookies)
        if reponse.status_code==200:
            try:
                results.append(parser_product(reponse.json()))
            except:
                p_ids.remove(pid)
                continue
    df_product=pd.DataFrame(results)
    df_product['category_type']=df['urlkey'][i]
    df_product['category_id']=df['category'][i]
    df_product.to_csv("C:/Users/ACER/Downloads/product/product_data{}.csv".format(i),index=False)

