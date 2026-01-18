class AppLogic:
    def __init__(self):
        self.click_count = 0

    def process_click(self) -> str:
        self.click_count += 1
        return f"Button clicked {self.click_count} time(s)"
