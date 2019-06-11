# Polygon-Transformer
Polygon-Transformer lets you visualize polygons, circles and ellipses, as well as the following geometrical transformations:

   - Translation
   - Rotation
   - Scaling

## Usage
1. Run [polygonTransformer.py](https://github.com/BhavyaC16/Polygon-Transformer/blob/master/polygonTransformer.py)
2. In the first line, enter the type of geometric object you wish to create. It can either be a POLYGON, or a DISC. In the next line, you specify the object coordinates and dimensions as follows:
```
  POLYGON 
  for n sided polygon, enter space separated list of X coordinates of vertices in the first line
  enter space separated list of corresponding Y coordinates in the second line
  
  DISC
  for a circle, this line contains the following space separated attributes: centerX centerY radius
```
3. Now, any of the following commands can be used for any number of times:
```
  T x y
    Translates the 2D object by x units on the X axis, and Y units on the Y axis
  R theta
    Rotates the 2D object by theta degrees in the anti-clockwise direction
  S x y
    Scales the 2D object by x times about the X axis, and y times about the Y axis
```
4. To exit the program, type 'quit'.

## Output
After each command, the transformed figure is plotted, and the attributes of the transformed figure are displayed as follows:
```
  POLYGON:
    line 1: list of x coordinates of transformed object
    line 2: list of y coordinates of transformed object
  
  DISC:
    centerX centerY majorAxis minorAxis
```

## Sample Input and Output
### Input
```
  polygon
  1 -1 -1 1
  1 1 -1 -1
  S 2 1
  R 90
  T 0 -2
  quit
```
### Output
```
  2 -2 -2 2
  1 1 -1 -1
  
  -1 -1 1 1
  2 -2 -2 2
  
  -1 -1 1 1
  0 -4 -4 0
```
