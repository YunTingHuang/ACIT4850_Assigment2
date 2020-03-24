"""This is base.py"""

import unittest
import inspect
import xmlrunner
import points_api
import os

from point_manager import PointManager

from sqlalchemy import create_engine
from base import Base

class TestPointApi(unittest.TestCase):
    """function docstring."""
    #testing

    def setUp(self):
        """function docstring."""
        engine = create_engine('sqlite:///test_points.sqlite')
        
        # Creates all the tables
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine
        points_api.point_mgr = PointManager('test_points.sqlite')
        points_api.app.testing = True
        self.app = points_api.app.test_client()
        self.logPoint()

    def tearDown(self):
        """function docstring."""

        os.remove('test_points.sqlite')
        self.logPoint()

    def logPoint(self):
        """function docstring."""

        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_points_all(self):
        """function docstring."""

        rv = self.app.get('/points/all')
        self.assertEqual(rv.status, '200 OK')
    
    def test_points_all(self):
        rv = self.app.get('/points/all')
        self.assertEqual(rv.status, '200 OK')
        
    def test_post_get_point(self):
        """function docstring."""

        rv_post = self.app.post('/points', json={"x": 5, "y": 5},
                                headers={"content-type":"application/json"})
        self.assertEqual(rv_post.status, '200 OK')
        
        rv_get = self.app.get('/points/all')
        self.assertEqual(rv_get.status, '200 OK')
        #testing

if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output='api-test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
    