import datetime
from pyramid.response import Response
from pyramid.response import FileResponse
from paste.httpserver import serve
import json
import csv
from bson.json_util import dumps
def my_view(request):
    request.db.authenticate('bartolovic','bartolovic')
    return {'project':'cta_project'}
def csvview(request):
	response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
	return response
def wea_ws(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_hum(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gust(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_see(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dust(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_temp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_cal(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzd(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttemp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1temp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2temp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1hum(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2hum(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartopleft(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttopright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerr(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1t(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globr(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtw(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_ac(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astrob(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_crate(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_rack(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhum(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devaz(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzd(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcx(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_stars(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_bright(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_temp(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloud(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skyt(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3km(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6km(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9km(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12km(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psf(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfn(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_size(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_b(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_l(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daq(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_cal(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_cal(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sig(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_ped(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_ped(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_int(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_wsy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_humy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gusty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_seey(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dusty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_tempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_caly(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzdy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1tempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2tempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1humy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2humy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottlefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartoplefty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottrighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttoprighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerry(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1ty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2ty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globry(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtwy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_acy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astroby(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_cratey(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_racky(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2y(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhumy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devazy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzdy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcxy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcyy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_starsy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_brighty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_tempy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloudy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skyty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3kmy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6kmy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9kmy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12kmy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfny(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_sizey(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_by(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_ly(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daqy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_caly(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_caly(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sigy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_pedy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_pedy(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_inty(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_wsM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_humM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gustM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_seeM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dustM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_tempM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_calM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_intM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sigM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzdM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttempM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1tempM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2tempM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1humM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2humM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptopleftM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottrightM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptopleftM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottrightM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastopleftM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottrightM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftopleftM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottrightM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottleftM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartopleftM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottrightM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttoprightM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerrM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1tM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2tM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globrM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3M2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtwM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1M2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2M2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_acM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astrobM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_crateM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_rackM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1M2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2M2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhumM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devazM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzdM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcxM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_starsM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_brightM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_tempM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloudM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skytM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3kmM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6kmM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9kmM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12kmM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfnM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_sizeM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_bM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_lM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daqM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sigM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sigM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_calM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_intM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sigM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_calM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_intM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sigM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_pedM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_intM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_intM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_pedM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_intM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_intM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_wsyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_humyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gustyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_seeyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dustyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_tempyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_calyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_intyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sigyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzdyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttempyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1tempyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2tempyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1humyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2humyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptopleftyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottrightyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptopleftyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottrightyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastopleftyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottrightyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftopleftyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottrightyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottleftyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartopleftyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottrightyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttoprightyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerryM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1tyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2tyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globryM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3yM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtwyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1yM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2yM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_acyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astrobyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_crateyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_rackyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1yM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2yM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhumyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devazyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzdyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcxyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcyyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_starsyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_brightyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_tempyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloudyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skytyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3kmyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6kmyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9kmyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12kmyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfnyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_sizeyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_byM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_lyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daqyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sigyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sigyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_calyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_intyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sigyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_calyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_intyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sigyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_pedyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_intyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_intyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_pedyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_intyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_intyM2(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "min":0, "max":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_wsmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_hummm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gustmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_seemm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dustmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_tempmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_calmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_intmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sigmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzdmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttempmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1tempmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2tempmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1hummm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2hummm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptopleftmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottrightmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptopleftmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottrightmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastopleftmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottrightmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftopleftmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottrightmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottleftmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartopleftmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottrightmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttoprightmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerrmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1tmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2tmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globrmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3mm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtwmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1mm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2mm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_acmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astrobmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_cratemm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_rackmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1mm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2mm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhummm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devazmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzdmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcxmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_starsmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_brightmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_tempmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloudmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skytmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3kmmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6kmmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9kmmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12kmmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfnmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_sizemm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_bmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_lmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daqmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sigmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sigmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_calmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_intmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sigmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_calmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_intmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sigmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_pedmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_intmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_intmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_pedmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_intmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_intmm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_wsymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_humymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gustymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_seeymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dustymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_tempymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_calymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_intymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sigymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzdymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttempymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1tempymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2tempymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1humymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2humymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptopleftymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottrightymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptopleftymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottrightymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastopleftymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottrightymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftopleftymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottrightymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottleftymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartopleftymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottrightymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttoprightymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerrymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1tymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2tymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globrymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3ymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtwymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1ymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2ymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_acymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astrobymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_crateymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_rackymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1ymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2ymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhumymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devazymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzdymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcxymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcyymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_starsymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_brightymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_tempymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloudymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skytymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3kmymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6kmymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9kmymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12kmymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfnymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_sizeymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_bymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_lymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daqymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sigymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sigymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_calymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_intymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sigymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_calymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_intymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sigymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_pedymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_intymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_intymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_pedymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_intymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_intymm(request):
    cursor = request.db.magic.find({ "telescope":"M1", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_wsM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_humM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gustM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_seeM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dustM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_tempM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_calM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_intM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sigM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzdM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttempM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1tempM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2tempM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1humM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2humM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptopleftM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottrightM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptopleftM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottrightM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastopleftM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottrightM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftopleftM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottrightM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottleftM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartopleftM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottrightM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttoprightM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerrM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1tM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2tM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globrM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3M2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtwM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1M2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2M2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_acM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astrobM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_crateM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_rackM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1M2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2M2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhumM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devazM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzdM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcxM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_starsM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_brightM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_tempM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloudM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skytM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3kmM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6kmM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9kmM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12kmM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfnM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_sizeM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_bM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_lM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daqM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sigM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sigM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_calM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_intM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sigM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_calM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_intM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sigM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_pedM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_intM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_intM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_pedM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_intM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_intM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/temperatures2.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_wsyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_ws"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_humyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_gustyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_gust"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_seeyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_see"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_dustyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_dust"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def rec_tempyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"rec_temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camtd_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camtd_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camipr_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camipr_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camiprerr_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camiprerr_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_calyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_intyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calq_sigyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calq_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvzdyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"drvzd"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def drvdev_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"drvdev_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camhv_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camhv_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdc_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camdc_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campd_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"campd_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def campixtemp_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"campixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def meanpixtemp_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"meanpixtemp_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camclusttempyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camclusttemp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camvcelbias_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camvcelbias_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1tempyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv1temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2tempyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv2temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv1humyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv1hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camlv2humyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camlv2hum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcptopleftyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfcptopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfcpbottrightyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfcpbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcptopleftyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrcptopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrcpbottrightyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrcpbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiastopleftyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiastopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasbottrightyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasftopleftyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasftopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolchasiasfbottrightyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolchasiasfbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolrearbottleftyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolrearbottleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolreartopleftyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolreartopleft"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfrontbottrightyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfrontbottright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camcoolfronttoprightyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camcoolfronttopright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def amcerryM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"amcerr"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l1tyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l1t"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2tyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l2t"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def l2t_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"l2t_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_globryM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_globr"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_l3yM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_l3"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_dtwyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_dtw"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt1yM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_cbt1"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_cbt2yM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_cbt2"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_acyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_ac"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sumt_astrobyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sumt_astrob"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_crateyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cool_crate"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cool_rackyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cool_rack"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp1yM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbtemp1"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbtemp2yM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbtemp2"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def calbhumyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"calbhum"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devazyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_devaz"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_devzdyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_devzd"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcxyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_camcx"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_camcyyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_camcy"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_starsyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_stars"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sg_brightyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sg_bright"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def wea_tempyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"wea_temp"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_cloudyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pyro_cloud"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pyro_skytyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pyro_skyt"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans3kmyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans3km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans6kmyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans6km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans9kmyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans9km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def las_trans12kmyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"las_trans12km"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_psf"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_psfnyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_psfn"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def muon_sizeyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"muon_size"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_byM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sbigpsf_b"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def sbigpsf_lyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"sbigpsf_l"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def camdt_daqyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"camdt_daq"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def bias_sigyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"bias_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def hitfrac_sigyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"hitfrac_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_calyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_intyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtm_sigyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtm_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_calyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_cal"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_intyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def arrtmrms_sigyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"arrtmrms_sig"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_pedyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"ped_ped"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def ped_intyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"ped_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def npe_intyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"npe_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_pedyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pedrms_ped"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def pedrms_intyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"pedrms_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response
def cfact_intyM2mm(request):
    cursor = request.db.magic.find({ "telescope":"M2", "name":"cfact_int"}, {"_id":0, "name":0, "telescope":0, "mean":0, "median":0, "rms":0})
    count = 0
    data = open('/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv', 'w')
    csvwriter = csv.writer(data)
    for document in cursor:
		if count == 0:
			header = document.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(document.values())
    data.close()
    response = FileResponse(
		'/var/www/html/jmatic/CTA_project/cta_project/cta_project/CSV files/csvfile.csv',
		request=request,
		content_type='csv'
		)
    return response

