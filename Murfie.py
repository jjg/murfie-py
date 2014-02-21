import httplib
import urllib
import json

class API:
	
	API_ENDPOINT = 'api.murfie.com'
	API_CONNECTION = httplib.HTTPSConnection(API_ENDPOINT)
	token = None
	
	def __init__(self, email, password):
		
		# fetch the user's token
		api_url = '/api/tokens'
		params = urllib.urlencode({'email':email, 'password':password})
		headers = {'Content-type':'application/x-www-form-urlencoded','Accept':'text/plain'}
		
		self.API_CONNECTION.request('POST', api_url, params, headers)
		response = self.API_CONNECTION.getresponse()
		raw_response = response.read()
		self.API_CONNECTION.close()
		
		api_result = json.loads(raw_response)
		
		self.token = api_result['user']['token']
	
		
	# get collection
	def Collection(self):
		api_url = '/api/discs.json?auth_token=' + self.token
		headers = {'Content-type':'application/x-www-form-urlencoded','Accept':'text/plain'}
		self.API_CONNECTION.request(method='GET', url=api_url, headers=headers)
		response = self.API_CONNECTION.getresponse()
		raw_response = response.read()
		self.API_CONNECTION.close()
		
		api_result = json.loads(raw_response)
		
		return api_result
		
		
	# get disc
	def Disc(self, disc):
		api_url = '/api/discs/%s.json?auth_token=%s' % (disc, self.token)
		headers = {'Content-type':'application/x-www-form-urlencoded','Accept':'text/plain'}
		self.API_CONNECTION.request(method='GET', url=api_url, headers=headers)
		response = self.API_CONNECTION.getresponse()
		raw_response = response.read()
		self.API_CONNECTION.close()
		
		api_result = json.loads(raw_response)
		
		return api_result['disc']
		
	
	# get track
	def Track(self, disc, track):
		api_url = '/api/discs/%s/tracks/%s.json?auth_token=%s' % (disc, track, self.token)
		headers = {'Content-type':'application/x-www-form-urlencoded','Accept':'text/plain'}
		self.API_CONNECTION.request(method='GET', url=api_url, headers=headers)
		response = self.API_CONNECTION.getresponse()
		raw_response = response.read()
		self.API_CONNECTION.close()
		
		api_result = json.loads(raw_response)
		
		return api_result['track']
	