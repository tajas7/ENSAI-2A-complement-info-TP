from business_object.pokemon.abstract_pokemon import AbstractPokemon


class TestLevelUp:
    def test_level_up(self):
        # GIVEN
        snorlax = AbstractPokemon(level=10)

        # WHEN
        snorlax.level_up()

        # THEN
        assert snorlax.level == 11
