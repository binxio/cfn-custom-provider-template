import os
import logging

from cfn_resource_provider import ResourceProvider

from . import cfn_custom_provider

logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))


def handler(request, context):
    # Modify this value to support a custom Custom:: tag
    # Add elif conditions (and additional cfn_*_provider files to support multiple tags
    # see binxio/cfn-certificate-provider for an example
    if request["ResourceType"] == "Custom::Custom":
        return cfn_custom_provider.handler(request, context)
    else:
        # try to provide reasonable responses to CF request if Resource Type is not supported
        provider = ResourceProvider()
        provider.set_request(request, context)
        if provider.request_type == 'Delete' and provider.physical_resource_id in ['create-not-found', 'deleted']:
            provider.success(f'Clean rollback when provider is not found on create.')
            provider.physical_resource_id = 'deleted'
        elif provider.request_type == 'Create':
            provider.fail(f'Provider not found on create: {request["ResourceType"]}')
            # used to indicate a clean rollback (i.e. no resources needing deleted)
            provider.physical_resource_id = 'create-not-found'
        else:
            provider.fail(f'Provider not found for resource: {request["ResourceType"]}')
        provider.send_response()
        raise KeyError(f'No handler found for resource: {request["ResourceType"]}')
