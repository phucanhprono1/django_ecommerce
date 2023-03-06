from django.http import HttpResponse


def catalog(request):
 site_name = "Modern Musician"
 response_html = u"<html><body>Welcome to %s.</body></html>" % site_name
 return HttpResponse(catalog_html)