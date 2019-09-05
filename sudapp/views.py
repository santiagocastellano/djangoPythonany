from django.shortcuts import render
from funcs.func_genericas import *
import json
from django.conf import settings
from suds.client import Client
from django.http import JsonResponse
from suds.sudsobject import asdict
from django.http import HttpResponse
def vistaAdministradora(request):
    return render(request, 'base/index.html', {})

def traduccion_recursiva(d):
    result = {}
    for k, v in asdict(d).items():
        if hasattr(v, '__keylist__'):
            result[k] = traduccion_recursiva(v)
        elif isinstance(v, list):
            result[k] = []
            for item in v:
                if hasattr(item, '__keylist__'):
                    result[k].append(traduccion_recursiva(item))
                else:
                    result[k].append(item)
        else:
            result[k] = v
    return result
#######################################################################
def consultarDelimitaciones(request):
    delimitaciones = request.GET.get('delimitaciones')
    x = request.GET.get('x')
    y = request.GET.get('y')
    soaphost = settings.CLIENT_SOAP_HOST

    try:
        conexion = getSOAPClient(soaphost).service.consultarDelimitaciones(x, y, delimitaciones)
        jsonresponse = traduccion_recursiva(conexion)

    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}

    return JsonResponse(jsonresponse, safe=False)
###########################################################################################
#no se puede usar la recursiva porque devuelve un solo string
def consultarDelimitacion(request):
    delimitacion = request.GET.get('delimitacion')
    x = request.GET.get('x')
    y = request.GET.get('y')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.consultarDelimitacion(delimitacion,x,y)
        jsonresponse = {'Delimitacion': conexion}
    except Exception as error:
        jsonresponse = 'Parametros incorrectos'
    return JsonResponse(jsonresponse, safe=False)
###########################################################################################
def delimitacionesDisponibles(request):
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.delimitacionesDisponibles()
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = 'Parametros incorrectos '+str(error)

    return JsonResponse(jsonresponse, safe=False)

#######################################################
def delDir(request):
    delimitaciones = request.GET.get('delimitaciones')
    calle = request.GET.get('calle')
    altura = request.GET.get('altura')
    autodesambiguar = request.GET.get('autoDesambiguar')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service. consultarDelimitacionesPorDireccion(calle,altura,delimitaciones,autodesambiguar)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)
########################################################################################
def todasLasRegiones(request):
    delimitacion = request.GET.get('delimitacion')
    print(delimitacion)
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.obtenerTodasLasRegiones(delimitacion)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}

    return JsonResponse(jsonresponse, safe=False)
####################################################################################
def deldirDesamb(request):
    delimitaciones = request.GET.get('delimitaciones')
    calle = request.GET.get('calle')
    altura = request.GET.get('altura')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.consultarDelimitacionesPorDireccionYDesambiguar(calle, altura, delimitaciones)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)
###################################################################################
#no se usa la recursiva porque entrega un solo dato
def obtenerIdCuadraPorCodCalleAltura(request):
    print('obtenerIdCuadraPorCodCalleAltura')
    codCalle = request.GET.get('codCalle')
    altura = request.GET.get('altura')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.obtenerIdCuadraPorCodCalleAltura(codCalle,altura)
        jsonresponse = {'IdCuadra': conexion}
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}

    return JsonResponse(jsonresponse, safe=False)
#################################################################################
def obtenerIdCuadraPor2CodigosDeCalle(request):
    codCalle1 = request.GET.get('codCalle1')
    codCalle2 = request.GET.get('codCalle2')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.obtenerIdCuadraPor2CodigosDeCalle(codCalle1, codCalle2)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}

    return JsonResponse(jsonresponse, safe=False)
#####################################################################################
#no se usa la recursiva porque entrega un solo parametro
def obtenerIdCuadraPorDireccion(request):
    calle = request.GET.get('calle')
    altura = request.GET.get('altura')
    autoDesambiguar = request.GET.get('autoDesambiguar')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.obtenerIdCuadraPorDireccion(calle, altura, autoDesambiguar)
        jsonresponse = {'Id':conexion}
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)


####################################################################################
def obtenerRecorridoMismaCallePorAltura(request):
    codCalleMisma = request.GET.get('codCalle')
    altura1Misma = request.GET.get('altura1')
    altura2Misma = request.GET.get('altura2')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.obtenerRecorridoMismaCallePorAltura(codCalleMisma, altura1Misma, altura2Misma)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)

#################################################################################
def obtenerTodasLasCalles(request):
    prefijo = request.GET.get('prefijo')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.obtenerTodasLasCalles(prefijo)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)

################################################################################
def obtenerTramosDeCallesDentroDeRadio(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    radio = request.GET.get('radio')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.obtenerTramosDeCallesDentroDeRadio(x,y,radio)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)

###############################################################################
def obtenerClasesDeLugares(request):

    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.obtenerClasesDeLugares()
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)

###############################################################################
def buscarLugar(request):
    str = request.GET.get('str')
    clases = request.GET.get('clases')
    limite = request.GET.get('limite')
    desplazamiento = request.GET.get('desplazamiento')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.buscarLugar(str, clases, limite, desplazamiento)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)

################################################################################
def buscarLugarPorPerfil(request):
    str = request.GET.get('str')
    clases = request.GET.get('clases')
    clasificadores_clases = request.GET.get('clasificadores_clases')
    perfil = request.GET.get('perfil')
    limite = request.GET.get('limite')
    desplazamiento = request.GET.get('desplazamiento')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.buscarLugar(str, clases,clasificadores_clases, perfil, limite, desplazamiento)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrerctos'}
    return JsonResponse(jsonresponse, safe=False)

##################################################################################

def obtenerSMPPorPuerta(request):
    codCalle = request.GET.get('codCalle')
    altura = request.GET.get('altura')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.obtenerSMPPorPuerta(codCalle, altura)
        jsonresponse = {'SMP': conexion}
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)
##################################################################################
def convertirCoordenadas(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    formatoSalida = request.GET.get('formatoSalida')
    soaphost = settings.CLIENT_SOAP_HOST
    try:
        conexion = getSOAPClient(soaphost).service.ConvertirCoordenadas(x, y, formatoSalida)
        jsonresponse = traduccion_recursiva(conexion)
    except Exception as error:
        jsonresponse = {'ERROR':'Parametros incorrectos'}
    return JsonResponse(jsonresponse, safe=False)
