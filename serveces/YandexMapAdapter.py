from serveces.APIResponse import APIResponse
from serveces.IMapService import IMapService


class YandexMapAdapter(IMapService):
    def get_map(self, longitude, latitude, zoom):
        return APIResponse("maps", dict(ll=str(longitude) + ',' + str(latitude),
                                       z=zoom,
                                       l="map")).get_content()
