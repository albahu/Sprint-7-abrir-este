import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
   

    def __init__(self, driver):
        self.driver = driver

        def test_open_page(self):
        self.driver.get("https://4c605270-205d-4bdc-9518-b8a2b6a4f062.serverhub.tripleten-services.com?lng=es")

    def test_set_window_size(self):
        self.driver.set_window_size(1920, 1057)

    def click_from(self,):
        self.driver.find_element(By.ID, "from").click()

    def set_from(self):
        self.driver.find_element(By.ID, "from").send_keys("east 2nd street 601")

    def click_to(self):
        self.driver.find_element(By.ID, "to").click()

    def set_to(self):
        self.driver.find_element(By.ID, "to").send_keys("1300 1st st")

    def click_personal(self):
        self.driver.find_element(By.CSS_SELECTOR, ".mode:nth-child(3)").click()

    def click_button_taxi(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(3)").click()

    def click_comfort(self):
        self.driver.find_element(By.CSS_SELECTOR, ".tcard:nth-child(5) > .tcard-icon > img").click()

    def click_phone_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".np-text").click()

    def click_phone_number(self):
        self.driver.find_element(By.CSS_SELECTOR, ".active .label").click()

    def phone_input(self):
        self.driver.find_element(By.ID, "phone").send_keys("+1 123 123 12 12")

    def click_next(self):
        self.driver.find_element(By.CSS_SELECTOR, ".active .button").click()

    def click_close(self):
        self.driver.find_element(By.CSS_SELECTOR, ".active:nth-child(2) > .close-button").click()

    def click_payment_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".pp-text").click()

    def click_card_number(self):
        self.driver.find_element(By.ID, "number").click()

    def type_card_number(self):
        self.driver.find_element(By.ID, "number").send_keys("1234 5678 9100")

    def click_code_number(self):
        self.driver.find_element(By.NAME, "code").click()

    def type_code_number(self):
        self.driver.find_element(By.NAME, "code").send_keys("111")

    def click_add_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".payment-picker .active > .close-button").click()

    def click_comment_field(self):
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .input-container > .label").click()

    def type_comment_field(self):
        self.driver.find_element(By.ID, "comment").send_keys("muestrame el camino al museo")

    def click_tissues(self):
        self.driver.find_element(By.CSS_SELECTOR, ".r:nth-child(1) .slider").click()

    def click_ice_cream(self):
        self.driver.find_element(By.CSS_SELECTOR, ".r:nth-child(1) .counter-plus").click()

    def click_ice_cream_2(self):
        self.driver.find_element(By.CSS_SELECTOR, ".r:nth-child(1) .counter-plus").click()

    def click_call_taxi_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".smart-button-main").click()



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    def test_configure_address(self):
        self.UrbanRoutesPage.configure_address(data.address_from)
        assert configured_address == address_to_configure   
    # Se verifica configurar dirección de destino

    def test_select_comfort_rate(self):
        self.UrbanRoutesPage.select_comfort_rate()
        assert selected_comfort_rate == "COMFORT"
        # Se agrega seleccionar tarifa COMFORT

    def test_fill_phone_number(self):
        self.UrbanRoutesPage.fill_phone_number('+1 123 123 12 12')
         assert actual_phone_number == phone_number_to_fill
        
        # Se verifica rellenar el número telefónico

    def test_add_credit_card(self):
        self.UrbanRoutesPage.add_credit_card('1234 5678 9011', '111')
        assert added_credit_card == (credit_card_number, cvv)
        # Se verifica agregar tarjeta de crédito

    def test_write_message(self):
        self.UrbanRoutesPage.write_message('Muestrame el camino al museo')
        assert written_message == message_to_write
        # Se verifica mensaje de prueba

    def test_order_blanket_and_tissues(self):
        self.UrbanRoutesPage.order_blanket_and_tissues()
        assert "Orden completada" in order_confirmation_message
        # Se pide una manta y pañuelos

    def test_order_ice_cream(self):
        self.UrbanRoutesPage.order_ice_cream(2)
         assert f"Orden completada: {quantity_to_order} helados" in order_confirmation_message, f"La orden de {quantity_to_order} helados no se completó correctamente."
        # Se verifica para pedir un helado

    def test_open_taxi_modal(self):
        self.UrbanRoutesPage.open_taxi_modal()
        assert is_taxi_modal_open
        # Se verifican para buscar un taxi

    def test_wait_for_driver_info_modal(self):
        self.UrbanRoutesPage.wait_for_driver_info_modal()
         assert is_driver_info_modal_present
        
        # Se verifica información


    if __name__ == '__main__':
        unittest.main()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

  



