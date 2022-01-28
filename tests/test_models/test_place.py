#!/usr/bin/python3
"""Test class Place"""

import models
import unittest
from models.place import Place


class Test_place(unittest.TestCase):
    """Simple test model"""

    def test_attr(self):
        """Test class attrbute"""
        is_attr = False
        list_ = [
            'city_id', 'user_id',
            'name', 'description',
            'number_rooms', 'number_rooms',
            'number_bathrooms', 'max_guest',
            'price_by_night', 'latitude',
            'longitude', 'amenity_ids'
            ]
        for key in list_:
            attr = hasattr(Place, key)
            if not attr:
                break
        self.assertEqual(attr, True)

    def test_type_str(self):
        """Test type of class attribute"""

        scity_id = type(Place.city_id).__name__
        suser_id = type(Place.user_id).__name__
        sname = type(Place.name).__name__
        sdescription = type(Place.description).__name__
        inumber_rooms = type(Place.number_rooms).__name__
        inumber_bathrooms = type(Place.number_bathrooms).__name__
        imax_guest = type(Place.max_guest).__name__
        fprice_by_night = type(Place.price_by_night).__name__
        flatitude = type(Place.latitude).__name__
        flongitude = type(Place.longitude).__name__
        lamenity_ids = type(Place.amenity_ids).__name__

        self.assertEqual(scity_id, 'str')
        self.assertEqual(suser_id, 'str')
        self.assertEqual(sname, 'str')
        self.assertEqual(sdescription, 'str')
        self.assertEqual(inumber_rooms, 'int')
        self.assertEqual(inumber_bathrooms, 'int')
        self.assertEqual(fprice_by_night, 'int')
        self.assertEqual(imax_guest, 'int')
        self.assertEqual(flatitude, 'float')
        self.assertEqual(flongitude, 'float')
        self.assertEqual(lamenity_ids, 'list')
