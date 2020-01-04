import extension
from scimschema import validate, load_dict_to_schema
import json
def get_data():
    with open("myuser.txt") as jsonfile:
        return json.load(jsonfile)


validate(data=get_data(), extension_schema_definitions=extension.schema)



# schema = load_dict_to_schema("extension/myuser.json")
# validate(
#     data=get_data(),
#     extension_schema_definitions=schema
# )