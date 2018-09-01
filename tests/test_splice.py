import os
#import pytest
from PIL import Image

from pzm import PinZimu


os.chdir('tests')
print(os.getcwd())


class TestPinZimu:
    def test_sniff(self):
        materials = PinZimu.sniff()

        assert len(materials) == 2
        assert 59 < sum([len(i[1]) for i in materials]) < 62
        assert len(materials[0]) == 2
        assert materials[0][0].split('/')[-1] == 'tests'
        assert len(materials[0][1]) == 29

        assert len(materials[1]) == 2
        assert materials[1][0].split('/')[-1] == 'shots'
        assert len(materials[1][1]) == 31

    def test_splice(self):
        cwd = os.getcwd()
        materials = PinZimu.sniff()
        assert materials[0][0] == cwd

        for folder in materials:
            PinZimu.splice(folder, cwd)
        assert os.getcwd() == materials[0][0]
        assert 'tests.png' in os.listdir()
        tpng = Image.open('tests.png')
        assert tpng.size == (1440, 3240)

        assert materials[1][0].split('/')[-1] == 'shots'
        os.chdir(materials[1][0])
        assert 'shots.png' in os.listdir()
        spng = Image.open('shots.png')
        assert spng.size == (1440, 3420)
