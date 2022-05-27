"""Unit tests for viewmodel.py"""

from email.errors import InvalidBase64PaddingDefect
import pytest
from todo_app import viewmodel
from todo_app.data.trello_items import Item

@pytest.fixture
def view_model():
    items = []
    items.append(Item(1, 'To Do', 'item1'))
    items.append(Item(2, 'To Do', 'item2'))
    items.append(Item(3, 'Doing', 'item3'))
    items.append(Item(4, 'Doing', 'item4'))
    items.append(Item(5, 'Doing', 'item5'))
    items.append(Item(6, 'Done', 'item6'))
    items.append(Item(7, 'Done', 'item7'))
    items.append(Item(8, 'Done', 'item8'))
    items.append(Item(9, 'Done', 'item9'))
    return viewmodel.ViewModel(items)

def test_view_model_todo_items(view_model: viewmodel.ViewModel):
    # arrange / act
    items = view_model.todo_items

    # assert
    assert len(items) == 2
    assert items[0].id == 1
    assert items[0].status == 'To Do'
    assert items[0].name == 'item1'
    assert items[1].id == 2
    assert items[1].status == 'To Do'
    assert items[1].name == 'item2'

def test_view_model_doing_items(view_model: viewmodel.ViewModel):
    # arrange / act
    items = view_model.doing_items

    # assert
    assert len(items) == 3
    assert items[0].id == 3
    assert items[0].status == 'Doing'
    assert items[0].name == 'item3'
    assert items[1].id == 4
    assert items[1].status == 'Doing'
    assert items[1].name == 'item4'
    assert items[2].id == 5
    assert items[2].status == 'Doing'
    assert items[2].name == 'item5'

def test_view_model_done_items(view_model: viewmodel.ViewModel):
    # arrange / act
    items = view_model.done_items

    # assert
    assert len(items) == 4
    assert items[0].id == 6
    assert items[0].status == 'Done'
    assert items[0].name == 'item6'
    assert items[1].id == 7
    assert items[1].status == 'Done'
    assert items[1].name == 'item7'
    assert items[2].id == 8
    assert items[2].status == 'Done'
    assert items[2].name == 'item8'
    assert items[3].id == 9
    assert items[3].status == 'Done'
    assert items[3].name == 'item9'