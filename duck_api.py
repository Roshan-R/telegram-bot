
import requests
import re
import json


def search(keywords, max_results=None, index=0):
    """ Searches through duckduckgo and returns image result at index """

    url = 'https://duckduckgo.com/';
    params = {
    	'q': keywords
    };

    """  First make a request to above URL, and parse out the 'vqd'
       This is a special token, which should be used in the subsequent request """
    res = requests.post(url, data=params)
    
    searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M|re.I);

    if not searchObj:
        # logger.error("Token Parsing Failed !");
        return -1;

    headers = {
        'authority': 'duckduckgo.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-dest': 'empty',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://duckduckgo.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = (
        ('l', 'us-en'),
        ('o', 'json'),
        ('q', keywords),
        ('vqd', searchObj.group(1)),
        ('kp', '-2'),
        ('f', ',,,'),
        ('p', '-1'),
        ('v7exp', 'a'),
    )

    request_url = url + "i.js";

    data = ""
    
    while True:
        try:
            res = requests.get(request_url, headers=headers, params=params);
            data = json.loads(res.text);
            break;
        except ValueError as e:
            print(str(e))
            # logger.debug("Hitting Url Failure - Sleep and Retry: %s", requestUrl);
            continue;


    return(data["results"][index]["image"])

