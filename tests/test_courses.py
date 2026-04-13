from playwright.sync_api import expect, Page
import pytest


@pytest.mark.registration
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_text).to_have_text('Courses')

    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    content_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(content_text).to_have_text('There is no results')

    message_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(message_text).to_have_text('Results from the load test pipeline will be displayed here')

