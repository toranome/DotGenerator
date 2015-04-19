Generated DOT files for GraphViz

E.g:
{{BasicExample.dot}}
{{SequenceExample.dot}}

Input files
SampleSequenceInput.xml

Syntax:
    Human.Has(Legs); // Human = higher hierarchy
    Human.Owns(Pet); // Human = higher hierarchy
    Dog.Is(Animal); // Dog = lower hierarchy
    Pet.OwnedBy(Human); // Pet = lower hierarchy
    Legs.PartOf(Animal); // Legs = lower hierarchy
