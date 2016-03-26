import base
import bz2
import gzip
import lzma
from functools import partial

def passthrough(x):
	return x

compressors = (bz2.compress, gzip.compress, partial(lzma.compress, check=lzma.CHECK_NONE), passthrough)
decompressors = (bz2.decompress, gzip.decompress, lzma.decompress, passthrough)

def encode(data):
	return base.encode(min((c(data) for c in compressors), key=len))

def decode(encoded):
	compressed = base.decode(encoded)
	for z in decompressors:
		try:
			return z(compressed)
		except (OSError, lzma.LZMAError):
			pass