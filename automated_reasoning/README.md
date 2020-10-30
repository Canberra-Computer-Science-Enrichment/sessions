# Logic and Automated Reasoning

## Propositional Logic

| Symbol | English | Other symbols |
| --- | --- | --- |
| ⊤ | true | 1, *T* |
| ⊥ | false | 0, *F* |
| ¬*p* | not *p* | *&#x305;p*, -*p*, ~*p* |
| *p* ∧ *q* | *p* and *q* | *pq*, *p*&*q*, *p* ⋅ *q* |
| *p* ∨ *q* | *p* or *q* | *p* + *q*, *p* | *q* |
| *p* → *q* | *p* implies *q* | *p* ⇒ *q*, *p* ⊃ *q* |
| *p* ↔ *q* | *p* if and only if (iff) *q* | *p* ⇔ *q*, *p* = *q*, *p* ≡ *q* |

## Tautologies

- ¬⊤ ↔ ⊥
- ¬⊥ ↔ ⊤
- ¬¬*p* ↔ *p*
- *p* ∧ *p* ↔ *p*
- *p* ∧ ¬*p* ↔ ⊥
- *p* ∨ *p* ↔ *p*
- *p* ∨ ¬*p* ↔ ⊤
- *p* ∧ *q* ↔ *q* ∧ *p*
- *p* ∧ (*q* ∧ *r*) ↔ (*p* ∧ *q*) ∧ *r*
- *p* ∨ *q* ↔ *q* ∨ *p*
- *p* ∨ (*q* ∨ *r*) ↔ (*p* ∨ *q*) ∨ *r*

### Implication

- *p* → *q* ↔ ¬*p* ∨ *q*
- *p* → ¬*q* ↔ ¬*p* ∨ ¬*q*

### Contraposition

- *p* → *q* ↔ ¬*q* → *p*
- *p* → ¬*q* ↔ *q* → ¬*p*

### Distribution

- *p* ∨ (*q* ∧ *r*) ↔ (*p* ∨ *q*) ∧ (*p* ∨ *r*)
- *p* ∧ (*q* ∨ *r*) ↔ (*p* ∧ *q*) ∨ (*p* ∧ *r*)

### De Morgan's Laws

- ¬(*p* ∧ *q*) ↔ ¬*p* ∨ ¬*q*
- ¬(*p* ∨ *q*) ↔ ¬*p* ∧ ¬*q*
- *p* ∧ *q* ↔ ¬(¬*p* ∨ ¬*q*)
- *p* ∨ *q* ↔ ¬(¬*p* ∧ ¬*q*)

## Conjunctive Normal Form (CNF)

A statement in conjunctive normal form is composed of only literals (e.g. *p*, *¬q*, ⊤, ⊥) and the connectives ∨ and ∧. Furthermore, it is a conjunction of disjunctions:

C<sub>1</sub> ∧ C<sub>2</sub> ∧ … ∧ C<sub>n</sub> 

where each clause C<sub>i</sub> is of the form:

C<sub>i</sub> = l<sub>i1</sub> ∨ l<sub>i2</sub> ∨ … ∨ l<sub>im</sub>

A set of *m* clauses in CNF that reference *n* variables can be encoded as a [DIMACS CNF format text file](https://jix.github.io/varisat/manual/0.2.0/formats/dimacs.html) as follows:

````
p cnf n m
1 2 0
-3 4 0
...
````

## Brain Teasers

Try encoding the following problems to conjunctive normal form.

Once you believe you have a correct encoding (and have represented it as a DIMACS CNF text format), run it through [MiniSAT online](https://msoos.github.io/cryptominisat_web/) to find the solution.

### Knight and Knave

Each of A and B are either a knight or a knave. A knight always tells the truth; a knave always lies.

A says: "At least one of us is a knave."

Who is a knight and who is a knave?

### Knight, Knave, Knormal

(from [What is the Name of This Book?](https://www.goodreads.com/book/show/493576.What_Is_the_Name_of_This_Book_) by Raymond Smullyan)

There are three people, Anna, Bella, and Charlie. One is a knight, who always tells the truth. One is a knave, who always lies. One is a normal person, who sometimes tells the truth and sometimes tells lies. They each make one statement:

A. I am normal.

B. A's statement is true.

C. I am not normal.

### Pet Show

Solve the [Pet Show problem from John Slaney's Logic4Fun](https://l4f.cecs.anu.edu.au/puzzles/intermediate/pet-show)

### 5x5

Can you fill a 5x5 grid with the letters a, b, c, d, e so that no letter is repeated in any row, column, or diagonal?

### Sudoku

Can you build a solver for [4x4 Sudoku puzzles](http://sudoku4me.com/sudoku%204x4.php)?

Hint: imagine dividing the CNF into two parts: a general set of clauses that apply to any puzzle, and a specific set of clauses that represent the setup of a particular puzzle.
