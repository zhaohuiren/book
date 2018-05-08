from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    def test_home_page_returns_correct_html(self):
        request=HttpRequest()  #创建一个HttpRequest对象 用户在浏览器中请求网页时，django看到的就是这个HttpRequest对象
        response=home_page(request) #把这个对象传给home——page视图，得到响应
        self.assertTrue(response.content.startswith(b'<html>')) # 断言响应
        self.assertIn(b'<html><title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

