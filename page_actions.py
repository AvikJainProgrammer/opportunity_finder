from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageActions:
    def __init__(self, driver):
        self.driver = driver

    def hover_over_element(self, locator):
        """Hover over an element specified by its locator."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            ActionChains(self.driver).move_to_element(element).perform()
            print("Hovered over the element successfully.")
        except Exception as e:
            print("Error hovering over element:", e)

    def click_on_element(self, locator):
        """Click on an element specified by its locator."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            element.click()
            print("Clicked on the element successfully.")
        except Exception as e:
            print("Error clicking on element:", e)

    def switch_to_new_tab_and_close_others(self):
        """Switches to the newest browser tab and closes all others, ensuring safe operations."""
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        all_tabs = self.driver.window_handles
        current_tab = self.driver.current_window_handle
        
        # Attempt to switch to a new tab
        new_tab = None
        for handle in all_tabs:
            if handle != current_tab:
                new_tab = handle
                self.driver.switch_to.window(handle)
                print(f"Switched to new tab: {handle}")
                break
        
        if not new_tab:
            raise Exception("No new tab was opened.")

        # Close all other tabs safely
        for handle in all_tabs:
            if handle != new_tab:
                self.driver.switch_to.window(handle)
                self.driver.close()
                print(f"Closed tab: {handle}")

        # Safely switch to the new tab as the final step
        self.driver.switch_to.window(new_tab)
        print(f"Currently on new tab: {self.driver.current_window_handle}")

    def select_from_select2(self, dropdown_locator, option_text):
        """Selects an option from a select2 dropdown by its visible text."""
        try:
            # Click the select2 dropdown to open the list of options
            self.click_on_element(dropdown_locator)

            # Wait for the dropdown options to become visible and click the desired option
            option_locator = (By.XPATH, f"//li[text()='{option_text}']")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(option_locator))
            self.click_on_element(option_locator)

            print(f"Selected '{option_text}' from select2 dropdown.")
        except Exception as e:
            print("Error selecting from select2 dropdown:", e)


