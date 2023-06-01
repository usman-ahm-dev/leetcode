"""659. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then
sent over the network and is decoded back to the original list of strings.
"""


class Solution:
    def encode(self, strs):
        encoding = ""
        for string in strs:
            encoding += str(len(string)) + "#" + string

    def decode(self, s):
        decoding = []
        i = 0
        while i < len(s):
            j = i
            while str[j] != "#":
                j += 1
            length = int(s[i:j])
            decoding.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return decoding
