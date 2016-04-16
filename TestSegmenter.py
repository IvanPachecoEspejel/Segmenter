from Segmenters import RectangularSegmenter
from Trajectories import SimpleTrajectory, CircularTrajectory
from PIL.Image import open

if __name__ == '__main__':
	img = open('/home/ivan/Imagenes/Fondos/chika1.jpg')

	horizontalStride = 60
	verticalStride = 100
	topOffset = 125
	bottomOffset = 125
	rigthOffset = 125
	leftOffset = 125
	widthCut = 250
	heighCut = 250
	widthImage, heightImage = img.size

	trajectory = SimpleTrajectory(horizontalStride, verticalStride, topOffset, leftOffset, rigthOffset, bottomOffset,
								  widthImage, heightImage)

	horizontalStride = 0.3
	verticalStride = 70
	radiusMax = 200
	radiusMin = 50
	centerX = 350
	centerY = 300
	widthImage = 703
	heightImage = 627
	trajectoryCircular = CircularTrajectory(horizontalStride,
											verticalStride,
											radiusMax,
											radiusMin,
											centerX,
											centerY,
											widthImage,
											heightImage)

	segmenter = RectangularSegmenter(img, heighCut, widthCut, trajectoryCircular)

	i = 0
	image = segmenter.getCurrentSegment()
	image.PILImage.save('/home/ivan/Escritorio/RecortesTest/recorte' + str(i) + '.jpg')
	print str(i) + ' -- ' + str(image.xPositionClipper) + ' -- ' + str(image.yPositionClipper)
	i += 1
	while (segmenter.hasNextSegment()):
		image = segmenter.getNextSegment()
		image.PILImage.save('/home/ivan/Escritorio/RecortesTest/recorte' + str(i) + '.jpg')
		print str(i) + ' -- ' + str(image.xPositionClipper) + ' -- ' + str(image.yPositionClipper)
		i += 1
