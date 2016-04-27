from collections import deque

class VigenereCipher:
    num2alphabet = [chr(i) for i in range(65, 65+26)]
    alphabet2num = {i: ord(i) - 65 for i in num2alphabet}

    def __init__(self, keyword):
        self.keyword = self._filter_non_alphabetic(keyword).upper()

    def __repr__(self):
        return "keyword: {}".format(self.keyword)

    @staticmethod
    def _filter_non_alphabetic(s):
        return ''.join([i for i in filter(str.isalnum, s)])

    @staticmethod
    def _shift_right(lst, num_pos=0):
        d = deque(lst)
        d.rotate(num_pos)
        return list(d)

    def _extend_keyword(self, length):
        repeats = length // len(self.keyword) + 1
        dup_keyword = self.keyword * repeats
        return dup_keyword[:length]

    def _encode_letter(self, ch, key):
        row_idx = self.alphabet2num[ch]
        col_idx = self.alphabet2num[key]
        return self._shift_right(self.num2alphabet, -row_idx)[col_idx]

    def _decode_letter(self, ch, key):
        col_offset = (26 + ord(ch) - ord(key)) % 26
        return self.num2alphabet[col_offset]

    def _code(self, content, code_func):
        content = self._filter_non_alphabetic(content).upper()
        ext_keyword = self._extend_keyword(len(content))        
        res = []

        for ch, key in zip(content, ext_keyword):
            res.append(code_func(ch, key))

        return ''.join(res)

    def decode(self, encoded):
        return self._code(encoded, self._decode_letter)

    def encode(self, content):
        return self._code(content, self._encode_letter)
