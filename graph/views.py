from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
import json
def mainPage(request):
	if request.method=='GET':	
		t = get_template('graph.html')
		html = t.render(Context({}))
		return HttpResponse(html)
	else:	
		data_string=request.POST.get('data')	
		adj_list=json.loads(data_string)
		colors=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
		color_list=[-1]*len(adj_list)
		for vertex in range(len(adj_list)):
			adj_vertices=adj_list[vertex]
			adj_colors=[]	
			for  adj in adj_vertices:
				adj_colors.append(color_list[adj])
			color_list[vertex]=list(set(colors)-set(adj_colors))[0]
			
				
		color_string = json.dumps(color_list)
		return HttpResponse(color_string)

