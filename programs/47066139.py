def backwards_alphabet(n):
  if ord(n) == 97:
    return n
  else:
    return n + backwards_alphabet(ord(n-1))

backwards_alphabet(98)