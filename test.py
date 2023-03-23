
class Paginator():
    def __init__(self, data: dict, number_of_item: int) -> None:
        self.data = data
        self.number_of_item = number_of_item
        self.current_page_number = 1
    
    def current_page(self) -> int:
        return self.current_page_number

    def get_next_page(self):
        self.current_page_number = self.current_page_number + 1

    def get_previous_page(self):
        self.current_page_number = self.current_page_number - 1

    def get_elements(self, page=None) -> list:
        if not page:
            page = self.current_page_number
        first_element = (page - 1) * self.number_of_item
        last_element = first_element + self.number_of_item
        return [i for i in range(first_element, last_element)]
    
paginator = Paginator({i:i+1 for i in range(100)}, 10)

