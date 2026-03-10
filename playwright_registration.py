from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Открыть страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнить поля
    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill("user.name@gmail.com")

    user_input = page.get_by_test_id("registration-form-username-input").locator('input')
    user_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    registration_link = page.get_by_test_id("registration-page-registration-button")

    # Нажать на ссылку "Registration" — произойдёт редирект на страницу Registration
    registration_link.click()

    # Проверит заголовок "Dashboard"
    dashboard_link = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_link).to_be_visible()



