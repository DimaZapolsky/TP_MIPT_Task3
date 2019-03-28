from classes import PlayingField
from classes import DireArmyFactory
from classes import RadiantArmyFactory
import unittest


class TestSingleton(unittest.TestCase):
    def test_field_size(self):
        field = PlayingField(20, 20)
        self.assertEqual(len(field.get_field()), 20)
        self.assertEqual(len(field.get_field()[0]), 20)

    def test_instance(self):
        field1 = PlayingField(2, 2)
        field1.get_field()[0][0] = 10
        field2 = PlayingField(2, 2)
        self.assertEqual(field1.get_field()[0][0], field2.get_field()[0][0])


class TestingFactorie(unittest.TestCase):
    def test_dire_cannon(self):
        obj = DireArmyFactory().create_cannon()
        self.assertEqual(str(obj), 'Dire cannon')

    def test_radiant_cannon(self):
        obj = RadiantArmyFactory().create_cannon()
        self.assertEqual(str(obj), 'Radiant cannon')

    def test_dire_scout(self):
        obj = DireArmyFactory().create_scout()
        self.assertEqual(str(obj), 'Dire scout')

    def test_radiant_scout(self):
        obj = RadiantArmyFactory().create_scout()
        self.assertEqual(str(obj), 'Radiant scout')

    def test_difference_dc(self):
        obj1 = DireArmyFactory().create_cannon()
        obj2 = DireArmyFactory().create_cannon()
        self.assertNotEqual(obj1, obj2)

    def test_difference_ds(self):
        obj1 = DireArmyFactory().create_scout()
        obj2 = DireArmyFactory().create_scout()
        self.assertNotEqual(obj1, obj2)

    def test_difference_rc(self):
        obj1 = RadiantArmyFactory().create_cannon()
        obj2 = RadiantArmyFactory().create_cannon()
        self.assertNotEqual(obj1, obj2)

    def test_difference_rs(self):
        obj1 = RadiantArmyFactory().create_scout()
        obj2 = RadiantArmyFactory().create_scout()
        self.assertNotEqual(obj1, obj2)
