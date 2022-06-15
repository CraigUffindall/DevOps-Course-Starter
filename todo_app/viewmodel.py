class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        return self.get_items_by_status('To Do')

    @property
    def doing_items(self):
        return self.get_items_by_status('Doing')

    @property
    def done_items(self):
        return self.get_items_by_status('Done')

    def get_items_by_status(self, status):
        items = []
        
        for item in self._items:
            if item.status == status:
                items.append(item)

        return items