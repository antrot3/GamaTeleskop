import datetime
from pyramid.response import Response
from pyramid.response import FileResponse
from paste.httpserver import serve
import json
import csv
from bson.json_util import dumps
def my_view(request):
    request.db.authenticate('cta_project','fesbstudent11')
    dumps = request.db.mycollection.find_one()
    json_pars = dumps['temperature_details']
    temperature_data = open('C:/Users/Ante/Desktop/teleskop/GamaTeleskop/Website/cta_project/cta_project/CSV files/temperatures.csv', 'w')
    csvwriter = csv.writer(temperature_data)
    count = 0
    for temp in json_pars:
		if count == 0:
			header = temp.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(temp.values())
    temperature_data.close()
    return {'project':'cta_project'}
def csvview(request):
	response = FileResponse(
		'C:/Users/Ante/Desktop/teleskop/GamaTeleskop/Website/cta_project/cta_project/CSV files/temperatures.csv',
		request=request,
		content_type='csv'
		)
	return response



