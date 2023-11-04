#!/usr/bin/python3
def multiple_returns(sentence):
    return tuple([0, None] if not sentence else [len(sentence), sentence[0]])
