# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-08-25 00:19
import unicodedata
from typing import List, Dict


def format_scores(results: Dict[str, float]) -> str:
    return ' - '.join(f'{k}: {v:.4f}' for (k, v) in results.items())


def ispunct(token):
    return all(unicodedata.category(char).startswith('P')
               for char in token)


def split_long_sentence_into(tokens: List[str], max_seq_length):
    punct_offset = [i for i, x in enumerate(tokens) if ispunct(x)]
    if not punct_offset:
        # treat every token as punct
        punct_offset = [i for i in range(len(tokens))]
    punct_offset += [len(tokens)]
    start = 0
    for i, offset in enumerate(punct_offset[:-1]):
        if punct_offset[i + 1] - start >= max_seq_length:
            yield tokens[start: offset + 1]
            start = offset + 1
    if start < punct_offset[-1]:
        yield tokens[start:]
