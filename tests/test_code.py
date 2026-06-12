# import pytest
# from src import code

# def test_sum_numbers():
#   result1, result2 = code.sum_numbers(1, 2)
#   assert result1 == 3
#   assert result2 == 1

# def get_json_data_mock(id):
#   return {'name':'サプー'}

# def test_get_user_names(monkeypatch):
#   monkeypatch.setattr(
#     code, 'get_json_data', get_json_data_mock)
#   result = code.get_user_names(['001', '009'])

#   assert list(result.keys()) == ['001', '009']
#   assert list(result.values()) == ['サプー', 'サプー']

# def test_user_name_validation():
#   with pytest.raises(ValueError) as e:
#     code.user_name_validation(None)
#   assert str(e.value) == '名前が設定されていません'

# from code import add

# def test_add():
#   assert　add(1, 2) == 3

import pytest
from src.code import multiply, is_even, divide

# def test_is_adult():
#   assert is_adult(20)
#   assert is_adult(18)
#   assert not is_adult(17)

# def test_divide():
#   with pytest.raises(ZeroDivisionError):
#     divide(10, 0)

# def mock_get_json_data(user_id):
#   return {"name": "サプー"}

# def test_get_user_name(monkeypatch):
#   monkeypatch.assert(
#     code,
#     "get_json_data",
#     mock_get_json_data
#   )
#   result = code.get_user_name("001")
#   assert result == "サプー"

def test_multiply():
  assert multiply(3, 4) == 12

def test_is_even():
  assert is_even(4)
  assert not is_even(5)

def test_divide():
  with pytest.raises("ZeroDivisionError"):
  divide(10, 0)

def mock_get_json_data(user_id):
  return {"name": "サプー"}

def test_get_user_name(monkeypatch):
  monkeypatch.setattr {
    code,
    "get_json_data",
    mock_get_json_data
  }
  assert code.get_user_name("001") == "サプー"

def test_get_status(monkeypatch):
  monkeypatch.setattr(
    requests,
    "get",
    mock_get
  )
  assert code.get_status()

def mock_test_get:
  return 200
