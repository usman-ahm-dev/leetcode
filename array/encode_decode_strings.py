"""659. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then
sent over the network and is decoded back to the original list of strings.
"""


class Solution:
    def encode(self, strs):
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)};{s}")
        return "".join(encoded)

    def decode(self, s):
        decoded = []
        for i in range(len(s)):
            j = i
            while s[i] != ";":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded
