import urllib
import urllib.request
import urllib.parse
import json
url="http://rest.wufazhuce.com/OneForWeb/one/getHp_N"
month =['01','02','03','04','05','06','07','08','09','10','11','12']
day=['01','02','03','04','05','06','07','08','09','10','11','12','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']

for x in month:
	for y in day:
		z='2015'+'-'+x+'-'+y
		para={
		'strDate':z,
		'strRow':'1'
		}
		url_values=urllib.parse.urlencode(para)
		url_values=url_values.encode(encoding='UTF8')  
		full_url=urllib.request.Request(url,url_values) 
		response=urllib.request.urlopen(full_url).read()
		hjson=json.loads(response.decode('utf-8'))
		print(z)
		print(hjson['hpEntity']['strContent'])

		
