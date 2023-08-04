import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()

    def test_id_is_string(self):
        """
        Test that id is a string
        """
        self.assertIsInstance(self.base.id, str)

    def test_created_at_is_datetime(self):
        """
        Test that created_at is a datetime object
        """
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test that updated_at is a datetime object
        """
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test that save() updates the updated_at attribute
        """
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_to_dict_returns_dict(self):
        """
        Test that to_dict() returns a dictionary
        """
        dict_obj = self.base.to_dict()
        self.assertIsInstance(dict_obj, dict)

    def test_to_dict_has_expected_keys(self):
        """
        Test that to_dict() returns a dictionary with the expected keys
        """
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        dict_obj = self.base.to_dict()
        self.assertCountEqual(dict_obj.keys(), expected_keys)

    def test_to_dict_id_is_str(self):
        """
        Test that the 'id' key in to_dict() is a string
        """
        dict_obj = self.base.to_dict()
        self.assertIsInstance(dict_obj['id'], str)

    def test_to_dict_created_at_is_str(self):
        """
        Test that the 'created_at' key in to_dict() is a string
        """
        dict_obj = self.base.to_dict()
        self.assertIsInstance(dict_obj['created_at'], str)

    def test_to_dict_updated_at_is_str(self):
        """
        Test that the 'updated_at' key in to_dict() is a string
        """
        dict_obj = self.base.to_dict()
        self.assertIsInstance(dict_obj['updated_at'], str)

    def test_to_dict_has_classname(self):
        """
        Test that the '__class__' key in to_dict() has the expected value
        """
        dict_obj = self.base.to_dict()
        self.assertEqual(dict_obj['__class__'], 'BaseModel')

    def test_str_method(self):
        """
        Test that the __str__ method returns the expected string
        """
        base = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(str(base), expected_str)

    def test_init_kwargs(self):
        """
        Test that __init__ correctly sets attributes using **kwargs
        """
        id_val = str(uuid.uuid4())
        time_val = datetime.utcnow()
        kwargs = {'id': id_val, 'created_at': time_val, 'updated_at': time_val}
        base = BaseModel(**kwargs)
        self.assertEqual(base.id, id_val)
        self.assertEqual(base.created_at, time_val)
        self.assertEqual(base.updated_at, time_val)


if __name__ == '__main__':
    unittest.main()
