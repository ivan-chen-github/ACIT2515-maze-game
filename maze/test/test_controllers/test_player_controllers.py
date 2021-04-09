import pytest
from controllers.player import PlayerController


def test_initialization():
    """checks if initialization of controller and if they are private"""
    player = PlayerController("Batman","Doomsday")
    assert hasattr(player, '_player')
    assert hasattr(player, '_maze')
    assert hasattr(player, '_cd')
    assert type(player._cd) is dict
    assert hasattr(player, '_time_passed')
    assert type(player._time_passed) is dict
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

def test_set_cd():
    """
    check if set_cd() properly resets time_passed and sets correct bool
    """
    try:
        player = PlayerController("Batman","Doomsday")
        player._time_passed['right'] = 200
        assert player._time_passed == {"up": 0, "down": 0, "left": 0, "right": 200}
        
        player._time_passed['left'] = 400
        assert player._time_passed == {"up": 0, "down": 0, "left": 400, "right": 200}
        assert player._cd['right'] == False
        
        player.set_cd("right")
        assert player._cd == {"up": False, "down": False, "left": False, "right": True}
        assert player._time_passed == {"up": 0, "down": 0, "left": 400, "right": 0} 
        
        player.set_cd('left')
        assert player._cd == {"up": False, "down": False, "left": True, "right": True}
        assert player._time_passed == {"up": 0, "down": 0, "left": 0, "right": 0}

    except:
        assert False


def test_clear_cd():
    """checks to clear the direction"""
    try:
        player = PlayerController("Batman","Doomsday")
        player.set_cd('right')
        assert player._cd['right'] == True
        player.clear_cd('right')
        assert player._cd['right'] == False
    except:
        assert False

def test_check_cd():
    """
    check if check_cd() will properly invoke clear_cd()
    """
    try:
        player = PlayerController("Batman","Doomsday")
        player.set_cd('right')
        assert player._cd['right'] == True
        player.check_cd(200, 'right')
        assert player._cd['right'] == True
        assert player._time_passed['right'] == 200
        player.check_cd(150, 'right')
        assert player._cd['right'] == True
        assert player._time_passed['right'] == 350
        player.check_cd(200, 'right')
        assert player._cd['right'] == False
        assert player._time_passed['right'] == 0
    except:
        assert False