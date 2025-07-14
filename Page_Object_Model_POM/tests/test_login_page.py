import ui_pages_classes.login_page

def test_login_page(get_driver_and_web_wait):
    driver, wait = get_driver_and_web_wait

    loginPage = ui_pages_classes.login_page.LoginPage(driver=driver, wait=wait)

    loginPage.click_login_link()
    print("The current URL Is: ", loginPage.return_url());

    assert loginPage.return_url() == "https://www.letskodeit.com/login"

    loginPage.enter_email_addr()
    loginPage.enter_password()
    loginPage.click_login_btn()