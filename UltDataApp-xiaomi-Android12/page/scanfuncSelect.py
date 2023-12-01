from page.base import base


class ScanfuncSelect(object):
    def __init__(self, page_name, element_name):
        self.base = base(page_name, element_name)

    def select_func(self):
        return self.base.getElement().click()
