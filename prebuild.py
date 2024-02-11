import yaml


def custom_scalar_constructor(loader, node):
    value = loader.construct_scalar(node)
    if value.lower() == "yes":
        return "yes"
    elif value.lower() == "no":
        return "no"
    else:
        return loader.construct_yaml_bool(node)


def load_api_spec(file_path):
    """Lädt die OpenAPI-Spezifikation aus einer YAML-Datei."""
    with open(file_path, "r") as file:
        yaml.SafeLoader.add_constructor(
            "tag:yaml.org,2002:bool", custom_scalar_constructor
        )
        return yaml.safe_load(file)


def sort_api_spec(api_spec: dict, depth=0, max_depth: int = None):
    """Sortiert die OpenAPI-Spezifikation alphabetisch bis zur n-ten Ebene."""
    if max_depth is not None and depth >= max_depth:
        return api_spec

    sorted_spec = {}
    for key in sorted(api_spec.keys(), key=lambda x: x.lower()):
        if isinstance(api_spec[key], dict):
            sorted_spec[key] = sort_api_spec(
                api_spec[key], depth=depth + 1, max_depth=max_depth
            )
        else:
            sorted_spec[key] = api_spec[key]
    return sorted_spec


def replace_in_api_spec(
    api_spec: dict,
    old_word: str,
    new_word: str,
    depth=0,
    max_depth: int = None,
    key: str = None,
):
    """Ersetzt Wortpaaren in OpenAPI-Spezifikation bis zur n-ten Ebene."""
    if max_depth is not None and depth >= max_depth:
        return api_spec

    replaced_spec = {}
    for thisKey in api_spec.keys():
        if isinstance(api_spec[thisKey], dict):
            replaced_spec[thisKey] = replace_in_api_spec(
                api_spec[thisKey],
                old_word=old_word,
                new_word=new_word,
                depth=depth + 1,
                max_depth=max_depth,
                key=key,
            )
        else:
            if key is None or key == thisKey:
                replaced_spec[thisKey] = api_spec[thisKey].replace(old_word, new_word)
            else:
                replaced_spec[thisKey] = api_spec[thisKey]
    return replaced_spec


def delete_in_api_spec(api_spec: dict, key: str, max_depth: int = None, depth=0):
    """Entfernt ein Schlüssel in OpenAPI-Spezifikation bis zur n-ten Ebene."""
    if max_depth is not None and depth >= max_depth:
        return api_spec

    deleted_spec = {}
    for thisKey in api_spec.keys():
        if isinstance(api_spec[thisKey], dict):
            deleted_spec[thisKey] = delete_in_api_spec(
                api_spec[thisKey], key=key, depth=depth + 1, max_depth=max_depth
            )
        else:
            if thisKey != key:
                deleted_spec[thisKey] = api_spec[thisKey]
    return deleted_spec


def save_api_spec(api_spec, file_path):
    """Speichert die geänderte OpenAPI-Spezifikation in einer YAML-Datei."""
    with open(file_path, "w") as file:
        yaml.safe_dump(api_spec, file, sort_keys=False)


# Spezifikation laden
api_spec = load_api_spec("oas.yml")
# Titel ändern
api_spec["info"]["title"] = "Rentman API"
# Server anpassen
api_spec["servers"] = [{"url": "https://api.rentman.net", "description": "url"}]
# JSON Schema Dialect hinzufügen
api_spec["jsonSchemaDialect"] = "http://json-schema.org/draft-04/schema"
api_spec = delete_in_api_spec(api_spec, "$schema")
# Security hinzufügen
api_spec["components"].update(
    {
        "securitySchemes": {
            "bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
        }
    }
)
api_spec["security"] = [{"bearerAuth": []}]
# Replace words in identifiers
word_pairs = [
    ("Accessoire", "Accessory"),
    ("Afspraakmedewerker", "AppointmentCrew"),
    ("Afspraak", "Appointment"),
    ("Person", "ContactPerson"),
    ("Medewerker", "Crew"),
    ("Beschikbaarheid", "CrewAvailability"),
    ("Medewerkertarief", "CrewRates"),
    ("Materiaal", "Equipment"),
    ("Setinhoud", "EquipmentSetsContent"),
    ("Files", "File"),
    ("Btwbedrag", "InvoiceLines"),
    ("Factuur", "Invoice"),
    ("Grootboek", "LedgerCode"),
    ("Planningpersoneel", "ProjectCrew"),
    ("Planningmateriaal", "ProjectEquipment"),
    ("MateriaalCat", "ProjectEquipmentGroup"),
    ("Functiegroep", "ProjectFunctionGroup"),
    ("Functie", "ProjectFunction"),
    ("Type", "ProjectType"),
    ("Planningtransport", "ProjectVehicles"),
    ("Offerte", "Quote"),
    ("Reparatie", "Repair"),
    ("Exemplaar", "SerialNumber"),
    ("AssetLocation", "StockLocation"),
    ("Voorraadmutatie", "StockMovement"),
    ("Inhuurmateriaal", "SubRentalEquipment"),
    ("Inhuurgroep", "SubRentalEquipmentGroup"),
    ("Inhuur", "SubRental"),
    ("Uren", "TimeRegistration"),
    ("Functieuur", "TimeRegistrationActivity"),
    ("Voertuig", "Vehicle"),
    ("Afspraakmedewerker", "AppointmentCrew"),
]
word_pairs.sort(key=lambda pair: len(pair[0]), reverse=True)
for old_word, new_word in word_pairs:
    component_schemas_to_modify = list(api_spec["components"]["schemas"].keys())
    for key in component_schemas_to_modify:
        value = api_spec["components"]["schemas"][key]
        new_key = key.replace(old_word, new_word)
        del api_spec["components"]["schemas"][key]
        api_spec["components"]["schemas"][new_key] = value
    api_spec["paths"] = replace_in_api_spec(
        api_spec=api_spec["paths"],
        old_word=old_word,
        new_word=new_word,
        key="operationId",
    )
    api_spec["paths"] = replace_in_api_spec(
        api_spec=api_spec["paths"], old_word=old_word, new_word=new_word, key="$ref"
    )
queryLimit = {
    "in": "query",
    "name": "limit",
    "schema": {
        "type": "integer",
        "minimum": 0,
        "default": 300,
        "maximum": 300,
    },
    "required": False,
    "description": "The number of items to return.",
}
queryOffset = {
    "in": "query",
    "name": "offset",
    "schema": {
        "type": "integer",
        "minimum": 0,
        "default": 0,
    },
    "required": False,
    "description": "The number of items to skip before starting to collect the result set.",
}
parameters = api_spec["components"].get("parameters", {})
parameters["queryLimit"] = queryLimit
parameters["queryOffset"] = queryOffset
api_spec["components"]["parameters"] = parameters
for path in api_spec["paths"]:
    for operation in api_spec["paths"][path]:
        if operation == "get":
            new_parameters = api_spec["paths"][path][operation].get("parameters", [])
            new_parameters.append({"$ref": "#/components/parameters/queryLimit"})
            new_parameters.append({"$ref": "#/components/parameters/queryOffset"})
            api_spec["paths"][path][operation]["parameters"] = new_parameters

# Spezifikation sortieren und speichern
api_spec = sort_api_spec(api_spec)
save_api_spec(api_spec, "oas_changed.yml")
