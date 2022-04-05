from flask import Blueprint
from .api import *


guest_app = Blueprint("guest_app", __name__)


homeapi_view = HomeAPI.as_view('home_api')

guest_app.add_url_rule('/',
	view_func=homeapi_view, 
	methods=['GET', 'POST'])


resultsapi_view = ResultsAPI.as_view('ResultsAPI_api')

guest_app.add_url_rule('/results',
	view_func=resultsapi_view, 
	methods=['GET'])


bouncingapi_view = BouncingAPI.as_view('BouncingAPI_api')

guest_app.add_url_rule('/bouncing',
	view_func=bouncingapi_view, 
	methods=['GET'])


downloadapi_view = DownloadAPI.as_view('DownloadAPI_api')

guest_app.add_url_rule('/download/<extension>',
	view_func=downloadapi_view, 
	methods=['GET'])

