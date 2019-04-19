#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2019-04-19 15:29

"""Calc Server."""

from concurrent import futures
import time
import logging

import grpc

from src.proto.calc import calc_pb2 as calc_pb_req_res_cls
from src.proto.calc import calc_pb2_grpc as calc_pb_client_server_cls


__author__ = 'Toran Sahu <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the MIT license'


logger = logging.getLogger(__name__)
ONE_DAY = 60 * 60 * 24  # in secs


class BasicCalculator(calc_pb_client_server_cls.CalculatorServicer):
    """Basic Calculator."""

    def Add(self, request, context):  # Case Sensitive
        """Add two numbers."""
        return calc_pb_req_res_cls.AddReply(n1=request.n1 + request.n2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calc_pb_client_server_cls.add_CalculatorServicer_to_server(BasicCalculator(), server)
    server.add_insecure_port("[::]:50050")
    server.start()
    logger.warning("Server started. Listening on port 50050")

    try:
        while True:
            time.sleep(ONE_DAY)
    except KeyboardInterrupt:
        server.stop(0)
        logger.warning("\nServer stopped.")


if __name__ == "__main__":
    serve()
