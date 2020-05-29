import folium
from csvReader import*
import csvReader as csv
import json



def ajouterMarkers(map, markers, donnees):
    couleurChaud = "orange"
    couleurFroid = "blue"
    iconChaud = "fire"
    iconFroid = "cloud"
    for marker in markers:
        nom, latitude, longitude, station = marker['Nom'], marker['Latitude'], marker['Longitude'], marker['numer_sta']
        position = float(marker["Latitude"])
        positionLong = float(marker["Longitude"])
        if position > 18 and positionLong > -56:
            donneesUneStation = csv.filtrerLigne(donnees,'numer_sta', station) 
            if len(donneesUneStation) > 0:
                donneesUneStation = conversion(donneesUneStation)
                moyenneStation = moyenne(donneesUneStation)
                fichierJson = templateJson(donneesUneStation, nom, moyenneStation )
                if moyenneStation >= moyenneGlobale:
                    couleur = couleurChaud
                    icon = iconChaud
                else:
                    couleur = couleurFroid
                    icon = iconFroid
                icon = folium.Icon(icon=icon, color = couleur)
                popup = folium.Popup().add_child(folium.VegaLite(fichierJson), name = nom)
                folium.Marker(location=[latitude,longitude],
                    popup = popup,
                    icon = icon
                ).add_to(map)
            else:
                print("pas  de donées pour la station {}".format(nom))
            
            print("Station: {} - lat, long [{},{}] - temp. moy. : {}".format(nom, latitude, longitude, moyenneStation))
        

                       

def templateJson(data, titre, moyenne):

    jsonFile = {
        "contains":"padding",
        "type": "fit",
        "description": "Carte des températures",
        "title":titre,
        "data": {
            "values": data
        },
    
        "mark":"line",
        "interpolate": "step-after",
        "stroke":"#008b8b",
        "encoding": { 
            "x": {
                "field":"date",
                "type": "temporal",
                "timeUnit": "yearmonthdayhoursminutessecondes",
                "scale": {"type": "utc"},
                "axis": { "labelAngle": 15 },
                "step": "number",
                "title":"Date"
            },
            "y": {
                "field":"t",
                "type": "quantitative",
                "title": "Température"
            } 
        }
    }
    return jsonFile 

def conversion(inputData):
    outputData = []
    for data in inputData:
        # conversion temperature (sauf quand pas de valeur relevee)
        if data["t"] != "mq":
            data["t"] = float(data["t"]) - 273.15
        # conversion format date pour affichage dans vega-lite
        data["date"] = formatageDate(data["date"])
        outputData.append(data)    
    return outputData

def formatageDate(inputDate):
    listeMois = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    day = inputDate[6:8]
    month = int(inputDate[4:6])
    year = inputDate[0:4]
    hour = inputDate[8:10]
    minutes = inputDate[10:12]
    sec = inputDate[12:14]
    outputDate = '{} {} {} {}:{}:{}'.format(day, listeMois[month - 1], year, hour, minutes, sec)
    return outputDate



def extractionTemperatures(listeDonnees):
    listeTemperatures = []
    for item in listeDonnees:
        chiffre = item["t"]
        if chiffre != "mq":
            listeTemperatures.append(float(chiffre))
    return listeTemperatures

def moyenne(temperatures):
    liste = extractionTemperatures(temperatures)
    moyenneTemperatures = sum(liste)/len(liste)        
    return moyenneTemperatures


def moyenneGlobale(donneesCoordonnees, donneesTemperature):
    stationsAprendreEnCompte =[]
    for station in donneesCoordonnees:
        numeroStation = station["numer_sta"]
        latitudeStation = float(station["Latitude"])
        longitudeStation = float(station["Longitude"])
        temperatures = extractionTemperatures(csv.filtrerLigne(donneesTemperature, "numer_sta", numeroStation))
        if latitudeStation >= 18 and longitudeStation > -56:
            for numero in temperatures:
                stationsAprendreEnCompte.append(numero)
    moyenneDesStations = sum(stationsAprendreEnCompte)/len(stationsAprendreEnCompte)-273.15
    return moyenneDesStations
     



m = folium.Map(location = [47.059167, 2.359833], zoom_start=5)

tablePostesDonnees = csv.importCSV('Postes_Données.csv')
critèrePostesDonnes = ['numer_sta','Nom','Latitude','Longitude','Altitude']
stationsMarkers = csv.filtrerColonne(tablePostesDonnees, critèrePostesDonnes) 


tableauDonneesCsv = importCSV('Données_Février2020.csv')
listeCriteres = ['numer_sta', 't', 'date']
tableauDonneesCsvFiltrees = csv.filtrerColonne(tableauDonneesCsv, listeCriteres) 


moyenneGlobale = moyenneGlobale(stationsMarkers, tableauDonneesCsvFiltrees)



ajouterMarkers(m, stationsMarkers, tableauDonneesCsvFiltrees)
m.save('carte_meteo.html')

















