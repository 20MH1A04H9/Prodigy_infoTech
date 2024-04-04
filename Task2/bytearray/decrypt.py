#decryption
try:
	
	path = r'D:\Tech\Task2\bytearray\infotech.jpg'
	key = int(input('Enter Key for encryption of Image : '))
	
	print('The path of file : ', path)
	print('Note : what if Decryption key wrong is not Open the image.')
	print('Key for Decryption : ', key)
	
	fin = open(path, 'rb')

	image = fin.read()
	fin.close()
	
	image = bytearray(image)

	for index, values in enumerate(image):
		image[index] = values ^ key


	fin = open(path, 'wb')
	
	fin.write(image)
	fin.close()
	print('Decryption Done...')


except Exception:
	print('Error caught : ', Exception.__name__)