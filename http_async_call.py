import requests
import asyncio

async def async_http_call_fn(index,file):
	result = requests.get("https://webhook.site")
	file.write("Run {0} : {1}\n".format(index, result.headers["Date"]))

async def main(loop):
	try:
		file = open("output.txt", "a+")
		file.write("---Asynchronous http call output---\n")
		tasks = [async_http_call_fn(index,file) for index in range(1,4)]
		await asyncio.gather(*tasks)
	except IOError: #catch file open/write exceptions
		print("An error occured while performing file operation.")
	else:
		file.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
