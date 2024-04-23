from selenium.webdriver.common.by import By
from webdriver_setup import WebDriverSetup
from page_actions import PageActions

def main():
    driver = WebDriverSetup.get_webdriver()
    actions = PageActions(driver)

    # Open the website
    driver.get("https://gem.gov.in")

    # Define locators
    bid_link_locator = (By.XPATH, "//a[@title='Bids' and contains(., 'Bids \xa0')]")
    list_of_bids_locator = (By.XPATH, "//a[@href='https://bidplus.gem.gov.in/all-bids' and @title='List of Bids']")
    advance_search_locator = (By.XPATH, "//a[contains(@href, '/advance-search') and contains(., 'Advance Search')]")
    ministry_tab_locator = (By.ID, "ministry-tab")  # Locator for the "Search by Ministry / Organization" link
    dropdown_locator = (By.CSS_SELECTOR, ".select2-selection--single")

    # Perform actions
    actions.hover_over_element(bid_link_locator)
    actions.click_on_element(list_of_bids_locator)
    actions.switch_to_new_tab_and_close_others()
    actions.click_on_element(advance_search_locator)
    actions.click_on_element(ministry_tab_locator)  # Click on the ministry tab
    actions.select_from_select2(dropdown_locator, "MINISTRY OF DEFENCE")

    # Wait and close
    try:
        input("Press Enter to close...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
