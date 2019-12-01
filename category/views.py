from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from category.models import Category, Language, Domain

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return HttpResponse('Category Homepage!')


def get_domains(request):
	domains = Domain.objects.all()
	domains_list = list(domains)  # important: convert the QuerySet to a list object
	data = list()
	for domain in domains_list:
		main_category = {
			'tag': domain.main_category.tag,
			'name': domain.main_category.name,
		}
		data.append({
			'domain': domain.domain,
			'name': domain.name,
			'is_porn': domain.is_porn,
			'is_malware': domain.is_malware,
			'is_mobile': domain.is_mobile,
			'is_phishing': domain.is_phishing,
			'is_foreign': domain.is_foreign,
			'language': domain.language.name,
			'main_category': main_category,
		})

	return JsonResponse(data, safe=False)
    
