import ctypes

ctypes.cdll.LoadLibrary("libc.so.6")
_mi = ctypes.CDLL('./libmi.so')
_mi.st_mi.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int)
_mi.st_mi.restype  = ctypes.c_float

def st_mi(x, y):
    global _mi
    n_bins = len(x)
    array_type = ctypes.c_int * n_bins
    MI = _mi.st_mi(array_type(*x), array_type(*y), ctypes.c_int(n_bins))
    return float(MI)


