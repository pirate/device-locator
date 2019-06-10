from flask import Flask, render_template
from pyicloud import PyiCloudService

api = PyiCloudService('someiclouduser@example.com')
app =  Flask(__name__)


@app.route('/')
def get_iphone():
	devices = api.devices
	iphone = devices['EXAMPLE_DEVICE_ID'] 
	location = iphone.location()

	return render_template(
		'devices.html',
		name=iphone.data['name'],
		latitude=location['latitude'],
		longitude=location['longitude'],
	)


if __name__ == '__main__':
	app.run(debug=True)
