# pySequences.trace

The trace class enables to draw points on a graph, independently of their belonging to a sequence.  

Thus, this class allows you to draw different sequences on the same graph, which is not possible with the Sequence.draw() method.

<br>

---

<br>

> ## Summary
> ### [The Trace() constructor](#the-trace-constructor-1)
> ### [The Trace objects Attributes](#the-trace-objects-attributes-1)
> > #### [Trace.pointsList](#tracepointslist-1)
> ### [The Trace objects Methods](#the-trace-objects-methods-1)
> > #### [Trace.addPoint()](#traceaddpoint-1)
> > #### [Trace.addPoints()](#traceaddpoints-1)
> > #### [Trace.draw()](#tracedraw-1)

<br>

---

<br>

## The Trace() constructor
The Trace() constructor enables to create trace objects.  
These objects enable to draw any points on the same graph, no matter their belonging to a sequence.  
This enables to draw  different sequences on the same graph.
  
````
Trace(pointsList=None, markerColor="0", markerSize: float = 2)
````

### Parameters
* #### pointsList:  
    > *type: dict*

    A list of points to add on the graph at the trace object initialization.  
    
* #### markerColor:  
    Define the default color of the new points.  
    
    > **Possible values:**  
    >  - A scalar or sequence of n numbers to be mapped to colors using cmap and norm.  
    >  - A 2-D array in which the rows are RGB or RGBA.  
    >  - A sequence of colors of length n.  
    >  - A single color format string.   
    >      
    > <br>     
    > Note that c should not be a single numeric RGB or RGBA sequence because that is indistinguishable from an array of values to be colormapped. If you want to specify the same RGB or RGBA value for all points, use a 2-D array with a single row. Otherwise, value- matching will have precedence in case of a size matching with x and y.  
    >  
    >  <br>  
    >  <br>  
    > If you wish to specify a single color for all points prefer the color keyword argument.  
    >  
    >  <br>  
    >  <br>  
    > Defaults to None. In that case the marker color is determined by the value of color, facecolor or facecolors. In case those are not specified or None, the marker color is determined by the next color of the Axes' current "shape and fill" color cycle. This cycle defaults to rcParams["axes.prop_cycle"] (default: cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])).  
    >  
    >  <br>
    >  
    >  **(Source: [Matplotlib documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html))**

* #### markerSize:  
    > *type: float*  
    Define the default size of the new points (in pt).

<br>

## The Trace objects Attributes

### Trace.pointsList
   > *type: dict*

   The list of the points belonging to the trace object, under the following form:  
   ````{n0: u_n0, n1: u_n1, n2: u_n2, ...}````
   * The key of each tuple represents the n-value of the point.
   * The value of each tuple represents the y-value of the point.
   
   > **Example:**  
   > The sequence **u** defined as follows:  
   > * u<sub>0</sub> = 10  
   > * u<sub>1</sub> = 15  
   > * u<sub>2</sub> = 27.5  
   > 
   > corresponds to the following **pointsList** value:  
   > ````{0: 10, 1: 15, 2: 27.5}````

<br>


## The Trace objects Methods

### Trace.addPoint()  
Add a new point to the trace object.  

````Trace.addPoint(n, y, markerColor="0", markerSize: float = 2)````  

* #### n:
  The n-value of the point.
  
* #### y:
  The y-value of the point.
  
* #### markerSize:
  The size of the point on the graph (in pt).

* #### markerColor:
    Define the color of the point.  
    
    > **Possible values:**  
    >  - A scalar or sequence of n numbers to be mapped to colors using cmap and norm.  
    >  - A 2-D array in which the rows are RGB or RGBA.  
    >  - A sequence of colors of length n.  
    >  - A single color format string.   
    >      
    > <br>     
    > Note that c should not be a single numeric RGB or RGBA sequence because that is indistinguishable from an array of values to be colormapped. If you want to specify the same RGB or RGBA value for all points, use a 2-D array with a single row. Otherwise, value- matching will have precedence in case of a size matching with x and y.  
    >  
    >  <br>  
    >  <br>  
    > If you wish to specify a single color for all points prefer the color keyword argument.  
    >  
    >  <br>  
    >  <br>  
    > Defaults to None. In that case the marker color is determined by the value of color, facecolor or facecolors. In case those are not specified or None, the marker color is determined by the next color of the Axes' current "shape and fill" color cycle. This cycle defaults to rcParams["axes.prop_cycle"] (default: cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])).  
    >  
    >  <br>
    >  
    >  **(Source: [Matplotlib documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html))**
  

### Trace.addPoints()  
Add new points to the trace object. 

````Trace.addPoints(pointsList: dict, markerColor="0", markerSize: float = 2)````

* #### pointsList:
  The list of the points to add, under the following form:  
  ````{n0: u_n0, n1: u_n1, n2: u_n2, ...}````

    * The key of each tuple represents the n-value of the point.
    * The value of each tuple represents the y-value of the point.


* #### markerSize:
  The size of the points to add on the graph (in pt).

* #### markerColor:
  The color of the points to add on the graph (in pt).  
    > **Possible values:**  
    >  - A scalar or sequence of n numbers to be mapped to colors using cmap and norm.  
    >  - A 2-D array in which the rows are RGB or RGBA.  
    >  - A sequence of colors of length n.  
    >  - A single color format string.   
    >      
    > <br>     
    > Note that c should not be a single numeric RGB or RGBA sequence because that is indistinguishable from an array of values to be colormapped. If you want to specify the same RGB or RGBA value for all points, use a 2-D array with a single row. Otherwise, value- matching will have precedence in case of a size matching with x and y.  
    >  
    >  <br>  
    >  <br>  
    > If you wish to specify a single color for all points prefer the color keyword argument.  
    >  
    >  <br>  
    >  <br>  
    > Defaults to None. In that case the marker color is determined by the value of color, facecolor or facecolors. In case those are not specified or None, the marker color is determined by the next color of the Axes' current "shape and fill" color cycle. This cycle defaults to rcParams["axes.prop_cycle"] (default: cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])).  
    >  
    >  <br>
    >  
    >  **(Source: [Matplotlib documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html))**
  
  
### Trace.draw()  
Draw all the points of the trace object on a graph.

````Trace.draw()````

<br>

---

[Back to top ⮥](#pysequencestrace)
