# Roman Numeral Reduction
# Have the function RomanNumeralReduction(str) read str which will be a string of roman numerals in decreasing order. The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. Your program should return the same number given by str using a smaller set of roman numerals. For example: if str is "LLLXXXVVVV" this is 200, so your program should return CC because this is the shortest way to write 200 using the roman numeral system given above. If a string is given in its shortest form, just return that same string.
# Examples
# Input: "XXXVVIIIIIIIIII"
# Output: L
# Input: "DDLL"
# Output: MC


def RomanNumeralReduction(strParam):
  romanDecimalMap = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
  }

  decimal = 0
  for char in strParam:
    decimal += romanDecimalMap[char]
  
  roman = ""
  deciamlRomanMap = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
  }

  for base,sym in deciamlRomanMap.items():
      roman += sym*(decimal//base)
      decimal %= base
  return roman

# keep this function call here 
print(RomanNumeralReduction(input()))