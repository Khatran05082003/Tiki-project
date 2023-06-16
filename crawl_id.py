import requests
import pandas as pd
import time
import random
from tqdm import tqdm

cookies = {
    "_trackity": "875b2ce4-212f-5cce-04d9-cc6ec84bf2f7",
    "_gcl_au": "1.1.793529080.1679215808",
    "_fbp": "fb.1.1679215808224.1068958507",
    "__uidac": "f163acf12945398651d700901d47bd14",
    "__RC": "5",
    "__R": "3",
    "_hjSessionUser_522327": "eyJpZCI6ImQ0MWUxODRkLTgzMzYtNWQ1Zi1hMmJiLWFhZGYyY2JmMWZmYiIsImNyZWF0ZWQiOjE2NzkyMTU4MDg0ODUsImV4aXN0aW5nIjp0cnVlfQ==",
    "__tb": "0",
    "__IP": "1906395470",
    "TOKENS": "{%22access_token%22:%22l6HVuhRjUtfPKE2A8iZIL0Dwb4xYazs5%22}",
    "delivery_zone": "Vk4wMTgwMTAwMDg=",
    "_gid": "GA1.2.1511626058.1686905968",
    "tiki_client_id": "774354415.1679215804",
    "_hjIncludedInSessionSample_522327": "0",
    "_hjSession_522327": "eyJpZCI6ImFjMjkwNDY1LTgyOGQtNDlmYy1iYTI1LTgwMzkwOWNhODUwOSIsImNyZWF0ZWQiOjE2ODY5MDU5NzE5MjgsImluU2FtcGxlIjpmYWxzZX0=",
    "_hjAbsoluteSessionInProgress": "0",
    "__iid": "749",
    "__su": "0",
    "amp_99d374": "Bdfp1skWNI3tqexv6d9H87...1h31msihq.1h31mvvnd.k.18.1s",
    "_ga": "GA1.2.774354415.1679215804",
    "_gat": "1",
    "cto_bundle": "7pSnfl9hWnFWSnkxRXRYMGNnJTJCUkZGbVpsNWI4R0FyV05XeEc4U1V4bWcyTU1USSUyRnhrY2pWYXNWYXJSRTRCQzluMkFoRzNGRSUyQmVaejIyM0slMkJHNWxJcHZoZVRkYWQ1cSUyQmgyN1JXcDcxV212NFpxaFJhSEdCZHpPOHVYdWNPZktDRWx0OCUyRjA1NG9yV2JadERyeFFxT09pJTJCY0hnQSUzRCUzRA",
    "__uif": "__uid%3A1607895402883714693%7C__ui%3A-1%7C__create%3A1640789540",
    "_ga_GSD4ETCY1D": "GS1.1.1686905971.3.1.1686906087.4.0.0",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789',
    'x-guest-token': 'l6HVuhRjUtfPKE2A8iZIL0Dwb4xYazs5',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'limit': '40',
    'include': 'advertisement',
    'aggregations': '2',
    'trackity_id': '875b2ce4-212f-5cce-04d9-cc6ec84bf2f7',
    'category': '2549',
    'page': '1',
    'urlKey':  'do-choi-me-be',
}

list=['do-choi-me-be','dien-thoai-may-tinh-bang','lam-dep-suc-khoe','dien-gia-dung','thoi-trang-nu','thoi-trang-nam','giay-dep-nu','tui-vi-nu','giay-dep-nam','tui-thoi-trang-nam','balo-va-vali','phu-kien-thoi-trang','dong-ho-va-trang-suc','laptop-may-vi-tinh-linh-kien','nha-cua-doi-song','cross-border-hang-quoc-te','bach-hoa-online','thiet-bi-kts-phu-kien-so','voucher-dich-vu','o-to-xe-may-xe-dap','nha-sach-tiki','dien-tu-dien-lanh','the-thao-da-ngoai','may-anh','san-pham-tai-chinh-bao-hiem']
list2=[2549,1789,1520,1882,931,915,1703,976,1686,27616,6000,27498,8371,1846,1883,17166,4384,1815,11312,8594,8322,4221,1975,1801,54042]
df=pd.DataFrame({'urlkey':list,'category':list2})


for i in range(len(df)):
    params['category']=df['category'][i]
    params['urlKey']=df['urlkey'][i]
    product_id=[]
    j=1
    while True:
        try:
            params['page']=j
            response=requests.get('https://tiki.vn/api/personalish/v1/blocks/listings',headers=headers,params=params,cookies=cookies)
            if response.status_code==200:
                for record in response.json().get('data'):
                    product_id.append({'id':record.get('id')})
            j+=1
        except:
            break
        if j==10:
            break
    df_id=pd.DataFrame(product_id)
    df_id.to_csv("C:/Users/ACER/Downloads/id/product_id{}.csv".format(i),index=False)