from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
class LayoutAndStylingTest(FunctionalTest):
#CSS测试

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        inputbox=self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.size['width'] / 2,182.5,delta=10)