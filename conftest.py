import pytest, pytest_html
# from enquiry_form_test import TestEnquiryForm
import search_page_new_test

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail) :
            extras.append(pytest_html.extras.url(search_page_new_test.driver.current_url))
            # only add additional html on failure
            # extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            screen_shot_name = "/home/shrey/PycharmProjects/MyProject/results/screenshot.png"
            search_page_new_test.driver.save_screenshot(screen_shot_name)
            extras.append(pytest_html.extras.image(screen_shot_name))
        report.extras = extras