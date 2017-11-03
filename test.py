import unittest
import bot
from config import *


class BotTest(unittest.TestCase):
    def test_monitor(self):
        self.try_sample('thats a sample', 0)
        self.try_sample('thats a brazil sample', 0)
        self.try_sample('thats a donna brazile sample', 1)
        self.try_sample('donna thats a brazile sample', 1)
        self.try_sample('thats a donna trump sample', 0)
        self.try_sample('isso eh um post qualquer sobre o brasil', 0)
        self.try_sample('brazile bullshit stuff trump', 1)


    def try_sample(self, sample, expect):
        counter = 0
        title = sample.lower()

        ignore = bot.is_blacklisted(sample)

        if ignore:
            counter += 1

        self.assertEqual(counter, expect)


unittest.main()

