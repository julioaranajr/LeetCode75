class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        # Calculate the bit length of n
        bit_length = n.bit_length()
        # Create a mask with all bits set to 1 of the same length as n
        mask = (1 << bit_length) - 1
        # XOR n with the mask to get the complement
        return n ^ mask
