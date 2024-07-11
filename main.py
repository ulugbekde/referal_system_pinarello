import requests
import random
import string


print("Referal kodini https://pinarello-usdt.com saytidan ro'yxatdan o'ting va kodini kiriting!")
ref_id = input("Referal kodini kiriting: ")



def random_gmail():
    domains = ["@gmail.com"]
    
    letters_and_digits = string.ascii_letters + string.digits
    
    username = ''.join(random.choice(letters_and_digits) for i in range(10))
    
    domain = random.choice(domains)
    
    gmail = username + domain
    
    return gmail


while True:
    r = requests.session()
    r.get(f"https://pinarello-usdt.com/#/register?ic={ref_id}")
    url = 'https://api.pinarello-usdt.com/api/user/register?lang=en'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'cookie': 'cf_clearance=v.Xhu9ySV9faidcTKN3DP0XNWLWuPJgxN17X8anJxmE-1720703398-1.0.1.1-8UOweaNIycJB.t15GtFuWTTPb8BIdLdBhlyUAW_QP3uUHCD_RVJ32D9ChncdJb25tkRQ8z7aIKL1Ll7inG5k.w',
        'origin': 'https://pinarello-usdt.com',
        'priority': 'u=1, i',
        'referer': 'https://pinarello-usdt.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'st-ctime': '2024-07-11 21:10:33',
        'st-lang': 'en',
        'st-ttgn': 'e86c74a9ed160fba3e704f1014fbc6b8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    data = {
        "account": random_gmail(),
        "pwd": "798930110234b98bdc989b840698ade0",
        "user_type": 1,
        "code": f"{ref_id}",
        "telegram": "",
        "whatsapp": "",
        "captcha": ""
    }  

    
    response = r.post(url, headers=headers, json=data)
    if (response.status_code)==200:
        print("Muvaffaqiyatli referal qo'shildi !")
    else:
        print("Ip block yoki pochta oldin ro'yxatdan o'tgan!")
    
        
