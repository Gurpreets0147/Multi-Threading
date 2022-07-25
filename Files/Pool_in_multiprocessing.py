from multiprocessing import Pool
import requests
import json

def f(n):
    return n*n


if __name__ == "__main__":



    url = "https://sampark.kochar.com:81/sync/get_user_info/token/sampark12345"

    payload = ""
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    array = [1000000000000000000, 263256435645364,
             37867764365434, 76347876478437434, 654566545667544755]
    p = Pool()
    result = p.map(f, array)
    print(result)
