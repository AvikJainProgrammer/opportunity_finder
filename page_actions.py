from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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

    def select_from_select2_by_text(self, dropdown_locator, option_text):
        """Selects an option from a select2 dropdown by the visible text."""
        try:
            # Wait for the select2 element to be clickable and click it to open the dropdown
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(dropdown_locator))
            print("Dropdown element is visible and clickable.")
            self.click_on_element(dropdown_locator)

        except TimeoutException:
            print("Timeout: Dropdown element was not visible or clickable within the expected time.")
            return  # Exit the function if the dropdown is not interactable
        except Exception as e:
            print(f"Error interacting with the dropdown element: {e}")
            return  # Exit the function on other errors

        try:
            # Wait for the option to be visible and click on it
            option_locator = (By.XPATH, f"//li[contains(., '{option_text}')]")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(option_locator))
            self.click_on_element(option_locator)
            print(f"Selected '{option_text}' from select2 dropdown.")
        except Exception as e:
            print("Error selecting option from select2 dropdown:", e)

    def set_date_from_datepicker(self, input_locator, date):
        """Sets a date on a jQuery UI datepicker."""
        # Click the input field to display the datepicker
        self.click_on_element(input_locator)
        
        # Calculate differences in month and year from current displayed date
        # Example date format '2024-04-15' for April 15, 2024
        target_year, target_month, target_day = map(int, date.split('-'))
        current_year = int(self.driver.find_element(By.CLASS_NAME, "ui-datepicker-year").get_attribute('value'))
        current_month = int(self.driver.find_element(By.CLASS_NAME, "ui-datepicker-month").get_attribute('value')) + 1  # Month is zero-indexed
        
        # Date picker button locator
        date_picker_next_button_locator = (By.CLASS_NAME, "ui-datepicker-next")
        date_picker_previous_button_locator = (By.CLASS_NAME, "ui-datepicker-next")

        # Adjust the year
        while current_year < target_year:
            self.click_on_element(date_picker_next_button_locator)
            current_year += 1
        while current_year > target_year:
            self.click_on_element(date_picker_previous_button_locator)
            current_year -= 1
        
        # Adjust the month
        while current_month < target_month:
            self.click_on_element(date_picker_next_button_locator)
            current_month += 1
        while current_month > target_month:
            self.click_on_element(date_picker_previous_button_locator)
            current_month -= 1
        
        # Click the day
        day_locator = (By.LINK_TEXT, str(target_day))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(day_locator)).click()




