import requests
from API_KEY import API_KEY

def main():
    # 入力
    payload = {
        'keyid': API_KEY,  # 基本APIキーは公開厳禁(push厳禁)
        'freeword': 'ワイン',
        'hit_per_page': 5
    }
    url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'

    # 計算（情報の取得）
    response = requests.get(url, params=payload)
    restaurant_list = response.json()['rest']

    # 出力
    for restaurant in restaurant_list:  # csv(comma separated value)形式で表示
        name = restaurant['name']
        url = restaurant['url']
        access = restaurant['access']['line'] + restaurant['access']['station']
        print(f'{name}, {url}, {access}')


if __name__ == '__main__':
    main()
