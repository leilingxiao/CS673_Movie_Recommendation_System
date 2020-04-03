import requests
import json
import operator
from collections import OrderedDict
class recommendation:
	def __init__(self,upc):
		self.upc=str(upc)
		self.brand_json=""
		self.category_json=""
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

	def __capture_brand(self):
		url="https://api.barcodespider.com/v1/lookup?token=eba3ac19cc270a0e8b42&upc="+self.upc
		response=requests.get(url)
		response_text=json.loads(response.text)
		value_attributes=response_text.get('item_attributes')
		self.brand=value_attributes.get('brand')
		return self.brand

	def __capture_category(self):
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

	def sort(self,data):
		print(data.keys())
		data=sorted(data,key=lambda item:item['Stores'].get('price',0))
		return data

	def recommendation_brand(self):
		
		url_brand='https://api.barcodespider.com/v1/search?token=eba3ac19cc270a0e8b42&s='+str(self.brand)
		response_brand=requests.get(url_brand)
		self.brand_json=json.loads(response_brand.text)
		"""self.brand_json=self.sort(self.brand_json)"""
		self.brand_json=str(self.brand_json)
		return self.brand_json

	
	def recommendation_category(self):
		url_catageory='https://api.barcodespider.com/v1/search?token=eba3ac19cc270a0e8b42&s='+str(self.category)
		response_catageory=requests.get(url_catageory)
		self.category_json=json.loads(response_catageory.text)
		"""self.category_json=self.sort(self.category_json)"""
		self.category_json=str(self.category_json)
		return self.category_json

	def getbrand(self):
		return self.brand_json

	
	def getcategory(self):
		return self.category_json

	
	def choose_category(self):
		self.__capture_category()
		self.recommendation_category()
		self.test_category()
		return self.getcategory()
	

	def choose_brand(self):
		self.__capture_brand()
		self.recommendation_brand()
		self.test_brand()

		return self.getbrand()



	










	





    





	
	

  
	



 


