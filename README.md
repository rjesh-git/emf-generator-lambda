# EMF Generator Lambda

Uses ```aws_lambda_python_alpha``` module for refering to external module in Lambda. The Lambda uses ```aws_embedded_metrics``` external module without creating Layer.

> It's an experimental feature only to be used in PoC and not for production use, refer to https://docs.aws.amazon.com/cdk/api/v2/docs/aws-lambda-python-alpha-readme.html for public release of this module.


**Make sure to run docker daemon, which required for this module to package the layer.**
