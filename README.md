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
the template contains all the stuff to create, test and deploy a simple provider.

The custom resource in the template [Custom::Custom](docs/Custom.md) copies the property `Value` as atttribute of the resource. 

to experience a complete development cycle, you need to implement the `create`, `update` and `delete` methods in `src/cfn_custom_provider.py` 
until the following command succeeds:

```sh
make test
```

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

Checkout https://github.com/binxio/cfn-kong-provider, https://github.com/binxio/cfn-secret-provider and https://github.com/binxio/cfn-ses-provider
for example.

## S3 Buckets
<a id="s3bucket"></a> 
To deploy, you need to have one or more s3 buckets matching the name pattern:

```
   <s3-bucket-prefix>-<aws-region>
```

If you want to allow easy deployment in all regions, make sure that the buckets
are created in every region. You could use the [create-global-s3-buckets](https://github.com/binxio/create-global-s3-buckets) script.
