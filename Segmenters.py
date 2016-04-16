from Image import Image
class Segmenter:

	def getCurrentSegment(self):
		pass

	def getNextSegment(self):
		pass

	def hasNextSegment(self):
		pass

	def resetTrajectory(self):
		pass

class RectangularSegmenter(Segmenter):

	def __init__(self, PILImage, heightRectangle, widthRectangle, trajectory, lstPreprocessing = []):

		self.image = PILImage
		self.height = heightRectangle
		self.width = widthRectangle
		self.trajectory = trajectory
		self.lstPreprocessing = lstPreprocessing

	def resetTrajectory(self):
		self.trajectory.resetPosition()

	def hasNextSegment(self):
		return self.trajectory.hasNextPosition()

	def getCurrentSegment(self):

		centerCorner = self.trajectory.getPosition()
		upperLeftCorner = [centerCorner[0], centerCorner[1]]
		upperLeftCorner[0] = centerCorner[0] - (self.width / 2)
		upperLeftCorner[1] = centerCorner[1] - (self.height / 2)
		lowerRightCorner = [centerCorner[0], centerCorner[1]]
		lowerRightCorner[0] += (self.width / 2)
		lowerRightCorner[1] += (self.height / 2)

		cutout = self.image.crop((upperLeftCorner[0], upperLeftCorner[1], lowerRightCorner[0], lowerRightCorner[1]))

		for processing in self.lstPreprocessing:
			cutout = processing.process(cutout)

		return Image(centerCorner[0], centerCorner[1], cutout)


	def getNextSegment(self):

		if(not self.hasNextSegment()):
			return None

		centerCorner = self.trajectory.getNextPosition()
		upperLeftCorner = [centerCorner[0], centerCorner[1]]
		upperLeftCorner[0] = centerCorner[0] - (self.width/2)
		upperLeftCorner[1] = centerCorner[1] - (self.height/2)
		lowerRightCorner = [centerCorner[0], centerCorner[1]]
		lowerRightCorner[0] += (self.width/2)
		lowerRightCorner[1] += (self.height/2)

		cutout = self.image.crop((upperLeftCorner[0], upperLeftCorner[1], lowerRightCorner[0], lowerRightCorner[1]))

		for processing in self.lstPreprocessing:
			cutout = processing.process(cutout)

		return Image(centerCorner[0], centerCorner[1], cutout)






