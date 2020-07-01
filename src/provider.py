import os
import logging
from . import cfn_custom_provider

logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))


def handler(request, context):
    # Modify this value to support a custom Custom:: tag
    # Add elif conditions (and additional cfn_*_provider files to support multiple tags
    # see binxio/cfn-certificate-provider for an example
    if request["ResourceType"] == "Custom::Custom":
        return cfn_custom_provider.handler(request, context)
    else:
        raise ValueError(f'No handler found for custom resource {request["ResourceType"]}')
