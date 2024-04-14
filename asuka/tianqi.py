import requests
from tools.tianqi.utils.const_value import API,KEY,UNIT,LANGUAGE
from tools.tianqi.utils.helper import getLocation

def get_tianqi(chengshi):
    result = requests.get(API, params={
        'key': 'Sd_WJ4DWwg0jB3Wr4',
        'location': chengshi,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=1)
    return result.text

if __name__ == '__main__':
    location = getLocation()
    result = get_tianqi("西宁")
    print(result)
