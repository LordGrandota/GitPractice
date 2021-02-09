# -*- coding: utf-8 -*-
import json
import os
import clasechida

def existeelgrafo():
	existe=clasechida.existegrafo()

	return existe


def autoguard():
	
	contador=0
	while(contador!=1):
		os.system('cls')
		print("------Menu Guardar Cambios-----\n")
		opc=input("Si desea guardar sus cambios en el archivo Json, presione 1, si no desea guardarlos, presione 2 para continuar\nSi guarda sus cambios, se sobreescribira la informacion que tiene actualmente en su archivo\n")
		if opc == '1':
			clasechida.guardar()
			print("Sus cambios han sido guardados con exito\n")
			os.system('pause')
			contador=1
		elif opc=='2':
			contador = 1
		else:
			print("Opcion incorrecta, recuerde teclear el numero de las opciones mostradas\n")
			os.system('pause')

def agregar():
	
	contador=0
	while(contador!=1):
		os.system('cls')
		print("------Menu Agregar-----\n")

		opc=input("Teclee el numero de la opcion que desee:\n1)Agregar aristas\n2)Agregar vertices\n3)Regresar al menu anterior\n")
		if opc=='1':
			clasechida.agregar_aristasypeso()
			autoguard()

		elif opc=='2':

			clasechida.agregar_masvertices()
			autoguard()

		elif opc=='3':

			contador = 1
		else:
			print("Opcion incorrecta, recuerde teclear el numero de las opciones mostradas\n")
			os.system('pause')

def quitar():
	
	contador=0
	while(contador!=1):
		os.system('cls')
		print("------Menu Quitar-----\n")

		opc=input("Teclee el numero de la opcion que desee:\n1)Quitar aristas\n2)Quitar vertices\n3)Regresar al menu\n")

		if opc=='1':

			clasechida.quitar_aristas()
			autoguard()

		elif opc=='2':

			clasechida.quitar_vertices()
			autoguard()

		elif opc=='3':

			contador = 1
		else:
			print("Opcion incorrecta, recuerde teclear el numero de las opciones mostradas\n")
			os.system('pause')

def modificargrafo():
	
	contador=0
	while(contador!=1):
		os.system('cls')
		print("------Menu Modificar Grafo-----\n")
		opc= input("1)Agregar vertices o aristas\n2)Quitar vertices o aristas\n3)Regresar al menu\n")
		if opc=='1':

			agregar()
			
		elif opc=='2':

			quitar()
			
		elif opc=='3':

			contador = 1

		else:

			print("Opcion incorrecta, recuerde teclear el numero de las opciones mostradas\n")
			os.system('pause')


def menumostrarmodificar():
	contador=0
	while(contador!=1):
		os.system('cls')
		print("------Menu Mostrar o Modificar-----\n")
		print("Elija una de las siguientes opciones:.\n")
		opc=input("1)Mostrar Grafo\n2)Modificar Grafo\n3)Regresar al menu\n")
		if opc=='1':

			clasechida.mostrar_grafo()

		elif opc=='2':

			modificargrafo()

		elif opc=='3':

			contador = 1

		else:
			print("Opcion incorrecta, recuerde teclear el numero de las opciones mostradas\n")
			os.system('pause')


def menu():
	contador=0
	while(contador!=1):
		os.system('cls')
		print("------Menu Principal-----\n")

		print("Bienvenido al algoritmo de Dijkstra.\nElija una de las siguientes opciones:.\n")
		opc=input("1)Crear un nuevo Grafo\n2)Cargar un grafo existente de un archivo json\n3)Mostrar/Modificar grafo\n4)Guardar su grafo o cambios del mismo en un archivo json\n5)Algoritmos Dijkstra, Prim y Kruskal\n6)Salir\n")
		
		if opc=='1':
			
			clasechida.agregar_vertices()
			clasechida.agregar_aristasypeso()
			autoguard()

		elif opc=='2':

			opc=input("Si carga un grafo desde el archivo Json perdera todos los cambios no guardados.\nSi esta seguro de cargar el archivo, presione 1, de lo contrario presione 2 para regresar al menu\n")

			if(opc=='1'):
				clasechida.cargar()
				os.system('cls')

			elif(opc=='2'):
				menu()

			else:
				print("Opcion in")

		elif opc=='3':

			if(existeelgrafo()!=0):
				menumostrarmodificar()
			else:
				print("Actualmente no existe un grafo, porfavo cargue o cree uno para poder acceder a esta funcion\n")
				os.system('pause')

		elif opc=='4':

			if(existeelgrafo()!=0):

				opc=input("Si desea guardar sus cambios en el archivo Json, presione 1, si no desea guardarlos, presione 2 para regresar al menu\nSi guarda sus cambios, se sobreescribira la informacion que tiene actualmente en su archivo\n")

				if(opc=='1'):
					clasechida.guardar()
					os.system('cls')

				elif(opc=='2'):
					menu()

				else:
					print("Opcion incorrecta, recuerde teclear el numero de las opciones mostradas\n")

				
			else:
				print("Actualmente no existe un grafo, porfavo cargue o cree uno para poder acceder a esta funcion\n")
				os.system('pause')
	
			

		elif opc=='5':
			if(existeelgrafo()!=0):
				print("------Algoritmos-----\n")

				opc=input("Teclee el numero de la opcion que desee:\n1)Algoritmo Dijkstra\n2)Algoritmo Prim\n3)Algoritmo Kruskal\n4)Regresar al menu\n")
				if opc=='1':
					d=clasechida.caminocorto("","",0,[],"",{},{})
					os.system('pause')  
				elif opc=='2':
					print("")
					clasechida.prim("",[],[],"",[],0,1)
					os.system('pause') 

				elif opc=='3':
					print("")
					clasechida.kruskal()
					os.system('pause') 

				elif opc=='4':
					menu()
				else:
					print("Opcion incorrecta, recuerde teclear el numero de las opciones mostradas\n")

			else:
				print("Actualmente no existe un grafo, porfavo cargue o cree uno para poder acceder a esta funcion\n")
				os.system('pause')

			
			
		elif opc=='6':

			print("Hasta luego")
			contador=1

		else:

			print("Opcion incorrecta, recuerde teclear el numero de las opciones mostradas\n")
			os.system('pause')  


menu()