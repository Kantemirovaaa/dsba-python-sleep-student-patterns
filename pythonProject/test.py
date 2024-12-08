a = str(input())
unix_system = 'Unix path: /' + a
windows_path = 'Windows path: C: \\' + a
while a != '':

    a = str(input())
    unix_system += '/' + a
    windows_path += '\\' + a
print(unix_system)
print(windows_path)