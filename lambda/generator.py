import json
import time
import random
from aws_embedded_metrics import metric_scope

@metric_scope
def handler(event, context, metrics):
    metrics.set_namespace("Custom_Application")
    metrics.put_dimensions({"Device": "Pressure_Sensor"})
    metrics.put_metric("ProcessingLatency", random.randint(1,100), "Milliseconds")
    metrics.put_metric("Temperature", random.randint(1,100), "Count")
    metrics.set_property("SubscritionId", "123456789012")
    metrics.set_property("RequestId", "422b1569-16f6-4a03-b8f0-fe3fd9b100f8")
    metrics.set_property("DeviceId", "61270781-c6ac-46f1-baf7-22c808af8162")
    metrics.set_property(
        "Payload", {"sampleTime": int(time.time()), "temperature": random.randint(1,100), "pressure": random.randint(1,105)}
    )

    return {"message": "Hello!"}