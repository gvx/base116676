from codes import characters
from itertools import islice
reverse_characters = {c: i for i, c in enumerate(characters)}

def _convert_base(digits, oldbase, newbase):
	n = 0
	for digit in digits:
		n = n * oldbase + digit
	while n:
		yield n % newbase
		n //= newbase

def convert_base(digits, oldbase, newbase):
	return reversed(list(_convert_base(digits, oldbase, newbase)))

def convert_up(octets):
	yield from octets
	yield len(octets) // 256
	yield len(octets) % 256

def convert_down(octets):
	length = octets[-2] * 256 + octets[-1]
	return b'\0' * (length - len(octets) + 2) + bytes(octets[:-2])

def encode_characters(stream):
	return ''.join(characters[i] for i in stream)

def decode_characters(stream):
	return [reverse_characters[c] for c in stream]

def encode(data):
	return encode_characters(convert_base(convert_up(data), 256, 116676))

def decode(string):
	return convert_down(list(convert_base(decode_characters(string), 116676, 256)))