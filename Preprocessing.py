class Preprocessing:

	def process(self, PILImage):
		pass

class SizePreprocessing(Preprocessing):

	def __init__(self, widthResizeImgOut, heightResizeImgOut):
		self.widthResizeImgOut = widthResizeImgOut
		self.heightResizeImgOut = heightResizeImgOut

	def process(self, PILImage):
		return PILImage.resize((self.withResizeImgOut, self.highResizeImgOut))