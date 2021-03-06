#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from utils.util import ms_str_2_date

data = {
    "groups": [
        {"id": 1, "content": "com.test.demo1"},
        {"id": 2, "content": "com.test.demo2"}
    ],
    "items": [
        {
            'group': 1,
            'content': 'test group 1',
            'title': 'tooltips 1',
            'start': ms_str_2_date("1652953734"),
            'end': ms_str_2_date("1652963734")
        },
        {
            'group': 2,
            'content': 'test group 2',
            'title': 'tooltips 2',
            'start': ms_str_2_date("1652954734"),
            'end': ms_str_2_date("1652973734")
        },
    ]
}


def create_data_file():
    """
    Create a temporary data.json file to debug.
    Otherwise, you can create a similar file or python dict like this.
    :return:
    """
    with open("data/data.json", "w") as file:
        json.dump(data, file)


if __name__ == '__main__':
    create_data_file()
