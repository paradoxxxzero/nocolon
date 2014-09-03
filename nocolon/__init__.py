# -*- coding: utf-8 -*-
# Copyright (C) 2014 by Florian Mounier (paradoxxxzero)
# This file is part of nocolon, licensed under a 3-clause BSD licens
import codecs


def encode(input, errors='strict', *args):
    return codecs.utf_8_encode(input, errors)


def decode(input, errors='strict', *args):
    """Finds indent and add a colon on previous line"""
    u, l = codecs.utf_8_decode(input, errors, True)
    out = []
    offset = 0
    for line in u.split('\n'):
        if line.strip():
            indent = len(line) - len(line.lstrip())
            if indent > offset:
                i = -1
                while not out[i].strip() and len(out) > -i:
                    i -= 1

                if out[i].rstrip()[-1] != ':':
                    out[i] += ':'
            offset = indent
        out.append(line)
    return '\n'.join(out), l


class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return encode(input, errors)

    def decode(self, input, errors='strict'):
        return decode(input, errors)


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(
        name='nocolon',
        encode=Codec().encode,
        decode=Codec().decode,
        streamreader=StreamReader,
        streamwriter=StreamWriter
    )


def search_function(encoding):
    if encoding == 'nocolon':
        return (encode, decode, StreamReader, StreamWriter)


codecs.register(search_function)
