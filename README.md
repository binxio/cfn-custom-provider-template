# cfn-custom-provider-template
A template source directory for creating custom CloudFormation Providers.

After cloning this directory you have to following make targets at your command:

```
make                    - builds a zip file to target/.
make test               - execute the tests, requires a working AWS connection.

make deploy             - deploy to the default region eu-central-1.
make deploy-all-regions - deploy to all regions.

make release            - builds a zip file and deploys it to s3.

make deploy-provider    - deploys the provider.
make delete-provider    - deletes the provider.

make demo               - deploys the demo cloudformation stack.
make delete-demo        - deletes the demo cloudformation stack.

make clean              - the workspace.
```

## Pre-requisites
You need to have awscli, python, jq and Docker installed.



## Getting started
this template  contains all the stuff to create, test and deploy a simple Custom Resource provider for the resource [Custom::Custom](docs/Custom.md).

The idea is that the resource just copies the property `Value` to return it as an atttribute of the CFN resource.  To experience a complete development cycle, you need to implement the `create`, `update` and `delete` methods in `src/cfn_custom_provider.py` 
until the following command succeeds:

```sh
make test
```

The source implements a ResourceProvider class defined by Python module [cfn\_resource\_provider](https://pypi.python.org/pypi/cfn-resource-provider).


## Deploying the provider
Set the variable `S3_BUCKET_PREFIX` and `AWS_REGION` in the Makefile to point to your bucket (See [#S3 buckets](#s3buckets) for details).

After that succeeds, deploy the provider by typing:

```sh
make deploy
make deploy-provider
```

## Deploying the demo
After the provider is deployed, you can create the demo stack:

```sh
make demo
```

Now you are ready to create useful Custom CloudFormation Providers!

Checkout [Kong API Gateway](https://github.com/binxio/cfn-kong-provider), [Secrets](https://github.com/binxio/cfn-secret-provider) and [SES](https://github.com/binxio/cfn-ses-provider) for example.

## S3 Buckets
<a id="s3bucket"></a> 
To deploy your lambda to all AWS regions, you need to have s3 buckets in all regions matching the name pattern:

```
   <s3-bucket-prefix>-<aws-region>
```
For the development cycle, you need to have at least a bucket in your default region, for instance `binxio-public-eu-central-1`.

To ease the creation of all buckets, you could use the [create-global-s3-buckets](https://github.com/binxio/create-global-s3-buckets) script.
