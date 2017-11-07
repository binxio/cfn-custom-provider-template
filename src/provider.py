import os
import logging
import cfn_custom_provider

logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))


def handler(request, context):
    return cfn_custom_provider.handler(request, context)
