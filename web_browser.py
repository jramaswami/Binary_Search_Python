"""
binarysearch.com :: Web Browser
jramaswami
"""


class WebBrowser:
    def __init__(self, homepage):
        self.back_history = [homepage]
        self.fwd_history = []


    def visit(self, page):
        """Visits the site page, clearing all forward history."""
        self.back_history.append(page)
        self.fwd_history = []

    def back(self, n):
        """
        Goes back n number of steps in history and returns the current page.
        Note that once you reach the homepage, you stay on that page even if
        you go back.
        """
        while len(self.back_history) > 1 and n:
            self.fwd_history.append(self.back_history.pop())
            n -= 1
        return self.back_history[-1]

    def forward(self, n):
        """
        Goes forward n number of steps in history and returns the current page.
        Note that once you reach the most recent page, you stay on that page
        even if you go forward.
        """
        while self.fwd_history and n:
            self.back_history.append(self.fwd_history.pop())
            n -= 1
        return self.back_history[-1]
