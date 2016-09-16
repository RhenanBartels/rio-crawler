# coding: utf-8
from unittest import mock, TestCase

from zapcrawler import URL, ZapCrawlerManager


class TestZap(TestCase):
    @mock.patch('zapcrawler.Chrome')
    def setUp(self, _chrome):
        self.url = URL.format(neighbourhood='BOTAFOGO', zone='Zona Sul',
                              page='1', type='apartamento')

        instance = _chrome()
        self.manager = ZapCrawlerManager(self.url)
        self.manager.browser = instance

    def test_visit_list_buildings(self):
        self.manager.visit()

        self.manager.browser.get.assert_called_once_with(self.url)

    def test_get_informations(self):
        self.manager.get_information()

        self.manager.browser.find_elements_by_class_name.assert_called_once_with(
            'list-cell')

    @mock.patch('zapcrawler.ZapCrawlerManager.get_information')
    def test_normalize_information(self, _get_information):
        data = ['R$ 2.400\nCAMPO BELO\nRua Constantino de Souza\nSao Paulo - Sp\nApartamento\n1 quarto | 1 vaga | 48m2\n[?]']

        content_chrome_selenium = mock.MagicMock()
        content_chrome_selenium.text = data[0]

        _get_information.return_value = [content_chrome_selenium]

        self.manager.content = data

        response = self.manager.normalize_information()
        expected = ['R$ 2.400', '48m2', '1 quarto']

        self.assertEqual(response, expected)
