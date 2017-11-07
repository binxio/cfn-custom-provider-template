import uuid
from provider import handler


def test_create():

    # create
    value = 'v%s' % uuid.uuid4()
    request = Request('Create', value)
    response = handler(request, {})
    assert response['Status'] == 'SUCCESS', response['Reason']
    assert 'PhysicalResourceId' in response
    assert 'Value' in response['Data']
    assert response['Data']['Value'] == value

    # delete
    physical_resource_id = response['PhysicalResourceId']
    request = Request('Delete', value, physical_resource_id)
    assert response['Status'] == 'SUCCESS', response['Reason']


def test_update():

    # create
    value = 'v%s' % uuid.uuid4()
    request = Request('Create', value)
    response = handler(request, {})

    assert response['Status'] == 'SUCCESS', response['Reason']
    assert 'PhysicalResourceId' in response
    assert 'Value' in response['Data']
    assert response['Data']['Value'] == value

    # update to a new value
    new_value = 'new-%s' % value
    physical_resource_id = response['PhysicalResourceId']
    request = Request('Update', new_value, physical_resource_id)
    response = handler(request, {})

    assert response['Status'] == 'SUCCESS', response['Reason']
    assert 'PhysicalResourceId' in response
    assert 'Value' in response['Data']
    assert response['Data']['Value'] == new_value

    # delete the last created
    physical_resource_id = response['PhysicalResourceId']
    request = Request('Delete', new_value, physical_resource_id)
    assert response['Status'] == 'SUCCESS', response['Reason']


class Request(dict):

    def __init__(self, request_type, value, physical_resource_id=None):
        request_id = 'request-%s' % uuid.uuid4()
        self.update({
            'RequestType': request_type,
            'ResponseURL': 'https://httpbin.org/put',
            'StackId': 'arn:aws:cloudformation:us-west-2:EXAMPLE/stack-name/guid',
            'RequestId': request_id,
            'ResourceType': 'Custom::Custom',
            'LogicalResourceId': 'MyCustom',
            'ResourceProperties': {
                'Value': value
            }})

        self['PhysicalResourceId'] = physical_resource_id if physical_resource_id is not None else 'initial-%s' % str(uuid.uuid4())
