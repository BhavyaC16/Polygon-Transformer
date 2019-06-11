# AUTHOR: BHAVYA CHOPRA

import matplotlib.pyplot as plt
import math
import copy

class polygon(object):
	def __init__(self,x,y):
		'''
			The constructor initialises the object/instance of the class polygon with two attributes:
			The list of x coordinates and a separate list of y coordinates of the vertices of the polygon.
		'''
		self.x = x
		self.y = y

	def transform(self,s):
		'''
			The transform() function takes the instruction as an input parameter and generates the list of 
			vertices to be plotted after the transformation has been applied to the existing polygon.
			It also updates the existing list of vertices of the polygon.
		'''
		matrix = self.transformation_matrix(s)
		n_vertex = []
		for i in range(0,len(self.x)):
			vertex = [self.x[i],self.y[i],1]
			n_vertex = self.multiply(matrix,vertex)
			self.x[i] = n_vertex[0]
			self.y[i] = n_vertex[1]
		vertices = self.plot_figure()
		return vertices
		
	def plot_figure(self):
		'''
			The plot_figure() function returns the list of x and y coordinates of the polygon to be plotted.
		'''
		a = copy.deepcopy(self.x)
		b = copy.deepcopy(self.y)
		a.append(self.x[0])
		b.append(self.y[0])
		return [a,b]	

	def transformation_matrix(self,s):
		'''
			The transformation_matrix() function takes the instruction entered by the user as an input parameter
			and depending upon the type of transformation, generates the transformation matrix to be multiplied to 
			each vertex of the polygon.
		'''
		matrix = []
		if s[0]=='S':
			i = s.find(' ',2)
			sx = float(s[2:i])
			sy = float(s[i+1:])
			matrix.append([sx,0,0])
			matrix.append([0,sy,0])
			matrix.append([0,0,1])
		elif s[0]=='R':
			theta_deg = float(s[2:])
			theta_rad = theta_deg*(math.pi/180.0)
			a = math.sin(theta_rad)
			b = math.cos(theta_rad)
			matrix.append([b,-a,0])
			matrix.append([a,b,0])
			matrix.append([0,0,1])
		elif s[0]=='T':
			i = s.find(' ',2)
			dx = float(s[2:i])
			dy = float(s[i+1:])
			matrix.append([1,0,dx])
			matrix.append([0,1,dy])
			matrix.append([0,0,1])
		return matrix

	def multiply(self,matrix,vertex):
		'''
			The multiply() function takes the transformation matrix and a vertex of the polygon as input parameters and
			returns the matrix product of the two as the new vertex.
		'''
		new_vertex = []
		for i in range(0,len(matrix)):
			row = []
			for k in range(1):
				t=0
				for j in range(0,len(vertex)):
					t = t + (matrix[i][j]*vertex[j])
				row.append(t)
			new_vertex+=row 
		return new_vertex

