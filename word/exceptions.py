class OxfordExceptions(Exception):
    def __init__(self, status, msg):
        self.status = status
        self.msg = msg


class UnauthorizedError(OxfordExceptions):
    # 401
    pass


class AuthenticationError(OxfordExceptions):
    # 403
    pass


class InternalServerError(OxfordExceptions):
    # 500
    pass


class BadGatewayError(OxfordExceptions):
    # 502
    pass


class ServiceUnavailableError(OxfordExceptions):
    # 503
    pass
