import olefile
import zlib
print(olefile.isOleFile('ONLINE-54.ert'))
ole = olefile.OleFileIO('ONLINE-54.ert')
print(ole.listdir())
text = ole.openstream('MD Programm text')
data = text.read()
b = zlib.decompress(data, wbits = -15)
print(b.decode('ansi'))
