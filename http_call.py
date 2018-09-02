import requests

def http_call_fn():
	try:
		file = open("output.txt","a+")
		file.write("---Synchronous http call output---\n")
		for index in range(1,4):
			response = requests.get("https://webhook.site")
			file.write("Run {0} : {1} \n".format(index, response.headers["Date"]))
	except IOError: #catch file open/write exceptions.
                print("An error occured while performing file operation.")
	else:
		file.close()

http_call_fn()

