#!/usr/bin/python3

"""
class Place inherits from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Public attributes are city_id, user_id,  name. description, number_rooms,
    number_bathrooms, max_guest, price_by_night, latitude, Longitude,
    amenity_ids
    All entities are made up of
        floats(= 0.0) which are latitude,longitude,amenity_ids
        strings (= "") which are  city_id,user_id, name, description
        integers (= 0.0) which number_rooms, number_bathrooms, max_guest,
        price_by_night
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = 0.0
