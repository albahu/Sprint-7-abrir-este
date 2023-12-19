# urban_routes_page.py
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://c7424f10-9c9e-4919-94c0-b13a2f937964.serverhub.tripleten-services.com?lng=es')

    def set_address(self, address):
        address_input = self.driver.find_element(By.ID, 'address-input')
        address_input.clear()
        address_input.send_keys(address)

    def select_comfort_tariff(self):
        comfort_tariff_button = self.driver.find_element(By.ID, 'comfort-tariff-button')
        comfort_tariff_button.click()

    def fill_phone_number(self, phone_number):
        phone_input = self.driver.find_element(By.ID, 'phone-input')
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def add_credit_card(self, card_number, card_code):
        add_card_button = self.driver.find_element(By.ID, 'add-card-button')
        add_card_button.click()

        card_number_input = self.driver.find_element(By.ID, 'card-number-input')
        card_number_input.clear()
        card_number_input.send_keys(card_number)

        card_code_input = self.driver.find_element(By.ID, 'code')
        card_code_input.clear()
        card_code_input.send_keys(card_code)
        card_code_input.send_keys(Keys.TAB)  # Cambiar el enfoque para activar el botón de enlace

    def write_message(self, message):
        message_input = self.driver.find_element(By.ID, 'message-input')
        message_input.clear()
        message_input.send_keys(message)

    def request_blanket_and_tissues(self):
        blanket_button = self.driver.find_element(By.ID, 'blanket-button')
        blanket_button.click()

        tissues_button = self.driver.find_element(By.ID, 'tissues-button')
        tissues_button.click()

    def request_ice_creams(self):
        ice_creams_button = self.driver.find_element(By.ID, 'ice-creams-button')
        ice_creams_button.click()

    def is_search_modal_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'search-modal'))
            )
            return True
        except:
            return False


