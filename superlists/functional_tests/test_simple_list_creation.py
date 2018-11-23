from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):

        # Edith has heard about a cool new online to-do app. She goes

        # to check out its homepage

        self.browser.get(self.live_server_url)



        # She notices the page title and header mention to-do lists

        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text

        self.assertIn('To-Do', header_text)



        # She is invited to enter a to-do item straight away

        inputbox = self.get_item_input_box()

        self.assertEqual(

            inputbox.get_attribute('placeholder'),

            'Enter a to-do item'

        )



        # She types "Buy peacock feathers" into a text box (Edith's hobby

        # is tying fly-fishing lures)

        inputbox.send_keys('Buy peacock feathers')



        # When she hits enter, the page updates, and now the page lists

        # "1: Buy peacock feathers" as an item in a to-do list table

        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')



        # There is still a text box inviting her to add another item. She

        # enters "Use peacock feathers to make a fly" (Edith is very

        # methodical)

        inputbox = self.get_item_input_box()

        inputbox.send_keys('Use peacock feathers to make a fly')

        inputbox.send_keys(Keys.ENTER)



        # The page updates again, and now shows both items on her list

        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        self.wait_for_row_in_list_table('1: Buy peacock feathers')
