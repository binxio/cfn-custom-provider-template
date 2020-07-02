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
            # "minimum": 0, "maximum": 1,  # "integer" type only
            # "default": "",  # use python natives for "integer" and "boolean" types
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
        """Create the requested object and set a Resource ID.  See `update` for behaviors based on Resource ID."""
        value = self.get("Value")
        self.set_attribute("Value", value)
        # ARNs and IDs are ideal
        self.physical_resource_id = value

    def update(self):
        """Perform one of two update operations:

        1. In-place Update:  Make an update without changing the Resource ID.  On success, the new Resource is used.
           On failure, `update` is called again with the original parameters.
        2. Replacement:  Create a new object and return a new Resource ID.  On success, `delete` is called with the old
           Resource ID.  On failure, `delete` is called with the new Resource ID.
        """
        value = self.get("Value")
        self.set_attribute("Value", value)
        self.physical_resource_id = value

    def delete(self):
        """Remove the object indicated by the Resource ID."""
        self.success("nothing to do")


provider = CustomProvider()


def handler(request, context):
    return provider.handle(request, context)
