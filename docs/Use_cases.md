# Use cases
  
The following examples are going to help you become familiar with PySequences.  
The aim of this page is to introduce most of the sequences implementations in PySequences.

<br>

---

<br>

> ## Summary
> ### [Model and draw sequences](#model-and-draw-sequences-1)
> > #### [Model and draw a sequence with a recurrence relation](#model-and-draw-a-sequence-with-a-recurrence-relation-1)
> > #### [Model and draw a sequence with a function formula](#model-and-draw-a-sequence-with-a-function-formula-1)
> > #### [Model and draw a sequence with a list of points](#model-and-draw-a-sequence-with-a-list-of-points-1)
> ### [Multi-sequences drawing](#multi-sequences-drawing-1)

<br>

---

<br>

## Model and draw sequences

This section aims to show how to model sequences, in order to calculate any of their terms.

### Model and draw a sequence with a recurrence relation
> **In this example, we consider the following sequence:**  
> u<sub>0</sub> = 6  
> u<sub>n+1</sub> = (u<sub>n</sub> + 3)<sup>2</sup>

#### Initialize the sequence

> ##### Details:
>
> First, we import the pySequences module:
> ````python
> from pySequences import *
> ````
>
> Now, we need to create a new sequence object with the [Sequence() constructor](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#the-sequence-constructor-1).
>
> For this, we have to use the following syntax:  
> ````Sequence(sequenceType, formula, sequenceName = "u")````
>
> Here are the parameters values in this case:
>
> * **sequenceType** = ````"recurrenceRelation"````
> * **formula:** The syntax for this parameter is quite particular, because it changes depending on the sequenceType value.  
>
>     Here, sequenceType is equal to ````"recurrenceRelation"````.
>    
>     So, the syntax for this parameter is as follows:  
>     ````(n0, u_n0, i, u_nPlusI)````  
>    
>     In this example, we have:
>     * **n0** = ````0````, because the first n-value of the sequence is 0 (u<sub>**0**</sub>).
>     * **u_n0** = `````6`````, because u<sub>0</sub> = **6**.
>     * **i** = ````1````, because the increment is equal to 1 (u<sub>n+**1**</sub>).
>     * **u_nPlusI** = ````lambda u_n: (u_n + 3)**2````, because u<sub>n+1</sub> = (u<sub>n</sub> + 3)<sup>2</sup>.
    
>     **Thus, the formula parameter is equal to:**  
>     `````(0, 6, 1, lambda u_n: (u_n + 3)**2)`````.
>    
> * **sequenceName** = ````"u"````  
>   *Note: Here, you can keep this parameter empty because the default sequenceName value is already "u".*
  
**Here is the full solution:**
````python
from pySequences import *

u = Sequence("recurrenceRelation", (0, 6, 1, lambda u_n: (u_n + 3)**2), "u")
````

#### Calculate a value of the sequence

If you want to display the y-value for n = 5, you just have to add the following line:  
````python
print(u.calc(5))
````

#### Draw the points of the sequence

Before drawing the points on a graph, you need to specify that you want to store them in the pointsList attribute.  
To do so, you have to calculate the point you want to store, with the **store** parameter of the **calc()** method:
````python
# If you want to add the point for n = 8:
u.calc(8, True)
````

Then, the new calculated point is added to the pointsList attribute.

You can now draw the stored points:
````python
u.draw()
````

### Model and draw a sequence with a function formula
> In this example, we consider the sequence defined by the following function:  
> f(x) = 3x<sup>2</sup> - 6   
> v<sub>n</sub> = f(n)

#### Initialize the sequence

> ##### Details:
>
> First, we import the pySequences module:
> ````python
> from pySequences import *
> ````
>
> Now, we need to create a new sequence object with the [Sequence() constructor](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#the-sequence-constructor-1).
>
> For this, we have to use the following syntax:  
> ````Sequence(sequenceType, formula, sequenceName = "u")````
>
> Here are the parameters values in this case:
>
> * **sequenceType** = ````"function"````
> * **formula:** The syntax for this parameter is quite particular, because it changes depending on the sequenceType value.  
>
>     Here, sequenceType is equal to ````"function"````.
>    
>     So, the syntax for this parameter is as follows:  
>     ````function````  (a lambda function representing the function formula used to calculate the sequence values)  
>    
>     In this example, **function** is equal to:  
>     ````lambda n: 3 * n**2 - 6````  
>     because:  
>     v<sub>n</sub> = f(n) = 3n<sup>2</sup> - 6
> * **sequenceName** = ````"v"````

**Here is the full solution:**  
````python
from pySequences import *

v = Sequence("function", lambda n: 3 * n**2 - 6, "v")
````

#### Calculate a value of the sequence

If you want to display the y-value for n = 5, you just have to add the following line:  
````python
print(v.calc(5))
````

#### Draw the points of the sequence

Before drawing the points on a graph, you need to specify that you want to store them in the pointsList attribute.  
To do so, you have to calculate the point you want to store, with the **store** parameter of the **calc()** method:
````python
# If you want to add the point for n = 8:
v.calc(8, True)
````

Then, the new calculated point is added to the pointsList attribute.

You can now draw the stored points:
````python
v.draw()
````

### Model and draw a sequence with a list of points

> In this example, we consider the sequence defined by the following set:  
> w<sub>n</sub> = {(0; 5), (1; 10), (2; 20)}

#### Initialize the sequence

> ##### Details:
>
> First, we import the pySequences module:
> ````python
> from pySequences import *
> ````
>
> Now, we need to create a new sequence object with the [Sequence() constructor](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#the-sequence-constructor-1).
>
> For this, we have to use the following syntax:  
> ````Sequence(sequenceType, formula, sequenceName = "u")````
>
> Here are the parameters values in this case:
>
> * **sequenceType** = ````"pointsList"````
> * **formula:** The syntax for this parameter is quite particular, because it changes depending on the sequenceType value.  
>
>     Here, sequenceType is equal to ````"pointsList"````.
>    
>     So, the syntax for this parameter is as follows:  
>     ````{n0: u_n0, n1: u_n1, ...}````  (the n-values are stored as dict keys and the y-values as dict values)  
>    
>     In this example, function is equal to:  
>     ````{0: 5, 1: 10, 2: 20}````  
>     
> * **sequenceName** = ````"w"````

**Here is the full solution:**  
````python
from pySequences import *

w = Sequence("pointsList", {0: 5, 1: 10, 2: 20}, "w")
````

#### Calculate a value of the sequence

If you want to display the y-value for n = 5, you just have to add the following line:  
````python
print(w.calc(5))
````

#### Draw the points of the sequence

You can draw the points of the sequence with the followig line:
````python
w.draw()
````


## Multi-sequences drawing

Multi-sequences drawing enables to draw several sequences on the same graph.

To do so, we need to use the Trace objects.

> ### Details
>
> #### Initialize sequences and the trace object
>
> ````python
> from pySequences import *
>
> myGraph = Trace(markerSize=10)
>
> u = Sequence("recurrenceRelation", (0, 6, 1, lambda u_n: u_n + 3, "u"))
> v = Sequence("function", lambda n: 1.5 * n, "v")
> ````
>
> #### Add sequences points to the trace object
> 
> First, we have to calculate some points and store them in the pointsList attribute.
> 
> ````python
> # Loop for calculating the sequences values between 0 and 10
> for n_temp in range(0, 10):
>     u.calc(n_temp, True)
>     v.calc(n_temp, True)
> ````
> 
> Now, we have to add the sequences points to the Trace object.  
> To differentiate the two sequences, we will assign them different colors, for example red for **u** and blue for **v**.
> 
> ````python
> myGraph.addPoints(u.pointsList, "red")
> myGraph.addPoints(v.pointsList, "blue")
> 
> myGraph.draw()
> ````

**Here is the full solution:**

````python
from pySequences import *

myGraph = Trace(markerSize=20)

u = Sequence("recurrenceRelation", (0, 6, 1, lambda u_n: u_n + 3, "u"))
v = Sequence("function", lambda n: 1.5 * n, "v")

# Loop for calculating the sequences values between 0 and 10
for n_temp in range(0, 10):
    u.calc(n_temp, True)
    v.calc(n_temp, True)

myGraph.addPoints(u.pointsList, "red")
myGraph.addPoints(v.pointsList, "blue")

myGraph.draw()
````