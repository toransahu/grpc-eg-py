#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2019-04-19 15:48

"""Calc Client."""

import grpc

from src.proto.calc import calc_pb2 as calc_pb_req_res_cls
from src.proto.calc import calc_pb2_grpc as calc_pb_client_server_cls


__author__ = 'Toran Sahu <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the MIT license'


def run():
    channel = grpc.insecure_channel("localhost:50050")
    stub = calc_pb_client_server_cls.CalculatorStub(channel)
    response = stub.Add(calc_pb_req_res_cls.AddRequest(n1=10, n2=15))
    print(response.n1)


if __name__ == "__main__":
    run()
