# PySequences

PySequences is a small python module for modeling sequences and plotting them on a graph.

It enables to model a sequence in several ways:
* By entering a recurrence relation
* By entering a function formula
* By directly entering the coordinates of each point of the sequence

Then, you will be able to calculate any term of the sequence and plot it on a graph.

---

## Licence

This module implements basic tools, but anyone can improve it and publish new versions.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

---

## Documentation

> ### [Getting started](https://github.com/FlorianVaneste/PySequences/wiki/Getting_started) 
> > #### [Install dependencies](https://github.com/FlorianVaneste/PySequences/wiki/Getting_started#install-dependencies) 
> > > ##### [Install Python 3](https://github.com/FlorianVaneste/PySequences/wiki/Getting_started#install-python-3)  
> > > ##### [Install matplotlib](https://github.com/FlorianVaneste/PySequences/wiki/Getting_started#install-matplotlib)  
> > #### [Import PySequences](https://github.com/FlorianVaneste/PySequences/wiki/Getting_started#import-pysequences)  
> ### [The Sequence class](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class)  
> > #### [The Sequence() constructor](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#the-sequence-constructor-1)
> > #### [The Sequence objects Attributes](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#the-sequence-objects-attributes-1)
> > > ##### [Generic attributes](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#generic-attributes-1)  
> > > > ###### [Sequence.name](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequencename-1)  
> > > > ###### [Sequence.type](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequencetype-1)  
> > > > ###### [Sequence.pointsList](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequencepointslist-1)  
> > > > ###### [Sequence.constants](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequenceconstants-1)  
> > > ##### [Additional attributes for the sequences defined by a recurrence relation](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#additional-attributes-for-sequences-defined-by-a-recurrence-relation-1)  
> > > > ###### [Sequence.n0](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequencen0-1)
> > > > ###### [Sequence.u_n0](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequenceu_n0-1)
> > > > ###### [Sequence.stepI](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequencestepi-1)
> > > > ###### [Sequence.u_nPlusI](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequenceu_nplusi-1)
> > > ##### [Additional attributes for the sequences defined by a function formula](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#additional-attributes-for-sequences-defined-by-a-function-formula-1)  
> > > > ###### [Sequence.formula](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequenceformula-1)
> > #### [The Sequence objects Methods](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#the-sequence-objects-methods-1)
> > > #### [Sequence.calc()](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequencecalc-1)
> > > #### [Sequence.draw()](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequencedraw-1)
> > > #### [Sequence.printAllStoredPoints()](https://github.com/FlorianVaneste/PySequences/wiki/The_Sequence_class#sequenceprintallstoredpoints-1)
> ### [The Trace class](https://github.com/FlorianVaneste/PySequences/wiki/The_Trace_class)  
> > #### [The Trace() constructor](https://github.com/FlorianVaneste/PySequences/wiki/The_Trace_class#the-trace-constructor-1)
> > #### [The Trace objects Attributes](https://github.com/FlorianVaneste/PySequences/wiki/The_Trace_class#the-trace-objects-attributes-1)
> > > ##### [Trace.pointsList](https://github.com/FlorianVaneste/PySequences/wiki/The_Trace_class#tracepointslist-1)
> > #### [The Trace objects Methods](https://github.com/FlorianVaneste/PySequences/wiki/The_Trace_class#the-trace-objects-methods-1)
> > > ##### [Trace.addPoint()](https://github.com/FlorianVaneste/PySequences/wiki/The_Trace_class#traceaddpoint-1)
> > > ##### [Trace.addPoints()](https://github.com/FlorianVaneste/PySequences/wiki/The_Trace_class#traceaddpoints-1)
> > > ##### [Trace.draw()](https://github.com/FlorianVaneste/PySequences/wiki/The_Trace_class#tracedraw-1)
> ### [Use cases](https://github.com/FlorianVaneste/PySequences/wiki/Use_cases)
