import json
import os

class IdSum:
    def __init__(self):
        pass


    def import_json(self, file):
        return json.load(open(file))


    def find_item_sums(self, input_list):
        item_sum = 0
        if input_list.get('menu', {}).get('items'):
            for item_list in input_list['menu']['items']:
                if type(item_list) is dict and 'id' in item_list and isinstance(item_list['id'], int) and 'label' in item_list:
                    item_sum += item_list['id']
        return item_sum


    def print_item_sums(self, json_file):
        for input_list in json_file:
            print self.find_item_sums(input_list)


    def get_one_item_sum(self, input_list):
        item_sum = 0
        if input_list.get('menu', {}).get('items'):
            for item_list in input_list['menu']['items']:
                if (type(item_list) is dict and 'id' in item_list and isinstance(item_list['id'], int) and 'label' in item_list):
                    item_sum += item_list['id']
        return item_sum


def main():
    input_file_dir = "input_files"
    id_sum = IdSum()
    for file in os.listdir(input_file_dir):
        print "printing items_sums for file: %s" % file
        fullpath = '%s\%s' % (input_file_dir, file)
        if os.name != 'nt':
            fullpath = '%s/%s' % (input_file_dir, file)
        json_file = id_sum.import_json('%s\%s' % (input_file_dir, file))
        id_sum.print_item_sums(json_file)


if __name__ == '__main__':
    main()