from typing import List, Dict, Union

from cfn_resource_provider import ResourceProvider

#
# The request schema defining the Resource Properties
#
request_schema = {
    "type": "object",
    "required": ["Value"],
    "properties": {
        "Value": {
            # WARNING:  uses JSON `array` and `object` NOT python `list` and `dict`
            "type": "string",
            # "pattern": "^[_A-Za-z][A-Za-z0-9_$]*$",  # "string" values only
            # "minLength": 1, "maxLength": 32,
            # "enum": ["ValidOption1", "ValidOption2"]
            # "minimum": 0, maximum: 1,  # "integer" type only
            # "default": "",  # use python natives for "integer" and "boolean" types
            "description": "this value will be made accessible through  Fn::GetAtt, property 'Value'",
        }
    },
}


# TODO: Rename provider to <Name>Provider if you want to use a CloudFormation type like "Custom:<Name>"
class CustomProvider(ResourceProvider):
    def __init__(self):
        super(ResourceProvider, self).__init__()
        self.request_schema = request_schema

    def convert_property_types(self):
        self.heuristic_convert_property_types(self.properties)

    # TODO: Remove override if no complex validation is required
    def is_valid_request(self):
        if not super().is_valid_request():
            return False
        # insert complex validation
        return True

    # TODO: Implement create, update, and delete
    # TODO: Make sure methods are resilient to retries. CF will send two retries, on per minute if it hasn't received a response.
    def create(self):
        """Create the requested object and set a Resource ID.  See `update` for behaviors based on Resource ID."""
        value = self.get("Value")
        self.set_attribute("Value", value)
        # ARNs and IDs are ideal
        self.physical_resource_id = value

    def update(self):
        """Perform one of two update operations:

        1. In-place Update:  Make an update without changing the Resource ID.  On success, the updated Resource is used.
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

    # TODO: If the API call is asynchronous, use this method to check for completion; otherwise delete the override
    def is_ready(self):
        """indicates whether the resource is ready"""
        if self.request_type == 'Create':
            return True
        elif self.request_type == 'Update':
            return True
        elif self.request_type == 'Delete':
            return True
        else:
            raise ValueError(f"No is_ready method for Request Type: {self.request_type}")


provider = CustomProvider()


def handler(request, context):
    return provider.handle(request, context)
