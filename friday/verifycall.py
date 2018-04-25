import cognitive_face as CF

def test_verify(a,b):
    
    KEY = '512e8a398d2a4847bfe1fc6e7e55e35d'  # Replace with a valid Subscription Key here.
    CF.Key.set(KEY)

    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)
    res = CF.face.verify(face_id=a,another_face_id=b)
    return (res['isIdentical'])
    

if __name__ == '__main__':
	test_verify("28551663-ee54-4437-bb97-1dc0af2ec591","c2a2609d-8a91-4e3a-9078-15c8e0a4d771")