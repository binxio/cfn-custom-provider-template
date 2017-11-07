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
            "description": "this value will be made accessible through  Fn::GetAtt, property 'Value'"
        }
    }
}


class CustomProvider(ResourceProvider):

    def __init__(self):
        super(ResourceProvider, self).__init__()
        self.request_schema = request_schema

    def convert_property_types(self):
        self.heuristic_convert_property_types(self.properties)

    def create(self):
        self.fail('not yet implemented')
        self.physical_resource_id = 'failed-to-create'
        # use self.set_attribute() to set return values.

    def update(self):
        self.fail('not yet implemented')
        self.physical_resource_id = 'failed-to-create'

    def delete(self):
        self.success('nothing to do')

provider = CustomProvider()


def handler(request, context):
    return provider.handle(request, context)
