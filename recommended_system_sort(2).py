import requests
import json
import operator
from collections import OrderedDict
import csv
from urllib.parse import urlencode
from urllib.request import Request,urlopen
import sys

class recommendation:
	def __init__(self,upc):
		self.upc=str(upc)
		self.brand_json={}
		self.category_json={}
		self.brand=""
		self.category=""
		self.price={}
		self.sort_result=""



	def test_brand(self):
		if type(self.brand_json)!=str:
			return None
		try:
			json.loads(self.brand_json)
		except ValueError:
			return False
		return True

	def test_category(self):
		if type(self.category_json)!=str:
			return None

		try:
			json.loads(self.category_json)
		except ValueError:
			return False
		return True

	def capture_brand(self):
		url="https://api.barcodespider.com/v1/lookup?token=eba3ac19cc270a0e8b42&upc="+self.upc
		response=requests.get(url)
		response_text=json.loads(response.text)
		value_attributes=response_text.get('item_attributes')

		self.brand=value_attributes.get('brand')
		return self.brand

	def capture_category(self):
		url="https://api.barcodespider.com/v1/lookup?token=eba3ac19cc270a0e8b42&upc="+self.upc
		response=requests.get(url)
		response_text=json.loads(response.text)
		value_attributes=response_text.get('item_attributes')
		self.category=value_attributes.get('category')
		return self.category

	def __checkresponse(self,checkobject):
		
		response=checkobject.get('item_response')
		code=response.get('code')
		if code=='200':
			print('MMM')
			return True
		else:
			print(code)
			return False

	def recommendation_brand(self):
		
		url_brand='https://api.barcodespider.com/v1/search?token=eba3ac19cc270a0e8b42&s='+str(self.brand)
		response_brand=requests.get(url_brand)
		self.brand_json=json.loads(response_brand.text)
		
		"""self.brand_json=str(self.brand_json)"""
		return self.brand_json

	
	def recommendation_category(self):
		url_catageory='https://api.barcodespider.com/v1/search?token=eba3ac19cc270a0e8b42&s='+str(self.category)
		response_catageory=requests.get(url_catageory)
		self.category_json=json.loads(response_catageory.text)
		
		"""self.category_json=str(self.category_json)"""
		return self.category_json

	def getbrand(self):
		return self.brand_json

	
	def getcategory(self):
		return self.category_json

	
	def choose_category(self):
		self.capture_category()
		self.recommendation_category()
		
		self.to_csv(self.getcategory())
	

	def choose_brand(self):
		self.capture_brand()
		self.recommendation_brand()
		

		self.to_csv(self.getbrand())


	def to_csv(self,data):
		email = '1789173384@qq.com'
		json = str(data)
		filename = 'json_csv'
		sys.stdout.write('Status: 200 OK\n')
		sys.stdout.write('Content-Type: text/csv; charset=utf-8\n')
		sys.stdout.write('Content-Disposition: attachment; filename=' + filename + '\n\n')
		url = 'https://json-csv.com/api/getcsv'
		post_fields = {'email': email, 'json': json}
		request = Request(url, urlencode(post_fields).encode())
		csv = urlopen(request).read().decode()
		for l in csv.split('\r\n'):
			print (l)


















		"""outputdata=open('output.cvs','w')
		csvwriter=csv.writer(outputdata)
		count=0
		for i in data:
			if count==0:
				header=data.keys()
				csvwriter.writerow(header)
				count+=1
			csvwriter.writerow(i.values)
		outputdata.close()"""
		
		




	










	





    





	
	

  
	



 


