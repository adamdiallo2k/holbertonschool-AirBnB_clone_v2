import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        """
        Test that the Amenity class has the correct attributes
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_name_type(self):
        """
        Test that the name attribute is of type string
        """
        amenity = Amenity()
        name_type = type(amenity.name)
        self.assertEqual(name_type, str)

    def test_str_method(self):
        """
        Test that the __str__ method returns the expected string
        """
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)


if __name__ == '__main__':
    unittest.main()
