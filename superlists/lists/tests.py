from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.template.loader import render_to_string
from django.http import HttpRequest
# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)

    # def test_home_page_returns_correct_html(self):
    #
    #     request=HttpRequest()#创建request对象
    #     response=home_page(request)#把httprequest传给homepage视图
    #     html=response.content.decode('utf8')#转成html
    #     self.assertTrue(html.startswith('<html>'))#断言响应起始标签
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))#断言结束起始标签

    # def test_home_page_returns_correct_html(self):
    #     response=self.client.get('/')#传入url
    #     html= response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #     self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')