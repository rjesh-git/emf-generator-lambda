from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as _alambda
    # aws_sqs as sqs,
)

from constructs import Construct

class EmfGeneratorLambdaPyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Defines an AWS Lambda resource
        emf_lambda = _alambda.PythonFunction(
            self,
            'EMF-Generator',
            entry="./lambda/",
            runtime=_lambda.Runtime.PYTHON_3_9,
            index="generator.py",
            handler='handler',
        )
