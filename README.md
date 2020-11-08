# Inverse-Effect
Grayscale filter is a widely used and popular filter used by youngsters. Lets try making a filter of our own through Image Processing.

## Tools and Languages:
<img align="left" alt="OpenCV" width="26px" src="opencv.png" >
<img align="left" alt="VS Code" width="26px" src="visual-studio-code.png" >
<img align="left" alt="pip" width="26px" height="34px" src="pip.png" >
<img align="left" alt="Python" width="26px" src="python.png" >
<br>

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cv2 and numpy.


```bash
pip install cv2
pip install numpy
```

## Import

```python
import cv2
import numpy as np
```

## Reading image from file

```python
img = cv2.imread("cat.png")
```


## Gray scale

```python
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
```

## Completion message

```python
print('Image Grayscaled.')
```

## Comparing original vs grayscale

```python
cv2.imshow('ORIGINAL',img)
cv2.imshow('GRAYSCALE',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Images
<p align="center">
	<img src="cat.png" alt="Logo", height=250px,width=350px>
	<img src="Converted-Gray.PNG" alt="Gray", height=250px,width=350px>
</p>

### Developed by
 [Ashish ku. Behera](https://github.com/ashish-max "Github Id")
