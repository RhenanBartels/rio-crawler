# coding: utf-8

from decouple import config

from core import GoogleMaps

DOWNTOWN = ["Sao Cristovao", "Benfica", "Caju", "Centro",
            "Cidade Nova", "Estacio", "Gamboa", "Lapa", "Magueira",
            "Paqueta", "Rio Comprido", "Santa Teresa", "Santo Cristo",
            "Saude", "Vasco da Gama"
            ]

SOUTH_ZONE = ["Botafogo", "Catete", "Copacabana",  "Cosme Velho", "Gavea",
              "Humaita", "Ipanema", "Jardim Botanico", "Lagoa", "Laranjeiras",
              "Leblon", "Leme", "Rocinha", "Sao Conrado", "Urca", "Vidigdal"
              ]


GOOGLE_KEY = config('GOOGLE_KEY')


def _parse_neighbours(google_maps_obj, neighbourhoods):
    for idx, origin in enumerate(neighbourhoods):
        for destination in neighbourhoods[idx + 1:]:
            distance, duration = google_maps_obj.distance(
                _prepare_neighbour_name(origin),
                _prepare_neighbour_name(destination))
            print(distance, duration, origin, destination)


def _prepare_neighbour_name(name):
    return name + ", Rio de Janeiro - State of Rio de Janeiro, Brazil"

if __name__ == "__main__":
    google_maps_obj = GoogleMaps(GOOGLE_KEY)
    all_neighbourhoods = DOWNTOWN + SOUTH_ZONE
    _parse_neighbours(google_maps_obj, all_neighbourhoods[:6])
