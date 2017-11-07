# Custom::Custom
The `Custom::Custom` provider.

## Syntax
To declare this entity in your AWS CloudFormation template, use the following syntax:

```json
{
  "Type" : "Custom::Custom",
  "Properties" : {
    "Value": String
    }
  }
}
```

## Properties
You can specify the following properties:

    "Value" - copied to the attribute.


## Return values
With 'Fn::GetAtt' the following values are available:

- `value` - passed in through the property `Value`.

For more information about using Fn::GetAtt, see [Fn::GetAtt](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).
