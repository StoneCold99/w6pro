import requests 
import requests_cache 
import json 




#setup our api cache location (this is going to make a temporary database storage for our api calls)

requests_cache.install_cache('image_cache', backend='sqlite')


def get_image(search):
    url = "https://google-search72.p.rapidapi.com/search"

    querystring = {"q":"word cup","gl":"us","lr":"lang_en","num":"10","start":"0"}

    headers = {
	"X-RapidAPI-Key": "62b42f8b2fmsh0844b3892e2a6b5p1f8354jsnbedc252a98b8",
	"X-RapidAPI-Host": "google-search72.p.rapidapi.com"
}


    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    # print(data)

    img_url = ""

    if 'items' in data.keys():
           img_url = data['items'][0]['originalImageUrl'] 

    return img_url