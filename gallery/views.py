from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from .models import Image
from .models import Contact

def index(request):
	image_list 	= Image.objects.order_by('-name')
	template 	= loader.get_template('index.html')
	context 	= RequestContext(
		request,{
			'image_list': image_list,
		})
	return HttpResponse(template.render(context))

def get_all_images(request):
	return HttpResponse("Response all images")

def get_all_images_by_user(request):
	return HttpResponse("Respons to images by user")

def upload_image_by_url(request):
	if request.POST:
		image 				= Image()
		image.name 	= request.POST['image_name']
		image.url		= request.POST['image_url']
		image.desc		= request.POST['image_desc']
		image.save()
		return HttpResponseRedirect(reverse('index'))	
	else:
		return render(request, 'create.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	template 	= loader.get_template('contact.html')
	if request.POST:
		try:
			#try to save contact
			contact			= Contact()
			contact.name 	= request.POST['name']
			contact.email	= request.POST['email']
			contact.phone	= request.POST['phone']
			contact.comment	= request.POST['comment']
			contact.save()
			#prepare response
			context 		= RequestContext(
				request,{
					'messsage_sent':"OK" ,
			})

			return HttpResponse(template.render(context))
		except:
			return HttpResponse(template.render(context))
	else:
		return render(request, 'contact.html') 

