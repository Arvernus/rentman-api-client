import yaml

def load_api_spec(file_path):
    """Lädt die OpenAPI-Spezifikation aus einer YAML-Datei."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def sort_api_spec(api_spec, depth=0, max_depth=None):
    """Sortiert die OpenAPI-Spezifikation alphabetisch bis zur n-ten Ebene."""
    if max_depth is not None and depth >= max_depth:
        return api_spec

    sorted_spec = {}
    for key in sorted(api_spec.keys(), key=lambda x: x.lower()):
        if isinstance(api_spec[key], dict):
            sorted_spec[key] = sort_api_spec(api_spec[key], depth=depth+1, max_depth=max_depth)
        else:
            sorted_spec[key] = api_spec[key]
    return sorted_spec

def replace_in_api_spec(api_spec, old_word, new_word, depth=0, max_depth=None, key=None):
    """Ersetzt Wortparen in OpenAPI-Spezifikation bis zur n-ten Ebene."""
    if max_depth is not None and depth >= max_depth:
        return api_spec

    replaced_spec = {}
    for thisKey in api_spec.keys():
        if isinstance(api_spec[thisKey], dict):
            replaced_spec[thisKey] = replace_in_api_spec(api_spec[thisKey], old_word=old_word, new_word=new_word, depth=depth+1, max_depth=max_depth, key=key)
        else:
            if key is None or key == thisKey:
                replaced_spec[thisKey] = api_spec[thisKey].replace(old_word, new_word)
            else:
                replaced_spec[thisKey] = api_spec[thisKey]
    return replaced_spec

def save_api_spec(api_spec, file_path):
    """Speichert die geänderte OpenAPI-Spezifikation in einer YAML-Datei."""
    with open(file_path, 'w') as file:
        yaml.safe_dump(api_spec, file, sort_keys=False)

# Spezifikation laden
api_spec = load_api_spec("oas.yml")
api_spec_man = load_api_spec("oas_manuell.yml")
# Titel ändern
api_spec['info']['title'] = "Rentman API"
# Security hinzufügen
api_spec['components'].update(
    {
        'securitySchemes': {
            'bearerAuth': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT'
            }
        }
    }
)
api_spec['security'] = [{'bearerAuth': []}]
# Replace words in identifiers
word_pairs = [('Accessoire', 'Accessory'),
              ('Afspraakmedewerker', 'AppointmentCrew'),
              ('Afspraak', 'Appointment'),
              ('Person', 'Contactperson'),
              ('Medewerker', 'Crew'),
              ('Beschikbaarheid', 'CrewAvailability'),
              ('Medewerkertarief', 'CrewRates'),
              ('Materiaal', 'Equipment'),
              ('Setinhoud','EquipmentSetsContent'),
              ('Files','File'),
              ('Btwbedrag', 'InvoiceLines'),
              ('Factuur', 'Invoice'),
              ('Grootboek', 'LedgerCode'),
              ('Planningpersoneel', 'ProjectCrew'),
              ('Planningmateriaal', 'ProjectEquipment'),
              ('MateriaalCat', 'ProjectEquipmentGroup'),
              ('Functiegroep', 'ProjectFunctionGroup'),
              ('Functie', 'ProjectFunction'),
              ('Type', 'ProjectType'),
              ('Planningtransport', 'ProjectVehicles'),
              ('Offerte', 'Quote'),
              ('Reparatie', 'Repair'),
              ('Exemplaar', 'SerialNumber'),
              ('AssetLocation', 'StockLocation'),
              ('Voorraadmutatie', 'StockMovement'),
              ('Inhuurmateriaal', 'SubrentalEquipment'),
              ('Inhuurgroep', 'SubrentalEquipmentGroup'),
              ('Inhuur', 'Subrental'),
              ('Uren', 'TimeRegistration'),
              ('Functieuur', 'TimeRegistrationActivity'),
              ('Voertuig', 'Vehicle'),
              ('Afspraakmedewerker', 'AppointmentCrew')
              ]
word_pairs.sort(key=lambda pair: len(pair[0]), reverse=True)
for old_word, new_word in word_pairs:
    component_schemas_to_modify = list(api_spec['components']['schemas'].keys())
    for key in component_schemas_to_modify:
        value = api_spec['components']['schemas'][key]
        new_key = key.replace(old_word, new_word)
        del api_spec['components']['schemas'][key]
        api_spec['components']['schemas'][new_key] = value
    api_spec['paths']=replace_in_api_spec(api_spec=api_spec['paths'],old_word=old_word,new_word=new_word,key='operationId')
    api_spec['paths']=replace_in_api_spec(api_spec=api_spec['paths'],old_word=old_word,new_word=new_word,key='$ref')

# Spezifikation sortiren und speichern
api_spec = sort_api_spec(api_spec)
api_spec_man = sort_api_spec(api_spec_man)
save_api_spec(api_spec, "oas_changed.yml")
