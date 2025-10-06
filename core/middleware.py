class DomainRouterMiddleware:
    """
    هدایت مسیر بر اساس دامنه در runtime.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.META.get("HTTP_HOST", "")

        if host in ["mjes.ir", "www.mjes.ir"]:
            request.urlconf = "website.urls"
        elif host in ["kodom-masjed.com", "www.kodom-masjed.com"]:
            request.urlconf = "rezervation.urls"
        else:
            return HttpResponseNotFound("404 - دامنه نامعتبر")

        response = self.get_response(request)
        return response
