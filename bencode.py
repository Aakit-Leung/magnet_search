#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import types

reload(sys)
sys.setdefaultencoding('utf-8')

'''
b编码
因为这个爬虫只需要发送find_node和ping
所以只处理这两种情况
'''
def bencode(dic):
    try:
        if dic['q'] == 'ping':
            return 'd1:ad2:id20:' + \
                    dic['a']['id'] + \
                    'e1:q4:ping1:t' + \
                    str(len(dic['t'])) + \
                    ':' + dic['t'] + \
                    '1:y1:qe'

        if dic['q'] == 'find_node':
            return 'd1:ad2:id20:' + \
                   dic['a']['id'] + \
                   '6' + ':target20:' + \
                   dic['a']['target'] + \
                   'e1:q9:find_node1:t' + \
                   str(len(dic['t'])) + \
                   ':' + dic['t'] + \
                   '1:y1:qe'
    except ValueError:
            return ''

'''
解码
'''
'''def bdecode(string):
    if is_str(string):
        try:'''
