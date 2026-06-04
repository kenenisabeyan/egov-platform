class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before response logic (no-op boilerplate)
        response = self.get_response(request)
        # After response logic (no-op boilerplate)
        return response
