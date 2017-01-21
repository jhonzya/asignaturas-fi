# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time

archivo = open('CARPETA/archivo.txt', 'w')


for x in xrange(0,10000):
	contenido = urllib2.urlopen("http://inscripciones.ingenieria.unam.mx/consulta_horarios/index.php/horarios/consulta/"+str(x)).read()
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

					archivo.write(str(x)+"#"+clave+"#"+asignatura+"#"+tipo+"#"+grupo+"#"+profesor+"#"+inicio+"#"+fin+"#"+lunes+"#"+martes+"#"+miercoles+"#"+jueves+"#"+viernes+"#"+sabado+"#"+"\n")
	print str(x)
	
archivo.close()