class disc(object):
	def __init__(self,a,b,r1):
		'''
			The constructor initialises the object/instance of the class disc with the following attributes:
			The list of x coordinates and a separate list of y coordinates of the points of the disc, 
			the x and y coordinatesof the center of the circle, the semi-major and semi-minor axes of the disc,
			and the x and y coordinates of the vetices corresponding to the major and minor axes of the ellise.
		'''
		self.a = a
		self.b = b
		self.r1 = r1
		self.r2 = r1
		points = self.circle()
		self.x = points[0]
		self.y = points[1]
		self.vert_1 = [self.a+self.r1,self.b,1.0]
		self.vert_2 = [self.a,self.r1+self.b,1.0]

	def transform(self,s):
		'''
			The transform() function takes the instruction as an input parameter and generates the list of 
			points to be plotted after the transformation has been applied to the existing disc.
			It also updates the existing list of points of the disc along with the center coordinates and the 
			semi-major and semi-minor axes.
		'''

		matrix = self.transformation_matrix(s)
		for i in range(0,len(self.x)):
			vertex = [self.x[i],self.y[i],1.0]
			n_point = self.multiply(matrix,vertex)
			self.x[i] = n_point[0]
			self.y[i] = n_point[1]
		c = self.multiply(matrix,[self.a,self.b,1.0])
		self.a = c[0]
		self.b = c[1]
		v1 = self.multiply(matrix,self.vert_1)
		self.vert_1 = v1
		self.r1 = abs(v1[0]-self.a)
		v2 = self.multiply(matrix,self.vert_2)
		self.vert_2 = v2
		self.r2 = abs(v2[1]-self.b)
		return [self.x,self.y]


	def circle(self):
		'''
			The circle() function generates and returns the list of x and y coordinates of the disc to be plotted.
		'''
		i = 0
		c = (math.pi)*2
		l1 = []
		l2 = []
		while i<=c:
			x = self.a + self.r1*(math.cos(i))
			y = self.b + self.r2*(math.sin(i))
			l1.append(x)
			l2.append(y)
			i+=0.01
		return [l1,l2]

	def transformation_matrix(self,s):
		'''
			The transformation_matrix() function takes the instruction entered by the user as an input parameter
			and depending upon the type of transformation, generates the transformation matrix to be multiplied to 
			each point of the disc.
		'''
		matrix = []
		if s[0]=='S':
			i = s.find(' ',2)
			sx = float(s[2:i])
			sy = float(s[i+1:])
			matrix.append([sx,0,0])
			matrix.append([0,sy,0])
			matrix.append([0,0,1])
		elif s[0]=='R':
			theta_deg = float(s[2:])
			theta_rad = theta_deg*(math.pi/180.0)
			a = math.sin(theta_rad)
			b = math.cos(theta_rad)
			matrix.append([b,-a,0])
			matrix.append([a,b,0])
			matrix.append([0,0,1])
		elif s[0]=='T':
			i = s.find(' ',2)
			dx = float(s[2:i])
			dy = float(s[i+1:])
			matrix.append([1,0,dx])
			matrix.append([0,1,dy])
			matrix.append([0,0,1])
		return matrix

	def multiply(self,matrix,vertex):
		'''
			The multiply() function takes the transformation matrix and a point of the disc as input parameters and
			returns the matrix product of the two as the new transformed point.
		'''
		new_vertex = []
		for i in range(0,len(matrix)):
			row = []
			for k in range(1):
				t=0
				for j in range(0,len(vertex)):
					t = t + (matrix[i][j]*vertex[j])
				row.append(t)
			new_vertex+=row 
		return new_vertex

	def output(self):
		return [self.a,self.b,self.r1,self.r2]

s = ''
plt.ion()
figure = input()
if figure.lower()=='disc':
	d = list(map(float,input().split()))
	shape = disc(d[0],d[1],d[2])
	l = shape.circle()
	plt.plot(l[0],l[1])

elif figure.lower()=='polygon':
	x = list(map(float,input().split()))
	y = list(map(float,input().split()))
	a = copy.deepcopy(x)
	a.append(x[0])
	b = copy.deepcopy(y)
	b.append(y[0])
	plt.plot(a,b)
	shape = polygon(x,y)
else:
	print('Invalid Input : The figure may be a disc or a polygon.')
	exit() 
while(s.lower()!='quit'):
	points = []
	s = input()
	plt.clf()
	if s.lower()!='quit':
		points = shape.transform(s)
		if figure=='polygon':
			s1 = ''
			s2 = ''
			for i in range(0,len(points[0])-1):
				if i==0:
					s1+=str(points[0][i])
					s2+=str(points[1][i])
				else:
					s1=s1+' '+str(points[0][i])
					s2=s2+' '+str(points[1][i])
			print(s1)
			print(s2)
		elif figure=='disc':
			a = shape.output()
			if a[2]==a[3]:
				print(str(a[0])+' '+str(a[1])+' '+str(a[2]))
			else:
				print(str(a[0])+' '+str(a[1])+' '+str(a[2])+' '+str(a[3]))

		plt.plot(points[0],points[1])
