# sequencesLib.sequence

The sequence module enables to model sequences and do some operations on them.

## The Sequence() constructor
It enables to create sequences.
````
Sequence(sequenceType, formula, sequenceName = "u")
````
### Parameters
* **sequenceType :**  
    > *type: str*

    > SequencesLib enables to model a sequence by several ways:
    > * By enter a recurrence relation
    > * By enter a function formula
    > * By directly enter the coordinates of each point of the sequence
    
    Thus, the sequenceType parameter accepts 3 values :  
    ````"recurrenceRelation"````, 
    ````"function"```` or  ````"pointsList"````
    
* **formula :**  
    A set of data enabling to build the sequence.  
    The data structure varies depending on the [sequenceType](#sequenceType) value.
    
    * **If sequenceType is equal to "recurrenceRelation":**  
    ````formula = (n0, u_n0, i, u_nPlusI)````
        * **n0:**  
        The first defined n-value of the sequence
        
        * **u_n0:**  
        The y-coordinate in n0
        
        * **i:**  
        The increment given by the recurrence relation
        
        * **u_nPlusI:**  
        The recurrence relation, given by a lambda function returning a number.  
            > For example:  
            ````u_nPlusI = lambda u_n: 2 * u_n + 5````  
    
    * **If sequenceType is equal to "function":**  
    ````formula = functionFormula````
        * **functionFormula:** a lambda function returning a number, which represents a function formula.  
            
            > **For example:**  
            f(x) = 4x² - 2x corresponds to:  
            ````functionFormula = lambda x: 4 * x**2 - 2 * x````
        
    * **If sequenceType is equal to "pointsList":**  
    ````formula = {n0: y_n0, n1: y_n1, ...}````  
        * In this case, formula is a dictionary whose each item represents a point.
            > **For example:**  
            We consider that u is a sequence defined by the set {(0, 1), (1, 5), (2, 10)}.  
            ````formula = {0: 1, 1: 5, 2: 10}````
    
 * **sequenceName:**  
    >   *type: str*  
        *default value: "u"*  

    The name of the sequence.
    
    
## The Sequence objects attributes

These attributes are used by the Sequence instances.  
(not by the Sequence class itself)

### Sequence.name
*type: str*  

The name of the sequence.
    
### Sequence.type

*type: str*

The type of the sequence.
  
**Possible values:** "recurrenceRelation", "function" or "pointsList"

### Sequence.pointsList

*type: dict*

The list of the stored points of the sequence.
> Sequence points can be stored with the [calc()]() method.

> If the sequence type is a [points list](#Parameters), the entered points are automatically stored in Sequence.pointsList.

### Sequence.constants

*type: list*