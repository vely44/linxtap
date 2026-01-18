from src.core.app_logic import AppLogic


def test_process_click_increments_count():
    logic = AppLogic()
    assert logic.click_count == 0

    result = logic.process_click()
    assert logic.click_count == 1
    assert "1 time" in result


def test_process_click_multiple():
    logic = AppLogic()
    logic.process_click()
    logic.process_click()
    result = logic.process_click()

    assert logic.click_count == 3
    assert "3 time" in result
