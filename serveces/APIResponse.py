class APIResponse:
    def __init__(self, staticURL, keys):
        self.apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
        self.apikeysearch = "e7c6ca40-7e86-4c27-8e61-59d4431820ea"
        self.staticmaps = "https://static-maps.yandex.ru/1.x/?"
        self.staticgeocoder = "https://geocode-maps.yandex.ru/1.x/?"
        self.staticmapssearch = "https://search-maps.yandex.ru/v1/?"
        self.url = self.keys = self.staticURL = self.response = None
        self.update(staticURL, keys)

    def update(self, staticURL, keys):
        import requests
        from urllib.parse import urlencode
        self.staticURL = staticURL
        self.keys = keys
        if self.staticURL == "maps":
            self.staticURL = self.staticmaps
        elif self.staticURL == "search":
            self.staticURL = self.staticmapssearch
            self.keys["apikey"] = self.apikeysearch
        elif self.staticURL == "geocoder":
            self.staticURL = self.staticgeocoder
            self.keys["apikey"] = self.apikey
        self.url = self.staticURL + urlencode(keys)
        self.response = requests.get(self.url)

    def get_response(self):
        return self.response

    def get_json(self):
        return self.get_response().json()

    def get_url(self):
        return self.url

    def get_keys(self):
        return self.keys

    def get_staticURL(self):
        return self.staticURL

    def get_content(self):
        return self.response.content

    def get_coords(self, index=0):
        return self.get_toponym(index)["Point"]["pos"]

    def get_address(self, index=0):
        return self.get_toponym(index)["metaDataProperty"]["GeocoderMetaData"]["text"]

    def get_toponym(self, index=0):
        return self.get_json()["response"]["GeoObjectCollection"]["featureMember"][
            index]["GeoObject"]


