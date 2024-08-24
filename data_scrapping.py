import requests

indicators = ['CC.EST',
'CC.NO.SRC',
'CC.PER.RNK',
'CC.PER.RNK.LOWER',
'CC.PER.RNK.UPPER',
'CC.STD.ERR',
'DT.ODA.ALLD.CD',
'DT.ODA.ALLD.KD',
'DT.ODA.OATL.CD',
'DT.ODA.OATL.KD',
'DT.ODA.ODAT.CD',
'DT.ODA.ODAT.GI.ZS',
'DT.ODA.ODAT.GN.ZS',
'DT.ODA.ODAT.KD',
'DT.ODA.ODAT.MP.ZS',
'DT.ODA.ODAT.PC.ZS',
'DT.ODA.ODAT.XP.ZS',
'GE.EST',
'GE.NO.SRC',
'GE.PER.RNK',
'GE.PER.RNK.LOWER',
'GE.PER.RNK.UPPER',
'GE.STD.ERR',
'PV.EST',
'PV.NO.SRC',
'PV.PER.RNK',
'PV.PER.RNK.LOWER',
'PV.PER.RNK.UPPER',
'PV.STD.ERR',
'RQ.EST',
'RQ.NO.SRC',
'RQ.PER.RNK',
'RQ.PER.RNK.LOWER',
'RQ.PER.RNK.UPPER',
'RQ.STD.ERR',
'RL.EST'
]
for indicator in indicators:
    rows = []
    #indicator = 'CC.EST'
    countries = 'AF;AO;BI;BJ;BF;BD;BO;BT;CF;CI;CM;CD;CG;KM;CV;DJ;EG;ER;ET;FM;GH;GN;GM;GW;HN;HT;IN;JO;KE;KG;KH;KI;LA;LB;LR;LK;LS;MA;MG;ML;MM;MZ;MR;MW;NE;NG;NI;NP;PK;PH;PG;KP;PS;RW;SD;SN;SB;SL;SO;SS;ST;SZ;SY;TD;TG;TJ;TL;TN;TZ;UG;UZ;VN;VU;WS;YE;ZM;ZW'
    url = f'https://api.worldbank.org/v2/en/country/{countries}/indicator/{indicator}?format=json&date=1995:2019&per_page=50'

    response = requests.get(url)

    if response.status_code == 200:  # Verifica que la solicitud fue exitosa
        data = response.json()       # Convierte la respuesta JSON a un diccionario de Python
        print(data[0])
    else:
        print(f"Error {response.status_code}: No se pudo obtener los datos.")



    for i in range(2, data[0]['pages'] + 1):
        for row in data[1]:
            rows.append(f"{row['indicator']['id']},{row['country']['id']},{row['date']},{row['value']}")
        
        print(f'Se hace request GET {i} para el indicador {indicator}')
        
        response = requests.get(f'{url}&page={i}')
        if response.status_code == 200:  # Verifica que la solicitud fue exitosa
            data = response.json()       # Convierte la respuesta JSON a un diccionario de Python
        else:
            print(f"Error {response.status_code}: No se pudo obtener los datos.")
            break

    # Abrir un archivo en modo escritura
    with open(f"datos_python{indicator.replace('.','_')}.csv", 'w') as file:
        for item in rows:
            file.write(f"{item}\n")  # Escribir cada elemento en una nueva línea
