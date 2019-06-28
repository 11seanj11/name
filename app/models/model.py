import requests

def get_names(gender=None, region='united+states'):
    url = 'https://uinames.com/api/?amount=500&region='+region
    if gender is not None:
        url = url + '&gender='+gender
    response = requests.get(url)
    if response.status_code == 200:
        # print(response.content)
        return response.json()

    
    
def get_gif(name='sean'):
    url = 'https://api.giphy.com/v1/gifs/search?api_key=Cb01mHtidS7XtdfmMocBYVOG6T5c8C74&q='+name+'&limit=25&offset=0&rating=G&lang=en'
    # print(url)
    # url = 'http://api.giphy.com/v1/gifs/search/?api_key=Cb01mHtidS7XtdfmMocBYVOG6T5c8C74&q='+name
    res = requests.get(url)
    
    if res.status_code == 200:
        if len(res.json()['data']) == 0:
            return [{
                'images': {
                    'fixed_width': {
                        'url': 'https://media0.giphy.com/media/xT8qAXAERiWiL17OYU/200w.gif?cid=64d256715d1506a54455345141c56cbd&rid=200w.gif'
                    }
                }
            }]
        else:
            return res.json()['data']
    else:
        return [{
            'images': {
                'fixed_width': {
                    'url': 'https://media0.giphy.com/media/xT8qAXAERiWiL17OYU/200w.gif?cid=64d256715d1506a54455345141c56cbd&rid=200w.gif'
                }
            }
        }]