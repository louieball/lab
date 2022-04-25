import pytest
from classes import *


def setup_method(self):
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_down()
    tv.volume_up()
    tv.volume_down()
    tv.volume_down()


def test_init(self):
    assert tv.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
