import xmlrpc.client

url = 'http://localhost:8069'
db = 'refy_odoo'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
tt = models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})

s = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', False]]])

s = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', False]]])

ids = models.execute_kw(db, uid, password, 'crm.lead', 'search', [[]], {})
records = models.execute_kw(db, uid, password, 'crm.lead', 'read', [ids])

models.execute_kw(db, uid, password, 'crm.lead', 'write', [[2], {'refy_application_answers': "<table border=1 class=\"stocktable\" id=\"table1\"><tr><th>Question</th><th>Answer</th></tr><tr><td>\u00bfAceptas nuestros t\u00e9rminos y condiciones?</td><td>True</td></tr><tr><td>\u00bfQu\u00e9 est\u00e1s buscando?</td><td>Comprar mi primera propiedad</td></tr><tr><td>\u00bfCon qu\u00e9 objetivo quieres comprar la propiedad?</td><td>Vivienda, para vivir en ella</td></tr><tr><td>\u00bfQu\u00e9 tipo de propiedad es la que quieres financiar o refinanciar?</td><td>Departamento</td></tr><tr><td>\u00bfYa encontraste una propiedad?</td><td>S\u00ed, ya tengo la promesa firmada</td></tr><tr><td>\u00bfEn qu\u00e9 regi\u00f3n est\u00e1 ubicada la propiedad?</td><td>Metropolitana</td></tr><tr><td>\u00bfEn qu\u00e9 comuna?</td><td>Providencia</td></tr><tr><td>\u00bfEl inmueble es nuevo o usado?</td><td>Nuevo</td></tr><tr><td>\u00bfCu\u00e1l es la fecha de entrega del proyecto?</td><td>Entrega inmediata</td></tr><tr><td>\u00bfQu\u00e9 tipo de empleo tienes?</td><td>Tengo contrato indefinido</td></tr><tr><td>\u00bfQu\u00e9 tipo de renta tienes?</td><td>100% fija</td></tr><tr><td>\u00bfHace cu\u00e1nto tiempo tienes este empleo?</td><td>M\u00e1s de 2 a\u00f1os</td></tr><tr><td>\u00bfCu\u00e1l es tu sueldo l\u00edquido en pesos chilenos?</td><td>7000000</td></tr><tr><td>\u00bfTienes alguna otra fuente de ingresos comprobable?</td><td>No</td></tr><tr><td>\u00bfComplementas la renta con alguien?</td><td>No</td></tr><tr><td>Ingresa el valor de la propiedad en UF </td><td>5000</td></tr><tr><td>Ingresa el monto del pie del cr\u00e9dito en UF</td><td>2500</td></tr><tr><td>\u00bfQu\u00e9 tipo de tasa quieres para tu cr\u00e9dito?</td><td>Fija</td></tr><tr><td>\u00bfA qu\u00e9 plazo quieres el cr\u00e9dito?</td><td>20 a\u00f1os</td></tr><tr><td>\u00bfTienes alg\u00fan tipo de deuda?</td><td>No</td></tr><tr><td>\u00bfCu\u00e1l es tu nombre?</td><td>Test Ignacio Odoo</td></tr><tr><td>\u00bfCu\u00e1l es tu apellido?</td><td>Test Odoo</td></tr><tr><td>\u00bfQu\u00e9 edad tienes?</td><td>40</td></tr><tr><td>\u00bfCu\u00e1l es tu n\u00famero de tel\u00e9fono?</td><td>+56995996495</td></tr><tr><td>\u00bfPor d\u00f3nde prefieres que te contactemos?</td><td>Whatsapp</td></tr><tr><td>\u00bfCu\u00e1l es tu Rut?</td><td>15372170-K</td></tr></table>"}])
models.execute_kw(db, uid, password, 'crm.lead', 'write', [[2], {'refy_core_assessment_html_summary': '<h6>Metlife<h6/><ul><li><p>ltv:<font style="color: green">El monto a financiar es razonable con respecto al valor de la propiedad</font></p></li><li><p>debt:<font style="color: green">Tu nivel de endeudamiento es muy bajo, felicitaciones</font></p></li><li><p>solvency:<font style="color: green">Tu capacidad para pagar el dividendo estimado es buena</font></p></li><li><p>employment:<font style="color: green">Tienes un trabajo estable hace bastante tiempo</font></p></li></ul><h6>Evoluciona<h6/><ul><li><p>ltv:<font style="color: green">El monto a financiar es razonable con respecto al valor de la propiedad</font></p></li><li><p>debt:<font style="color: green">Tu nivel de endeudamiento es muy bajo, felicitaciones</font></p></li><li><p>solvency:<font style="color: green">Tu capacidad para pagar el dividendo estimado es buena</font></p></li><li><p>employment:<font style="color: red">No tienes la estabilidad laboral necesaria como para conseguir un crédito por el momento</font></p></li></ul><h6>BancoEstado<h6/><ul><li><p>ltv:<font style="color: green">El monto a financiar es razonable con respecto al valor de la propiedad</font></p></li><li><p>debt:<font style="color: green">Tu nivel de endeudamiento es muy bajo, felicitaciones</font></p></li><li><p>solvency:<font style="color: green">Tu capacidad para pagar el dividendo estimado es buena</font></p></li><li><p>employment:<font style="color: green">Tienes un trabajo estable hace bastante tiempo</font></p></li></ul><h6>BancoSecurity<h6/><ul><li><p>ltv:<font style="color: green">El monto a financiar es razonable con respecto al valor de la propiedad</font></p></li><li><p>debt:<font style="color: green">Tu nivel de endeudamiento es muy bajo, felicitaciones</font></p></li><li><p>solvency:<font style="color: green">Tu capacidad para pagar el dividendo estimado es buena</font></p></li><li><p>employment:<font style="color: green">Tienes un trabajo estable hace bastante tiempo</font></p></li></ul><h6>BancoConsorcio<h6/><ul><li><p>ltv:<font style="color: green">El monto a financiar es razonable con respecto al valor de la propiedad</font></p></li><li><p>debt:<font style="color: green">Tu nivel de endeudamiento es muy bajo, felicitaciones</font></p></li><li><p>solvency:<font style="color: green">Tu capacidad para pagar el dividendo estimado es buena</font></p></li><li><p>employment:<font style="color: green">Tienes un trabajo estable hace bastante tiempo</font></p></li></ul><h6>BancoFalabella<h6/><ul><li><p>ltv:<font style="color: green">El monto a financiar es razonable con respecto al valor de la propiedad</font></p></li><li><p>debt:<font style="color: green">Tu nivel de endeudamiento es muy bajo, felicitaciones</font></p></li><li><p>solvency:<font style="color: green">Tu capacidad para pagar el dividendo estimado es buena</font></p></li><li><p>employment:<font style="color: green">Tienes un trabajo estable hace bastante tiempo</font></p></li></ul><h6>BancoSantander<h6/><ul><li><p>ltv:<font style="color: green">El monto a financiar es razonable con respecto al valor de la propiedad</font></p></li><li><p>debt:<font style="color: green">Tu nivel de endeudamiento es muy bajo, felicitaciones</font></p></li><li><p>solvency:<font style="color: green">Tu capacidad para pagar el dividendo estimado es buena</font></p></li><li><p>employment:<font style="color: green">Tienes un trabajo estable hace bastante tiempo</font></p></li></ul><h6>BiceHipotecaria<h6/><ul><li><p>ltv:<font style="color: green">El monto a financiar es razonable con respecto al valor de la propiedad</font></p></li><li><p>debt:<font style="color: green">Tu nivel de endeudamiento es muy bajo, felicitaciones</font></p></li><li><p>solvency:<font style="color: green">Tu capacidad para pagar el dividendo estimado es buena</font></p></li><li><p>employment:<font style="color: green">Tienes un trabajo estable hace bastante tiempo</font></p></li></ul><h6>BancoInternacional<h6/><ul><li><p>ltv:<font style="color: green">El monto a financiar es razonable con respecto al valor de la propiedad</font></p></li><li><p>debt:<font style="color: green">Tu nivel de endeudamiento es muy bajo, felicitaciones</font></p></li><li><p>solvency:<font style="color: green">Tu capacidad para pagar el dividendo estimado es buena</font></p></li><li><p>employment:<font style="color: green">Tienes un trabajo estable hace bastante tiempo</font></p></li></ul>'}])


jj = models.execute_kw(db, uid, password, 'crm.lead', 'fields_get', [], {'attributes': ['string', 'help', 'type']})

user_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "Ignacio Pérez"}])


id = models.execute_kw(db, uid, password, 'crm.lead', 'create', [{'name': "Ignacio Pérez Contact", 'type': 'opportunity', 'refy_score': '80', 'partner_id': f'{user_id}'}])

info = xmlrpc.client.ServerProxy('http://localhost:8069/start').start()
url, db, username, password = info['host'], info['database'], info['user'], info['password']
