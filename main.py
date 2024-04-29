from date_util import DateUtil
from selenium.webdriver.common.by import By
from webdriver_setup import WebDriverSetup
from page_actions import PageActions
from selenium_utils import SeleniumUtilities


def main():
    driver = WebDriverSetup.get_webdriver()
    utilities = SeleniumUtilities(driver)
    actions = PageActions(driver)

    # Open the website
    driver.get("https://gem.gov.in")

    # Define locators
    bid_link_locator = (By.XPATH, "//a[@title='Bids' and contains(., 'Bids \xa0')]")
    list_of_bids_locator = (By.XPATH, "//a[@href='https://bidplus.gem.gov.in/all-bids' and @title='List of Bids']")
    advance_search_locator = (By.XPATH, "//a[contains(@href, '/advance-search') and contains(., 'Advance Search')]")
    ministry_tab_locator = (By.ID, "ministry-tab")  
    ministry_dropdown_locator = (By.ID, "select2-ministry-container")
    organization_dropdown_locator = (By.ID, "select2-organization-container")
    department_dropdown_locator = (By.ID, "select2-department-container")
    date_input_locator_from = (By.ID, "bidendFromMinistrySearch")
    date_to_set_from = DateUtil.get_current_date_str()
    date_input_locator_to = (By.ID, "bidendToMinistrySearch")
    date_to_set_to = DateUtil.get_date_with_offset(30)
    search_button_locator = (By.XPATH, "//a[@onclick=\"searchBid('ministry-search')\"]")


    # Perform actions
    actions.hover_over_element(bid_link_locator)
    actions.click_on_element(list_of_bids_locator)
    actions.switch_to_new_tab_and_close_others()
    actions.click_on_element(advance_search_locator)
    actions.click_on_element(ministry_tab_locator)
    actions.select_from_select2_by_text(ministry_dropdown_locator, "MINISTRY OF DEFENCE")
    actions.select_from_select2_by_text(organization_dropdown_locator, "ADVANCED WEAPONS AND EQUIPMENT INDIA LIMITED")
    actions.select_from_select2_by_text(department_dropdown_locator, "DEPARTMENT OF DEFENCE PRODUCTION")
    actions.set_date_from_datepicker(date_input_locator_from, date_to_set_from)
    actions.set_date_from_datepicker(date_input_locator_to, date_to_set_to)
    actions.click_on_element(search_button_locator)

    # Wait and close
    try:
        input("Press Enter to close...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
