#!/usr/bin/env python3
from prometheus_client import start_http_server
from prometheus_client.core import  CounterMetricFamily, REGISTRY
import random
import time


class CustomCollector(object):     ## Class for CustomCollector which helps us to use different metric types
    def __init__(self):
        pass
    def collect(self):
            
        f_read = open("test.txt", 'r')
        last_line = f_read.readlines()[-1]

        progress = (' '.join(last_line.split(' ')[:-10]))
        value = CounterMetricFamily("STATUS", 'dd progress in bytes', labels='value')
        value.add_metric(["bytes"], progress)
        yield value



if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    # Generate some requests.
    while True:
        time.sleep(30)
