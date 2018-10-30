from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
class LayoutAndStylingTest(FunctionalTest):
#CSS测试

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.size['width'] / 2,86.5,delta=10)