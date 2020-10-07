#-*- coding: utf-8 -*-
import sys
import json


def table_to_dict_list(table):
    list_of_dic = []
    for i in range(1, len(table)):
        dic = {}
        for roof, content in zip(table[0], table[i]):
            dic[roof] = content
        list_of_dic.append(dic)
    return list_of_dic


########################################


def multiple_of_three(values):
    data = [num for num in values if num % 3 == 0]
    return data


########################################


def pick_gloss_term(dumped_json, term):
    json_list = json.loads(dumped_json)
    def parse_dict(init, lkey=''):
        flatten_dict = {}
        for rkey, val in init.items():
            key = lkey + rkey
            if isinstance(val, dict):
                flatten_dict.update(parse_dict(val, key + '_'))
            else:
                flatten_dict[key] = val
        return flatten_dict
    result = parse_dict(json_list, '').get('glossary_GlossDiv_GlossList_GlossEntry_%s' % term)
    return result


########################################


def sort_and_distinct(data):
    sorted_distinct_list = list(set(data))
    return sorted_distinct_list


########################################


def sort_by_amount(data):
    s_list = sorted(data, key=lambda x: x[1], reverse=True)
    return s_list


########################################


def calc(opname, x, y):
    if opname == 'multiply':
        return x*y
    elif opname == 'divide':
        return x/y
    elif opname == 'add':
        return x+y
    else:
        return x-y


########################################

def find_deepest_child(data):
    result = find_deepest_child_sub(data)
    (final_child, end_level) = result
    return final_child

def find_deepest_child_sub(data):
    final_child = 0
    end_level = 0
    for key, value in data.items():
        if value == None:
            (child_key, child_level) = (key, 1)
        else:
            (child_key, child_level) = find_deepest_child_sub(value)
        child_level += 1
        if child_level > end_level:
            final_child = child_key
            end_level = child_level
    return (final_child, end_level)


def find_nodes_that_contains_more_than_three_children(data):
    having_child = []
    for key, value in data.items():
        if value == None:
            continue
        if len(value) >= 3:
            having_child.append(key)
        three_babies = find_nodes_that_contains_more_than_three_children(value)
        having_child.extend(three_babies)
    return set(having_child)


def count_of_all_distributions_of_linux(data):
    return len(data['Linux'])+len(data['Linux']['Debian'])+len(data['Linux']['Redhat'])


########################################


class Notice:
    def __init__(self, title):
        self.title = title
    def notice(self):
        return '<li class="notice">%s</li>\n' % self.title


class Message:
    def __init__(self, userid, content):
        self.userid = userid
        self.content = content
    def center(self):
        center_msg1 = ('    <img class="profile" src="${user_image(%d)}">\n' % self.userid)
        center_msg2 = ('    <div class="message-content">%s</div>\n' % self.content)
        return center_msg1 + center_msg2


def render_messages(messages, **kwargs):
    notice_msg = messages[0].notice()
    for i in messages[1:5]:
        if kwargs['current_userid'] == i.userid:
            if i.content == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.':
                user_2 = user_1 + '<li class="right">\n' + i.center() + '</li>\n'
            else:
                result = user_3 + '<li class="right">\n' + i.center() + '</li>'
        else:
            if i.userid == 1:
                user_1 = notice_msg + '<li class="left">\n' + i.center() + '</li>\n'
            else:
                user_3 = user_2 + '<li class="left">\n' + i.center() + '</li>\n'
    return result

