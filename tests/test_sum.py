import json
import sys
sys.path.append("..")
import id_sum

TEST_JSON_ONE = '{"menu":{"header":"menu","items":[{"id":70,"label":"Label 70"},{"id":93,"label":"Label 93"},{"id":2}]}}'
TEST_JSON_TWO = '{"menu":{"header":"menu","items":[{"id":70,"labelf":""},{"id":93,"label":"Label 93"},{"id":2}]}}'
TEST_JSON_THREE = '{"menu":{"header":"menu","items":[{"id":70,"label":"Label 70"},{"id":"9sdf3","label":"Label 93"},{"id":2}]}}'
TEST_JSON_FOUR = '{"menu":{"header":"menu","items":[{"ied":70,"label":"Label 70"},{"ied":93,"label":"Label 93"},{"id":2}]}}'
TEST_JSON_FIVE = '{}'


def test_json():
    test_class = id_sum.IdSum()
    assert test_class.get_one_item_sum(json.loads(TEST_JSON_ONE)) == 163
    assert test_class.get_one_item_sum(json.loads(TEST_JSON_TWO)) == 93
    assert test_class.get_one_item_sum(json.loads(TEST_JSON_THREE)) == 70
    assert test_class.get_one_item_sum(json.loads(TEST_JSON_FOUR)) == 0
    print test_class.get_one_item_sum(json.loads(TEST_JSON_FIVE)) == 0

