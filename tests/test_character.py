import unittest
import os
from battlenet.connection import Connection
from battlenet.things import Character

REGION = Connection.US
REALM = 'Nazjatar'
CHARACTER = 'Vishnevskiy'

Connection.setup(app=os.environ.get('BATTLENET_APP'))

class CharacterTest(unittest.TestCase):
    def test_general(self):
        character = Character(REGION, REALM, CHARACTER)

        self.assertEqual(character.name, CHARACTER)
        self.assertEqual(str(character), CHARACTER)

        self.assertEqual(character.get_realm_name(), REALM)
        self.assertEqual(character.realm.name, REALM)
        self.assertEqual(str(character.realm), REALM)

        self.assertEqual(character.faction, Character.HORDE)

        self.assertEqual(character.get_race_name(), Character.GOBLIN)

        self.assertEqual(character.get_class_name(), Character.WARLOCK)

        self.assertIsInstance(character.level, int)
        self.assertGreaterEqual(character.level, 85)

        self.assertIsInstance(character.achievement_points, int)

        self.assertEqual(character.gender, Character.MALE)

    def test_guild(self):
        character = Character(REGION, REALM, CHARACTER, fields=[Character.GUILD])

        self.assertEqual(character.guild.name, 'Excellence')

    def test_stats(self):
        character = Character(REGION, REALM, CHARACTER, fields=[Character.STATS])

        self.assertIsInstance(character.stats.agility, int)

    def test_professions(self):
        character = Character(REGION, REALM, CHARACTER, fields=[Character.PROFESSIONS])

        primary = character.professions['primary']

        tailoring = primary[0]
        enchanting = primary[1]

        self.assertEqual(tailoring.name, Character.TAILORING)
        self.assertIsInstance(tailoring.rank, int)
        self.assertIsInstance(tailoring.recipes, list)

        self.assertEqual(enchanting.name, Character.ENCHANTING)

        secondary = character.professions['secondary']

        first_aid = secondary[0]
        archaeology = secondary[1]

        self.assertEqual(first_aid.name, Character.FIRST_AID)
        self.assertEqual(archaeology.name, Character.ARCHAEOLOGY)

    def test_appearance(self):
        character = Character(REGION, REALM, CHARACTER, fields=[Character.APPEARANCE])

        self.assertEqual(character.appearance.face, 2)
        self.assertEqual(character.appearance.feature, 9)
        self.assertEqual(character.appearance.hair_color, 3)
        self.assertEqual(character.appearance.show_cloak, True)
        self.assertEqual(character.appearance.show_helm, True)
        self.assertEqual(character.appearance.hair, 5)

if __name__ == '__main__':
    unittest.main()