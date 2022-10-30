with open('File.txt', 'w+') as files:
    files.write('Я гений и стараюсь учить питон')
    files.seek(0)
    read = files.read(7)
print(read)