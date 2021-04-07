import pytest
from controllers.player import PlayerController


def test_initialization():
    """checks if initialization of controller and if they are private"""
    player =PlayerController("Batman","Doomsday")
    assert hasattr(player, '_player')
    assert hasattr(player, '_maze')
    assert hasattr(player, '_cd')
    assert hasattr(player, '_time_passed')
    assert player._player == "Batman"
    assert player._maze == "Doomsday"

def test_set_and_check_cd():
    """sets the movement cooldown and checks if it will reset after a second """
    try:
        player = PlayerController("Batman","Doomsday")
        player.set_cd("right")
        assert player._time_passed["right"] == 0
        assert player._cd == {"up": False, "down": False, "left": False, "right": True}
        player.check_cd(1001,"right")
        player.set_cd('left')
        assert player._time_passed["left"] == 0
        assert player._cd == {"up": False, "down": False, "left": True, "right": False}
        player.check_cd(1001,"left")
        player.set_cd('up')
        assert player._time_passed["up"] == 0
        assert player._cd == {"up": True, "down": False, "left": False, "right": False}
        player.check_cd(1001,"up")
        player.set_cd('down')
        assert player._time_passed["down"] == 0
        assert player._cd == {"up": False, "down": True, "left": False, "right": False}
    except:
        assert False
def test_clear_cd():
    """checks to clear the direction"""
    try:
        player = PlayerController("Batman","Doomsday")
        player.set_cd('right')
        player.clear_cd('right')
        assert player._cd['right'] == False
    except:
        assert False