#!/usr/bin/env python3
# coding: utf-8

import requests
import json

clientCrt = "certificado.pem"
clientKey = "chave.pem"

url_aut = "https://val.portalunico.siscomex.gov.br/portal/api/autenticar"
url_geo = "https://val.portalunico.siscomex.gov.br/recintos-ext/api/ext/evento-georreferenciamento"
url_ind = "https://val.portalunico.siscomex.gov.br/recintos-ext/api/ext/indisponibilidade-equipamentos"

payload_aut={}

headers_aut = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Accept-Encoding': 'gzip, deflate, br',
  'Role-Type': 'DEPOSIT'
}

response_aut = requests.request("POST", url_aut, headers=headers_aut, data=payload_aut, cert=(clientCrt, clientKey))

print(url_aut)
print('Consulta Aut Headers: ', response_aut.request.headers)
print('Consulta Aut Method: ', response_aut.request.method)
#print('Consulta Aut Hooks: ', response_aut.request.hooks)
print('Consulta Aut Body: ', response_aut.request.body)
print('Resposta Aut CODE: ', response_aut.status_code)
#print('Resposta Aut Headers: ', response_aut.headers)
#print('Resposta Aut Cookies: ', response_aut.cookies)
#print('Resposta Aut Raw: ', response_aut.raw)
print('Resposta Aut Raw: ', response_aut.text)
timeout_token=response_aut.headers.get('X-CSRF-Token')
auth_token=response_aut.headers.get('Set-Token')
print('X-CSRF-Token (timeout): ', timeout_token)
print('Authorization token: ', auth_token)

payload_geo='{ "tipoOperacao": "I", "idEvento": "string", "dataHoraOcorrencia": "2020-04-01T10:50:30.150-0300", "dataHoraRegistro": "2020-04-01T10:50:30.150-0300", "contingencia": false, "codigoRecinto": "7921302", "idAreaEquipamento": "string", "nome": "string", "areaEquipamentoAtivo": false, "azimuteCamera": 180, "tipo": 6, "listaCoordenadas": [ { "idElemento": "string", "latitude": -22.871284, "longitude": -43.201608 } ] } '

payload_ind='{ "tipoOperacao": "I", "idEvento": "string", "dataHoraOcorrencia": "2020-04-01T10:50:30.150-0300", "dataHoraRegistro": "2020-04-01T10:50:30.150-0300", "contingencia": false, "codigoRecinto": "7921302", "equipamento": "66d24eb1-6ac9-4798-bc93-f4c66eb6fa9b", "disponivel": false, "dataHoraPrevisaoDisponibilidade": "2020-04-01T10:50:30.150-0300", "motivoIndisponibilidade": "string" }'

headers_consult = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Accept-Encoding': 'gzip, deflate, br',
  'Role-Type': 'DEPOSIT',
  'Authorization': auth_token,
  'X-CSRF-Token': timeout_token
}

response_geo = requests.request("POST", url_geo, headers=headers_consult, data=payload_geo)

print('URL: ', url_geo)
#print('Consulta Geo Headers: ', response_geo.request.headers)
print('Consulta Geo Method: ', response_geo.request.method)
#print('Consulta Geo Hooks: ', response_geo.request.hooks)
print('Consulta Geo Body: ', response_geo.request.body)
print('Resposta Geo CODE: ', response_geo.status_code)
#print('Resposta Geo Headers: ', response_geo.headers)
#print('Resposta Geo Cookies: ', response_geo.cookies)
#print('Resposta Geo Raw: ', response_geo.raw)
print('Resposta Geo Text: ', response_geo.text)

response_ind = requests.request("POST", url_ind, headers=headers_consult, data=payload_ind)

print(url_ind)
#print('Constulta Ind Headers: ', response_ind.request.headers)
#print('Consulta Ind Method: ', response_ind.request.method)
print('Consulta Ind Body: ', response_ind.request.body)
print('Resposta Ind CODE: ', response_ind.status_code)
#print('Resposta Ind Headers: ', response_ind.headers)
#print('Resposta Ind Cookies: ', response_ind.cookies)
#print('Resposta Ind Raw: ', response_ind.raw)
print('Resposta Ind Text: ', response_ind.text)
