import json

from scimschema import core_schemas
from scimschema._model.schema_response import ScimResponse

import extension


def get_data():
    with open("myuser.txt") as jsonfile:
        return json.load(jsonfile)

ScimResponse(data=get_data(), core_schema_definitions=core_schemas.schema,
             extension_schema_definitions=extension.schema).validate()

# validate(data=get_data(), extension_schema_definitions=extension.schema)

# schema = load_dict_to_schema("extension/myuser.json")
# validate(
#     data=get_data(),
#     extension_schema_definitions=schema
# )