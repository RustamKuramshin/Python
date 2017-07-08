import os, fnmatch

dirIn = input("Укажите расположение архивов резервных копий: ")
dirOut = input("Укажите директорию распакови последних версий архивов: ")
folder = os.listdir(path=dirIn)
for i in range(len(folder)):
    zipFiles = []
    dirArch = dirIn + '\\' + folder[i]
    arch = os.listdir(path=dirArch)
    for name in arch:
        if fnmatch.fnmatch(name, '*.7z'):
            zipFiles += [name]
    if zipFiles:        
        last = zipFiles[0]
        for file in zipFiles:
            if os.path.getctime(dirArch + '\\' + file) > os.path.getctime(dirArch + '\\' + last):
                last = file
        dirLast = dirArch + '\\' + last
        cmd = '7z x ' + '-o' + dirOut + '\\' + folder[i] + ' ' + '"' + os.path.abspath(dirLast) + '"'
        os.system(cmd)
        print(dirLast)
    else:
        pass
 
        

