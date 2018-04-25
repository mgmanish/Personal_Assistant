import cognitive_face as CF

def fun(url):
	KEY = '512e8a398d2a4847bfe1fc6e7e55e35d'  # Replace with a valid Subscription Key here.
	CF.Key.set(KEY)

	BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
	CF.BaseUrl.set(BASE_URL)

	img_url = url
	result = CF.face.detect(img_url)
	x = (result[0]['faceId'])
	return x
if __name__ == '__main__':
	fun("https://rawgit.com/vikas12396/axis123/master/me.jpg")