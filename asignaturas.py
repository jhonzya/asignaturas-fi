# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import logging
from config import *

archivo = open("resultados/"+ARCHIVO_DESTINO, 'w')
logging.basicConfig(filename='error.log')

for x in CLAVES:
    # Intenta hacer la petición
    intentos = 0
    contenido = ""
    while intentos < MAXIMO_INTENTOS:
        try:
            contenido = urllib2.urlopen(URL_INSCRIPCIONES + str(x)).read()
            break
        except Exception, e:
            intentos += 1
            continue

    # Valida máximo de intentos
    if intentos >= MAXIMO_INTENTOS:
        error = str(x) + ": Máximo de intentos - " + str(MAXIMO_INTENTOS)
        logging.error(error)
        continue

    soup = BeautifulSoup(contenido, 'html.parser')
    tables = soup.findAll('table')

    for rows in tables:
        for tr in rows:
            if len(tr) > 1:
                cols = tr.findAll('td')
                if len(cols) > 1:
                    vacantes_dos = cols[3].string.encode('utf-8')
                    clave = cols[0].string.encode('utf-8')
                    asignatura = cols[1].string.encode('utf-8')
                    grupo = cols[2].string.encode('utf-8')
                    vacantes = cols[3].string.encode('utf-8')
                    profesor = cols[4].string.encode('utf-8')

                    inicio = cols[5].string.encode('utf-8')
                    fin = cols[6].string.encode('utf-8')

                    lunes = cols[7].center.contents[0].encode('utf-8')
                    martes = cols[8].center.contents[0].encode('utf-8')
                    miercoles = cols[9].center.contents[0].encode('utf-8')
                    jueves = cols[10].center.contents[0].encode('utf-8')
                    viernes = cols[11].center.contents[0].encode('utf-8')
                    sabado = cols[12].center.contents[0].encode('utf-8')

                    tipo = cols[13].string.encode('utf-8')

                    archivo.write(str(x)
                                  + TOKEN + clave
                                  + TOKEN + asignatura
                                  + TOKEN + tipo
                                  + TOKEN + grupo
                                  + TOKEN + profesor
                                  + TOKEN + inicio
                                  + TOKEN + fin
                                  + TOKEN + lunes
                                  + TOKEN + martes
                                  + TOKEN + miercoles
                                  + TOKEN + jueves
                                  + TOKEN + viernes
                                  + TOKEN + sabado
                                  + TOKEN + "\n")
    print str(x)
archivo.close()
