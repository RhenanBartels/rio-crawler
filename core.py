# coding: utf-8

import googlemaps


class Highlander:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Highlander, cls).__new__(cls,
                                                           *args,
                                                           **kwargs)

        return cls._instance


class GoogleMaps():

    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)

    def distance(self, origin, destination):
        response_driving = self._get_distance_by_mode(
            origin, destination, 'driving')

        # response_walking = self._get_distance_by_mode(
        #     origin, destination, 'walking')

        distance_driving = self._parse_response(response_driving)
        return distance_driving

    def _get_distance_by_mode(self, origin, destination, mode):
        print(origin + " ---> " + destination)
        response = self.gmaps.distance_matrix(origins=origin,
                                              destinations=destination,
                                              mode=mode)
        return response

    def _parse_response(self, response):
        rows = response.get('rows')[0]
        elements = rows.get('elements')[0]
        distance = elements.get('distance').get('text') if elements.get(
            'distance') else None
        duration = elements.get('duration').get('text') if elements.get(
            'duration') else None

        return distance, duration
