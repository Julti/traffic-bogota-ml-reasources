
import requests

import time

url_count = 'https://sig.simur.gov.co/arcgis/rest/services/Monitoreo/Velocidades_Bitcarrier_2020/FeatureServer/6/query?where=1%3D1&outFields=OBJECTID,FIN,HORA,DISTANCE,TYPE,VEL_PROMEDIO,CUARTO_HORA,DIA_SEMANA,MES,NAME_FROM,NAME_TO,VEL_PONDERADA,CODIGO,COEF_BRT,COEF_MIXTO,VEL_MEDIA_BRT,VEL_MEDIA_MIXTO,VEL_MEDIA_PONDERADA,INICIO,AÑO&returnCountOnly=true&orderByFields=OBJECTID DESC&outSR=4326&f=json'
def getResults(datalen):
    step = 1000
    index = 0
    fileData = open("Julio2020.csv", "a")
    while index<datalen:
        url = "https://sig.simur.gov.co/arcgis/rest/services/Monitoreo/Velocidades_Bitcarrier_2021/FeatureServer/6/query?where=OBJECTID>"+str(index)+"&outFields='*'&returnGeometry=false&orderByFields=OBJECTID ASC&outSR=4326&f=json"
        resp = requests.get(url  )
        if resp.status_code != 200:
        # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))

        json_data = resp.json()
        features = json_data["features"]
        print(len(features),str(index))
        for f in features:
            #print(f)
            #dat = str(f["attributes"]["OBJECTID"])+","+str(f["attributes"]["TID"])+","+str(f["attributes"]["INICIO"])+","+str(f["attributes"]["FIN"])+","+str(f["attributes"]["AÑO"])+","+str(f["attributes"]["HORA"])+","+str(f["attributes"]["DISTANCE"])+","+str(f["attributes"]["TYPE"])+","+str(f["attributes"]["VEL_PROMEDIO"])+","+str(f["attributes"]["CUARTO_HORA"])+","+str(f["attributes"]["DIA_SEMANA"])+","+str(f["attributes"]["MES"])+","+str(f["attributes"]["NAME_FROM"])+","+str(f["attributes"]["NAME_TO"])+","+str(f["attributes"]["VEL_PONDERADA"])+","+str(f["attributes"]["CODIGO"])+","+str(f["attributes"]["COEF_BRT"])+","+str(f["attributes"]["COEF_MIXTO"])+","+str(f["attributes"]["VEL_MEDIA_BRT"])+","+str(f["attributes"]["VEL_MEDIA_MIXTO"])+","+str(f["attributes"]["VEL_MEDIA_PONDERADA"])+","+str(f["attributes"]["SHAPE.LEN"])+"\n"
            dat = str(f["attributes"]["OBJECTID"])+"|"+str(f["attributes"]["TID"])+"|"+str(f["attributes"]["INICIO"])+"|"+str(f["attributes"]["FIN"])+"|"+str(f["attributes"]["AÑO"])+"|"+str(f["attributes"]["HORA"])+"|"+str(f["attributes"]["DISTANCE"])+"|"+str(f["attributes"]["TYPE"])+"|"+str(f["attributes"]["VEL_PROMEDIO"])+"|"+str(f["attributes"]["CUARTO_HORA"])+"|"+str(f["attributes"]["DIA_SEMANA"])+"|"+str(f["attributes"]["MES"])+"|"+str(f["attributes"]["NAME_FROM"])+"|"+str(f["attributes"]["NAME_TO"])+"||"+str(f["attributes"]["CODIGO"])+"|"+str(f["attributes"]["COEF_BRT"])+"|"+str(f["attributes"]["COEF_MIXTO"])+"|"+str(f["attributes"]["VEL_MEDIA_BRT"])+"|"+str(f["attributes"]["VEL_MEDIA_MIXTO"])+"|"+str(f["attributes"]["VEL_MEDIA_PONDERADA"])+"|"+str(f["attributes"]["SHAPE.LEN"])+"\n"
            fileData.write(dat)
        time.sleep(2)
        index = index+step
    fileData.close()
def get_count():
    resp = requests.get(url_count)
    if resp.status_code != 200:
    # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    json_data = resp.json()
    print(json_data["count"])
    return int(json_data["count"])
if __name__=="__main__":
    total=get_count()
    getResults(total)