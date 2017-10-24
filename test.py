import unittest
import bot
from config import *


class BotTest(unittest.TestCase):
    def test_monitor(self):
        SUBMISSIONS_SAMPLE = [
                'Thats a sample test for donna brazile',
                'thats a sample for brazile trump'
                ]

        self.try_sample('thats a sample', 0)
        self.try_sample('thats a brazil sample', 1)
        self.try_sample('thats a donna brazile sample', 0)
        self.try_sample('donna thats a brazile sample', 0)
        self.try_sample('thats a donna trump sample', 0)
        self.try_sample('isso eh um post qualquer sobre o brasil', 1)


    def try_sample(self, sample, expect):
        counter = 0
        title = sample.lower()

        for expression in EXPRESSIONS_TO_MONITOR:
            if expression in title:
                ignore_submission = False
                for ignored in BLACKLIST:
                    ignored_words = ignored.split('-')
                    if(all(word in title for word in ignored_words)):
                        ignore_submission = True
                if not ignore_submission:
                    counter += 1

        self.assertEqual(counter, expect)


unittest.main()

