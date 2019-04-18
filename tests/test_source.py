from app import models
import unittest
Source = models.Source

class TestSource(unittest.TestCase):
    '''
    This class tests the behaviour of the source class
    '''

    def setUp(self):
        '''
        Function that creates a new news object
        '''
        self.new_news = Source("123","CNN","The best news","https://www.cnn.com","politics","en","Kenya")

    def test_init(self):
        '''
        Function that tests if the object is initialized correctly
        '''
        self.assertTrue(self.new_news.id,"123")
        self.assertTrue(self.new_news.name,"CNN")
        self.assertTrue(self.new_news.description,"The best news")
        self.assertTrue(self.new_news.url,"https://www.cnn.com")
        self.assertTrue(self.new_news.category,"politics")
        self.assertTrue(self.new_news.language,"en")
        self.assertTrue(self.new_news.country,"Kenya")
