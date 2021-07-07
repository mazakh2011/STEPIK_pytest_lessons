link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_guest_should_find_button_add_card(browser):
    browser.get(link)
    card_button = browser.find_element_by_css_selector("#add_to_basket_form")
    assert card_button, 'Not find card_button'
