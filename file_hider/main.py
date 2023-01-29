import ctypes

hide_attribute = 0x02

ret = ctypes.windll.kernel32.SetFileAttributesW("ocultar.txt", hide_attribute)

if ret:
    print("Hidden file")
else:
    print("The file has not been hidden")
