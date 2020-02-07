from cfn_resource_provider import ResourceProvider

#
# The request schema defining the Resource Properties
#
request_schema = {
    "type": "object",
    "required": ["Value"],
    "properties": {
        "Value": {
            "type": "string",
            "description": "this value will be made accessible through  Fn::GetAtt, property 'Value'",
        }
    },
}


class CustomProvider(ResourceProvider):
    def __init__(self):
        super(ResourceProvider, self).__init__()
        self.request_schema = request_schema

    def convert_property_types(self):
        self.heuristic_convert_property_types(self.properties)

    def create(self):
        value = self.get("Value")
        self.set_attribute("Value", value)
        self.physical_resource_id = value

    def update(self):
        value = self.get("Value")
        self.set_attribute("Value", value)
        self.physical_resource_id = value

    def delete(self):
        self.success("nothing to do")


provider = CustomProvider()


def handler(request, context):
    return provider.handle(request, context)
