# -*- coding: utf-8 -*-

def procesar(file):
	f1=open(file, "r")
	contenido=f1.read()
	f1.close()
	lineas=contenido.split("\n")
	f2=open(file+".txt", "w")
	for linea in lineas:
		if linea.find("=")==-1:
			continue #pasamos a la siguiente
		l=linea.split("=")
		l[0]=l[0].replace("\\", "") #quitamos la barra invertida
		l[0]=format(int(l[0]), "x") #convertimos de decimal a hexadecimal
		f2.write(l[0]+" "+l[1]+"\n")
	f2.close()