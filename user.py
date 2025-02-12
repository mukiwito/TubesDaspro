import validasi, variabelGlobal

def checkRole(x):    # mengecek role x(admin/user) karena tiap role memiliki kekhususan masing-masing
    for i in range(len(variabelGlobal.user['data'])):
        if variabelGlobal.user['data'][i][2] == x:
            return variabelGlobal.user['data'][i][5]

def register(): # fungsi register
    idx = int(variabelGlobal.user['data'][-1][0]) + 1
    nama = input('Masukkan nama: ').title()
    username = input('Masukkan username: ')
    while not validasi.isUsernameValid(username):
        print("Username telah dipakai")
        username = input('Masukkan username: ')
        
    password = input('Masukkan password: ')
    alamat = input('Masukkan alamat: ')
    newUser = [idx,nama,username,password,alamat,'user']
    variabelGlobal.user['data'].append(newUser)
    print("\nUser {} telah berhasil register ke dalam Kantong Ajaib".format(username))
    return