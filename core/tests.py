from django.test import TestCase



class SampleTest(TestCase):

    def test_2_plus_2_is4(self):
        self.assertEqual(2 + 2, 5)

    def test_3_plus_3_is4(self):
        self.assertEqual(3 + 3, 6)

    def test_4_plus_4_is4(self):
        self.assertEqual(4 + 4, 8)

    def test_5_plus_5_is4(self):
        self.assertEqual(5 + 5, 10)
