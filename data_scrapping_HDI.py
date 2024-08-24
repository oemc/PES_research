import requests

countries = [
("AFG","AF"),("AGO","AO"),("BDI","BI"),("BEN","BJ"),("BFA","BF"),("BGD","BD"),("BOL","BO"),("BTN","BT"),("CAF","CF"),("CIV","CI"),("CMR","CM"),("COD","CD"),("COG","CG"),("COM","KM"),("CPV","CV"),("DJI","DJ"),("EGY","EG"),("ERI","ER"),("ETH","ET"),("FSM","FM"),("GHA","GH"),("GIN","GN"),("GMB","GM"),("GNB","GW"),("HND","HN"),("HTI","HT"),("IND","IN"),("JOR","JO"),("KEN","KE"),("KGZ","KG"),("KHM","KH"),("KIR","KI"),("LAO","LA"),("LBN","LB"),("LBR","LR"),("LKA","LK"),("LSO","LS"),("MAR","MA"),("MDG","MG"),("MLI","ML"),("MMR","MM"),("MOZ","MZ"),("MRT","MR"),("MWI","MW"),("NER","NE"),("NGA","NG"),("NIC","NI"),("NPL","NP"),("PAK","PK"),("PHL","PH"),("PNG","PG"),("PRK","KP"),("PSE","PS"),("RWA","RW"),("SDN","SD"),("SEN","SN"),("SLB","SB"),("SLE","SL"),("SOM","SO"),("SSD","SS"),("STP","ST"),("SWZ","SZ"),("SYR","SY"),("TCD","TD"),("TGO","TG"),("TJK","TJ"),("TLS","TL"),("TUN","TN"),("TZA","TZ"),("UGA","UG"),("UZB","UZ"),("VNM","VN"),("VUT","VU"),("WSM","WS"),("YEM","YE"),("ZMB","ZM"),("ZWE","ZW")
]

years = '1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019'

rows = []
    
for country in countries:
    print(f'Se hace request GET para el pais {country[0]}')
    url = f'https://hdrdata.org/api/CompositeIndices/query?apikey=HDR-WTPcQXXuQaeFXS7Id03lsDQRxNoeMNXe&countryOrAggregation={country[0]}&year={years}'

    response = requests.get(url)

    if response.status_code == 200:  # Verifica que la solicitud fue exitosa
        data = response.json()       # Convierte la respuesta JSON a un diccionario de Python
    else:
        print(f"Error {response.status_code}: No se pudo obtener los datos.")


    for record in data:
        rows.append(f"{country[0]},{country[1]},{record['indicator'].split()[0]},{record['year']},{record['value']}")
        
# Abrir un archivo en modo escritura
with open(f"datos_python_HDI.csv", 'w') as file:
    for item in rows:
        file.write(f"{item}\n")  # Escribir cada elemento en una nueva línea
