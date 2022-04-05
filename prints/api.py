from flask.views import MethodView
from flask import request, abort, jsonify, render_template, session,send_from_directory
from mainModules.arrive import simulate_queue


# import pdfkit, os



class HomeAPI(MethodView):

	def get(self):
		return render_template("index.html")

	def post(self):
		arr1, arr2, ser1, ser2 = int(request.form["arr1"]),int(request.form["arr2"]),int(request.form["ser1"]),int(request.form["ser2"])
		average_idle_time, average_service_time = simulate_queue(arr1,arr2,ser1,ser2)[0],simulate_queue(arr1,arr2,ser1,ser2)[0]

		return render_template("results.html", average_idle_time=average_idle_time, average_service_time=average_service_time)



class ResultsAPI(MethodView):

	def get(self):
		return render_template("results.html")



class BouncingAPI(MethodView):

	def get(self):
		
		return render_template("bouncing.html")

class DownloadAPI(MethodView):

	def get(self,extension):
		# return "success"
		names = "waitlist."+extension
		return send_from_directory(directory="mainModules",path=names)
