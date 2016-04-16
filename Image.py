#######################################################################################################################

class Image:

#-------------------------------------------------------------------------------------------------------------
	def __init__(self, xPositionClipper, yPositionClipper, PILImage):
		self.xPositionClipper = xPositionClipper
		self.yPositionClipper = yPositionClipper
		self.PILImage = PILImage

#-------------------------------------------------------------------------------------------------------------
	def __init__(self, xPositionClipper, yPositionClipper, originalSizeWidth, originalSizeHeight, PILImage):
		self.xPositionClipper = xPositionClipper
		self.yPositionClipper = yPositionClipper
		self.originalSizeWidth = originalSizeWidth
		self.originalSizeHeight = originalSizeHeight
		self.PILImage = PILImage

#######################################################################################################################