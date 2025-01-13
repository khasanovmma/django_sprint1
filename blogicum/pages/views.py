from django.shortcuts import render


def about(request):
    template = "pages/about.html"
    return render(request=request, template_name=template)

def rules(request):
    template = "pages/rules.html"
    return render(request=request, template_name=template)
