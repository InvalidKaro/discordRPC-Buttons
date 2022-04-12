import os

try:
	from pypresence import Presence
except ImportError:
	if input("Install dependencies? [y/n]\n").lower() == 'y':
		try:
			os.system("pip install pypresence")
		except:
			print("Something Went Wrong!")

import time
import json
import functions
import exceptions

void = 0

s = functions.settings()

if s["start_time"] == 0:
	start_time = time.time()

elif s["start_time"] < 0:
	start_time = functions.timestamp((s["start_time"]*-1))

else:
	start_time = s["start_time"]

class Main():
	def __init__(self , cid):
		self.presence = Presence(cid)
		self.client_id = cid
		self.presence.connect()

		os.system("@echo off")
		os.system("title Custom Presence v2.0")
		os.system("cls")

	def main(self):
		while True:
			try:
				time.sleep(10)
			except KeyboardInterrupt:
				raise exceptions.Exit("Application Closed by the user")

	def update(self , settings: dict):
		if settings["button"] == False:
			self.presence.update(large_image=settings["large-image"] , large_text=settings["large-image-text"] , details=settings["details"], state=settings["state"] , start=start_time)
		
		elif settings["button"] == True:
			try:
				self.presence.update(buttons = settings["buttons"] , large_image=settings["large-image"] , large_text=settings["large-image-text"] , details=settings["details"], state=settings["state"] , start=start_time)
			except:
				print("Invalid Settings.json , [there must be at least 1 button and maximum 2 buttons]")

		print("Successfully Loaded Settings!")

app = Main(functions.get_id())

try:
	app.update(s)
	app.main()
except exceptions.Exit:
	print("Application Closed")
