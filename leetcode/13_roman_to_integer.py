class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        if len(s) == 1:
            return roman_dict.get(s[0])
        res = 0
        i = 0
        while i < len(s):
            if s[i:i+2] not in roman_dict:
                res += roman_dict.get(s[i])
                i += 1
            else:
                res += roman_dict.get(s[i:i+2])
                i += 2
        return res
