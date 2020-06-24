# pySequences.sequence

The sequence class enables to model sequences and do some operations on them.  

## The Sequence() constructor
The Sequence() constructor enables to create sequences.  
````
Sequence(sequenceType, formula, sequenceName = "u")
````
### Parameters
* #### sequenceType :  
    > *type: str*

    > PySequences enables to model sequences in several ways:
    > * By entering a recurrence relation  
    > * By entering a function formula  
    > * By directly entering the coordinates of each point of the sequence  
    
    Thus, the sequenceType parameter accepts 3 values :  
    ````"recurrenceRelation"````, 
    ````"function"```` or  ````"pointsList"````
    
* #### formula :  
    A set of data enabling to build the sequence.  
    The data structure varies depending on the [sequenceType](#sequencetype-) value.
    
    * ##### If sequenceType is equal to "recurrenceRelation":  
        ````formula = (n0, u_n0, i, u_nPlusI)````  
        * ###### n0:   
            The first defined n-value of the sequence.  
        
        * ###### u_n0: 
            The y-coordinate in n0.  
        
        * ###### i:  
            The increment given by the recurrence relation, aka the step between each point of the sequence.  
        
        * ###### u_nPlusI:  
            The recurrence relation, given by a lambda function returning a number.  
            > For example:  
            ````u_nPlusI = lambda u_n: 2 * u_n + 5````    
    
    * ##### If sequenceType is equal to "function":  
        ````formula = functionFormula````  
        * ###### functionFormula:  
            A lambda function returning a number, which represents a function formula.  
            
            > **For example:**  
            f(x) = 4x² - 2x corresponds to:  
            ````functionFormula = lambda x: 4 * x**2 - 2 * x````
        
    * ##### If sequenceType is equal to "pointsList":  
        ````formula = {n0: y_n0, n1: y_n1, ...}````  
        > In this case, formula is a dictionary whose each item represents a point. 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        > **For example:**  
        We consider that u is a sequence defined by the set {(0, 1), (1, 5), (2, 10)}.  
        ````formula = {0: 1, 1: 5, 2: 10}````
    
 * #### sequenceName:   
    >   *type: str*  
        *default value: "u"*  

    The name of the sequence.  
    
<br>
    
## The Sequence objects Attributes

*Note: These attributes are used by the Sequence instances.  
(not by the Sequence class itself)*  

### Generic attributes

*The following attributes are common to all the Sequence objects.*  

* #### Sequence.name
    > *type: str*  
    
    The name of the sequence.  
    
* #### Sequence.type

    > *type: str*
    
    The type of the sequence.  
  
    **Possible values:** "recurrenceRelation", "function" or "pointsList"  

* #### Sequence.pointsList

    > *type: dict*
    
    The list of the stored points of the sequence.  
    > Sequence points can be stored with the [calc()](#sequencecalc) method.
    
    > If the sequence type is a [points list](#sequencepointslist), the entered points are automatically stored in Sequence.pointsList.

* #### Sequence.constants

    > *type: dict*  
      *default value: { }*  
    
    The list of the constants used to calculate the y-coordinates of each point of the sequence.  
    
    ##### How and when to use the Sequence.constants attribute ?  
    
    This attribute is useful when a lambda function defining the sequence contains a variable whose value is not known in advance.
    
    > **Example :**  
    We want to create a sequence given by an affine function formula, under the form **ax + b**.  
    In our case, **a** and **b** values have to be entered by the user.
    > 
    > > The following solution **is not correct**:
    > > ````python
    > > def affineSequence(a, b):
    > >   return Sequence("function", lambda x: a, b)
    > > ````
    > > Indeed, in the lambda function, **a and b variables** do not refer to the **a and b parameters** (given in the function definition).  
        They are undefined. 
    >  
    > To solve this problem, you can store the **a and b** parameters values as sequence constants, as you can see below:
    > ````python
    > def affineSequence(a, b):
    >   u = Sequence("function", lambda x: u.constants[a], u.constants[b])
    >   u.constants["a"] = a    # Store the a parameter value in the sequence object
    >   u.constants["b"] = b    # Store the b parameter value in the sequence object
    >   return u
    > ````
    > In the lambda function, the **a and b parameters values** are now indicated by **u.constants["a"]** and **u.constants["b"]**.
    > 
    > After having defined the sequence, we add it the **a** and **b** constants.
      For this, we have to define these constants with the following structure: 
    > ````python
    > mySequence.constants["constantName"] = constantValue
    > ````
    > Then, the lambda function will be able to access these constants.  
    > 

### Additional attributes for the sequences defined by a recurrence relation

* #### Sequence.n0
  The first defined n-value of the sequence.  
  
  > **See also:**  
  > * [n0 in the formula parameter of the Sequence() constructor](#n0) 

* #### Sequence.u_n0
  The y-coordinate of the sequence point in n0.  
  
  > **See also:**  
  > * [u_n0 in the formula parameter of the Sequence() constructor](#u_n0) 

* #### Sequence.stepI
  The increment given by the recurrence relation, aka the step between each point of the sequence.  
  
  > **See also:**  
  > * [i in the formula parameter of the Sequence() constructor](#i) 

* #### Sequence.u_nPlusI
  The recurrence relation, given by a lambda function returning a number.  
  
  > **For example:**  
    u_nPlusI = lambda u_n: 2 * u_n + 5

  > **See also:**  
  > * [u_nPlusI in the formula parameter of the Sequence() constructor](#u_nPlusI) 


### Additional attributes for the sequences defined by a function formula

* #### Sequence.formula
  The lambda function which represents the function formula used to calculate the sequence points coordinates.  
  
  > **See also:**  
  > * [functionFormula in the formula parameter of the Sequence() constructor](#functionFormula)

<br>

## The Sequence objects Methods

* ### Sequence.calc()
  Calculate the y-coordinate of the sequence for a given n-value.  
  
  ````calc(n, store_point: bool = False)````  
  > *return: float*
  
  * #### n:
    > *type: int*  
      *default value: None*  
    
    The n-value for which to calculate the y-coordinate of the sequence.
  
  * #### store_point:
    > *type: bool*  
      *default value: False*  
    
    A boolean indicating if the calculated point must be stored in [Sequence.pointsList](#sequencepointslist).
  
* ### Sequence.draw()
  Place the points of the sequence on a graph.  
  
  ***Note:** Only the points stored in the Sequence.pointsList attribute are placed on the graph.*  
  
  *For more information, refer to the store attribute of [Sequence.calc()](sequencecalc).*  
  
  ````trace(markerSize: float = 2, markerColor="0")````  

  * #### markerSize:
    The size of the point on the graph (in pt).
  
  * #### markerColor:
    The color of the point on the graph.
    
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

* ### Sequence.printAllStoredPoints()
  Display in the console each point of the sequence, under the following form:  
  ````u_0 = 1````  
  ````u_1 = 2````  
  ````...````  
  
  ***Note:** Only the points stored in the Sequence.pointsList attribute are placed on the graph.*  
  
  *For more information, refer to the store attribute of [Sequence.calc()](sequencecalc).*  
  
  ````printAllStoredPoints()````  
  
  
<br>

---

[Back to top ⮥](#pysequencessequence)

