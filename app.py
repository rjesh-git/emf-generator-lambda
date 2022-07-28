#!/usr/bin/env python3
import os

import aws_cdk as cdk

from emf_generator_lambda_py.emf_generator_lambda_py_stack import EmfGeneratorLambdaPyStack


app = cdk.App()
EmfGeneratorLambdaPyStack(app, "EmfGeneratorLambdaPyStack")

app.synth()
