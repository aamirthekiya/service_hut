from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe

from .models import Document

# Create your views here.
def index(request):
	documents = Document.objects
	context = {
		'documents': documents
	}
	return render(request, 'home.html', context)

@login_required(login_url="login")
def create(request):
	if request.method == 'POST':
		if request.POST['name'] and request.POST['keyword'] and request.FILES['file']:
			limit = 2 * 1024 * 1024
			siz = request.FILES['file'].size
			if siz > limit:
				context = {
					'error': 'File size exceeds the limit... max size => 2 MB',
				}
				return render(request, 'create.html', context)
			else:
				document = Document()
				document.name = request.POST['name']
				document.keyword = request.POST['keyword']
				document.file = request.FILES['file']
				document.creater = request.user
				siz = request.FILES['file'].size
				document.save()
				return redirect('create')
		else:
			context = {
				'error': 'All fields are required',
			}
			return render(request, 'create.html', context)
	return render(request, 'create.html')

@login_required(login_url="login")
def search(request):
	query_object = Document.objects.all()
	query = request.GET.get('query')
	ser = request.GET.get('qu')
	print(ser)
	# print(Document.file.url.split(".")[-1])
	# if request.method == "GET":
	#
	# 	text = query.replace(query, '<strong>'+query+'</strong>')
	#
	# 	# now you have to mark it as safe so the tags will be rendered as tags
	# 	text = mark_safe(text)
	# else:
	# 	text = None
	# a = query_object.file.name
	# print(a)
	# ext = query_object.file.url.split(".")[-1]
	if query != '' and query is not None:
		query_object = query_object.filter(keyword__icontains=query)
	return render(request, 'search.html', {'query_object':query_object,'query':query})
