# coding: utf-8
from unittest import mock, TestCase

from zapcrawler import URL, ZapCrawlerManager


class TestZap(TestCase):
    @mock.patch('zapcrawler.Chrome')
    def setUp(self, _chrome):
        self.url = URL.format(neighbourhood='BOTAFOGO', zone='Zona Sul',
                              page='1', type='apartamento')

        instance = _chrome.return_value
        self.manager = ZapCrawlerManager(self.url)
        self.manager.browser = instance

    def test_visit_list_buildings(self):
        self.manager.visit()

        self.manager.browser.get.assert_called_once_with(self.url)
