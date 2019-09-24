import requests


def main():

    # 入力
    payload = {
        'keyid' : 'e1baa9e16a360a6cb32e16f863fe45a2',   #基本APIキーは公開厳禁(push厳禁)
        'freeword': 'ワイン',
        'hit_per_page' : 5
    }
    url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'

    # 計算（情報の取得）
    response = requests.get(url, params=payload)
    search_results = response.json()['rest']

    # 出力
    for result in search_results:    # csv(comma separated value)形式で表示
        print(f'{result["name"]}, {result["url"]}, {result["access"]["line"]}{result["access"]["station"]}')


if __name__ == '__main__':
    main()