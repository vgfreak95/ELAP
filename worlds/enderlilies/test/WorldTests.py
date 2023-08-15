from test.TestBase import WorldTestBase

class EnderLiliesTestBase(WorldTestBase):
    game = "EnderLilies"
    test_player_id = 1
    def test_world_generation(self):
        print(f"Items in World: {self.multiworld.itempool}\n Items Length: {len(self.multiworld.itempool)}")
        print(f"Locations: {self.multiworld.get_locations(self.test_player_id)}\n Locations Length {len(self.multiworld.get_locations(self.test_player_id))}")
        print(f"Regions: {self.multiworld.get_regions(self.test_player_id)}\n Regions Length {len(self.multiworld.get_regions(self.test_player_id))}")

        self.assertEqual("hello", "hello")
