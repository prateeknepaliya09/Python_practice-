# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:56:33 2016

@author: Prateek
"""

def permutations (orig_list):
    if not isinstance(orig_list, list):
        orig_list = list(orig_list)

    yield orig_list

    if len(orig_list) == 1:
        return

    for n in sorted(orig_list):
        new_list = orig_list[:]
        pos = new_list.index(n)
        del(new_list[pos])
        new_list.insert(0, n)
        for resto in permutations(new_list[1:]):
            if new_list[:1] + resto <> orig_list:
                yield new_list[:1] + resto