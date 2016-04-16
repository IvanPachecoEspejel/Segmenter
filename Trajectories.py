#######################################################################################################################
class Trajectory:
	def getNextPosition(self):
		pass

	def getPosition(self):
		pass

	def hasNextPosition(self):
		pass

	def resetPosition(self):
		pass


#######################################################################################################################

class SimpleTrajectory(Trajectory):
	def __init__(self, horizontalStride, verticalStride, topOffset, leftOffset, rigthOffset, bottomOffset, widthImage,
				 heightImage):

		self.topOffset = float(topOffset)
		self.leftOffset = float(leftOffset)
		self.rightOffset = float(rigthOffset)
		self.bottomOffset = float(bottomOffset)
		self.horizontalStride = float(horizontalStride)
		self.verticalStride = float(verticalStride)
		self.widthImg = float(widthImage)
		self.heightImg = float(heightImage)

		self.moveNextPosition = True

		self.coordinate = [self.leftOffset, self.topOffset]

		self.resetPosition()

# ---------------------------------------------------------------------------
	def getPosition(self):
		return [int(i)for i in self.coordinate]

# ---------------------------------------------------------------------------
	def getNextPosition(self):
		if not self.moveNextPosition:
			return self.coordinate

		if self._getIncreaseX() >= (self.widthImg - self.rightOffset):
			self._resetXPosition()

			if self._getIncreaseY() >= (self.heightImg - self.bottomOffset):
				self.moveNextPosition = False
			else:
				self._increaseY()
		else:
			self._increaseX()

		return [int(i)for i in self.coordinate]

# ---------------------------------------------------------------------------
	def hasNextPosition(self):
		return self.moveNextPosition

# ---------------------------------------------------------------------------
	def resetPosition(self):
		self._resetXPosition()
		self._resetYPosition()

# ---------------------------------------------------------------------------
	def _resetXPosition(self):
		self.coordinate[0] = self.leftOffset

# ---------------------------------------------------------------------------
	def _resetYPosition(self):
		self.coordinate[1] = self.topOffset

# ---------------------------------------------------------------------------
	def _getIncreaseX(self):
		return self.coordinate[0] + self.horizontalStride

# ---------------------------------------------------------------------------
	def _getIncreaseY(self):
		return self.coordinate[1] + self.verticalStride

		# ---------------------------------------------------------------------------
	def _increaseX(self):
		self.coordinate[0] = self._getIncreaseX()

# ---------------------------------------------------------------------------
	def _increaseY(self):
		self.coordinate[1] = self._getIncreaseY()


#######################################################################################################################
from math import sin, cos, pi, acos

class CircularTrajectory(Trajectory):
	def __init__(self, horizontalStride, verticalStride, radiusMax, radiusMin, centerX, centerY,
				 widthImage, heightImage):

		if radiusMax <= radiusMin:
			raise Exception(
				'Error el parametro radiusMax: ' + str(radiusMax) + ' debe de ser mayor a radiusMin: ' + str(radiusMin))

		if not (0 < centerX < widthImage):
			raise Exception(
				'Error centerX: ' + str(centerX) + ' debe de estar entre los valores: (0-' + str(widthImage) + ')')

		if not (0 < centerY < heightImage):
			raise Exception(
				'Error centerY: ' + str(centerY) + ' debe de estar entre los valores: (0-' + str(heightImage) + ')')

		if horizontalStride >= 2:
			raise Exception('Error horizontalStride debe de ser menor a 2')

		if verticalStride >= radiusMax - radiusMin:
			raise Exception('Error verticalStride debe de ser menor a la resta de radiusMax-radiusMin: ' + str(
				radiusMax - radiusMin))

		self.radiusMax = float(radiusMax)
		self.radiusMin = float(radiusMin)
		self.centerX = float(centerX)
		self.centerY = float(centerY)
		self.horizontalStride = float(horizontalStride)
		self.verticalStride = float(verticalStride)
		self.widthImg = float(widthImage)
		self.heightImg = float(heightImage)

		self.moveNextPosition = True

		self.currentAngle = 0.0
		self.currentRadius = self.radiusMin

		self.currentPosition = [self.centerX, self.centerY]

# ---------------------------------------------------------------------------
	def getPosition(self):
		return [int(i) for i in self.currentPosition]

# ---------------------------------------------------------------------------
	def getNextPosition(self):

		if not self.moveNextPosition:
			return self.currentPosition

		self._calculateCurrentPosition()

		if self._getIncreaseAngle() >= 2:
			self._restAngle()
			if self._getIncreaseRadius() >= self.radiusMax:
				self.moveNextPosition = False
			else:
				self._increaseRadius()
		else:
			self._increaseAngle()

		return [int(i) for i in self.currentPosition]

# ---------------------------------------------------------------------------
	def hasNextPosition(self):
		return self.moveNextPosition

# ---------------------------------------------------------------------------
	def resetPosition(self):
		self.currentPosition = [self.centerX, self.centerY]

# ---------------------------------------------------------------------------
	def _restAngle(self):
		self.currentAngle = 0

# ---------------------------------------------------------------------------
	def _resetRadius(self):
		self.currentRadius = self.radiusMin

# ---------------------------------------------------------------------------
	def _calculateCurrentPosition(self):
		self._calculateCoordenateX()
		self._calculateCoordenateY()

# ---------------------------------------------------------------------------
	def _calculateCoordenateY(self):
		self.currentPosition[1] = sin(self.currentAngle * pi) * self.currentRadius + self.centerY

# ---------------------------------------------------------------------------
	def _calculateCoordenateX(self):
		self.currentPosition[0] = cos(self.currentAngle * pi) * self.currentRadius + self.centerX

# ---------------------------------------------------------------------------
	def _getIncreaseAngle(self):
		return self.currentAngle + self.horizontalStride

# ---------------------------------------------------------------------------
	def _getIncreaseRadius(self):
		return self.currentRadius + self.verticalStride

# ---------------------------------------------------------------------------
	def _increaseAngle(self):
		self.currentAngle = self._getIncreaseAngle()

#---------------------------------------------------------------------------
	def _increaseRadius(self):
		self.currentRadius = self._getIncreaseRadius()
#######################################################################################################################
if __name__ == '__main__':
	horizontalStride = 0.3
	verticalStride = 70
	radiusMax = 200
	radiusMin = 50
	centerX = 350
	centerY = 300
	widthImage = 703
	heightImage = 627
	trayectoria = CircularTrajectory(horizontalStride,
									 verticalStride,
									 radiusMax,
									 radiusMin,
									 centerX,
									 centerY,
									 widthImage,
									 heightImage)
	print trayectoria.getPosition()
	while trayectoria.hasNextPosition():
		print trayectoria.getNextPosition(), 'Angulo: '+str(trayectoria.currentAngle), "radio: "+str(trayectoria.currentRadius)

#######################################################################################################################
