# -*- coding: utf-8 -*-
import time
import logging
from datetime import datetime
from flask import request

log = logging.getLogger(__name__)


def before_request():
    request.start_time = time.time()
    request.time_ns = time.time_ns()


def log_after_request(response, request_latency):
    duration = request_latency / 1000000
    dt = datetime.fromtimestamp(request.start_time)
    timestamp = dt.isoformat('T')

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)
    request_id = request.headers.get('X-Request-ID') or ''

    log_params = {
        'method': request.method,
        'path': request.path,
        'status': response.status_code,
        'duration': int(duration),
        'time': timestamp,
        'ip': ip,
        'request_host': host,
        'params': args
    }

    if request_id:
        log_params['request_id'] = request_id

    log.info(f'{request.method} {request.path} : {response.status_code} : {duration} ms', extra=log_params)


def after_request(response):
    request_latency = time.time_ns() - request.time_ns
    log_after_request(response, request_latency)

    return response


def monitor(app):
    app.before_request(before_request)
    app.after_request(after_request)
