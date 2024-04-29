from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class SeleniumUtilities:
    def __init__(self, driver):
        self.driver = driver

    def print_element_details(self, locator):
        """Prints details about an element found with the given locator."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            print("Element found:")
            print("  Tag Name:", element.tag_name)
            print("  Text:", element.text)
            print("  Attributes:")
            # Attributes like 'id', 'class', 'name', 'type' can be commonly useful
            for attr in ['id', 'class', 'name', 'type']:
                value = element.get_attribute(attr)
                if value:
                    print(f"    {attr}: {value}")
        except NoSuchElementException:
            print("No such element: Could not find element using locator", locator)
        except Exception as e:
            print("Error finding element:", e)

