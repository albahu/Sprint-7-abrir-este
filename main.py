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
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')



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

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    if __name__ == '__main__':
        unittest.main()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

  



