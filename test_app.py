import unittest
import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import db, setup_db, Location, Clothes
from app import app


class CsrpTests(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        setup_db(self.app)

        # Import environment variables
        self.DATABASE_URL = os.environ.get('DATABASE_URL')
        self.TOKEN_REC = os.environ.get('TOKEN_REC')
        self.TOKEN_PSY = os.environ.get('TOKEN_PSY')

        # Define headers for authorization
        self.header_rec = [
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.TOKEN_REC}')
            ]
        self.header_psy = [
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.TOKEN_PSY}')
            ]

        # A test new location
        self.new_location = {
            'name': 'test location 4'
        }

        # A test updated location
        self.update_location = {
            'name': 'updated location'
        }

        # A test new piece of clothing
        self.new_clothes = {
            'location': '5',
            'category': 'new shirt',
            'description': 'new color'
        }

        # A test update piece of clothing
        self.update_clothes = {
            'location': '5',
            'category': 'updated shirt',
            'description': 'updated color'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # recreate all tables
            self.db.create_all()

    def tearDown(self):
        pass

    ##########
    # Get '/'
    ##########
    def test_homepage(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_login(self):
        res = self.client().get('/login')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    ##########
    # Get '/locations'
    ##########
    def locations_list_rec(self):
        # access '/locations' with recorder token
        res = self.client().get(
            '/locations',
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def locations_list_psy(self):
        # access '/locations' with psych token
        res = self.client().get(
            '/locations',
            headers=self.header_psy
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def locations_list_401(self):
        # access '/locations' without a token
        res = self.client().get('/locations')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    ##########
    # Post '/locations'
    ##########
    def locations_add_rec(self):
        # add location as recorder
        res = self.client().post(
            '/locations',
            json=self.new_location,
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def locations_add_401(self):
        # access '/locations' with psych token
        res = self.client().post(
            '/locations',
            json=self.new_location,
            headers=self.header_psy
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def locations_add_422(self):
        # try to add a repeating location
        res = self.client().post(
            '/locations',
            json=self.new_location,
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    ##########
    # Get '/locations/<location_id>'
    ##########
    def locations_one_rec(self):
        # access '/locations' with recorder token
        res = self.client().get(
            '/locations/5',
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ##########
    # Patch '/locations/<location_id>'
    ##########
    def locations_update_rec(self):
        # update location as recorder
        res = self.client().patch(
            '/locations/12',
            json=self.update_location,
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def locations_update_422(self):
        # forget to put location info
        res = self.client().patch(
            '/locations/12',
            json={},
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    ##########
    # Delete '/locations/<location_id>'
    ##########
    def locations_delete_rec(self):
        # delete location as recorder
        res = self.client().delete(
            '/locations/12',
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def locations_update_422(self):
        # delete non existing location
        res = self.client().delete(
            '/locations/1200',
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    ##########
    # Get '/Clothes'
    ##########
    def clothes_list_rec(self):
        # access '/clothes' as recorder
        res = self.client().get(
            '/clothes',
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ##########
    # Post '/clothes'
    ##########
    def clothes_add_rec(self):
        # add clothes as recorder
        res = self.client().post(
            '/clothes',
            json=self.new_clothes,
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def clothes_add_422(self):
        # try to add bad information
        res = self.client().post(
            '/clothes',
            json={
                'category': ''
            },
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    ##########
    # Patch '/clothes'
    ##########
    def clothes_update_rec(self):
        # update clothes as recorder
        res = self.client().patch(
            '/locations/12',
            json=self.update_clothes,
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ##########
    # Delete '/locations'
    ##########
    def clothes_delete_rec(self):
        # delete clothes as recorder
        res = self.client().delete(
            '/clothes/12',
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def clothes_update_422(self):
        # delete non existing clothes
        res = self.client().delete(
            '/clothes/1200',
            headers=self.header_rec
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)


if __name__ == '__main__':
    unittest.main()
