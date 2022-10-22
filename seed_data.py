from ejemplo.models import Familiar

Familiar(nombre="Laura", direccion="Av. Reforma 745", numero_pasaporte=123123).save()
Familiar(nombre="Alfredo", direccion="Av. Reforma 745", numero_pasaporte=890890).save()
Familiar(nombre="Martha", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Ricardo", direccion="Rio Parana 745", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")