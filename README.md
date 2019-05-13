# Logik

This program provide a simple way to manipulate and interact with propositional logic expressions.

## NOTES

> Logik is an educationnal project. It is not designed to be powerful and robust. But it can be used as a tool to solve logic exercices at a Bachelor level.

> If you want to take part in the developpement of Logik in any way you want, feel free to pull request !

## FEATURES

Logik provides 3 main features :

+ Evaluating expressions from the propositional logic
+ Building truth tables from parametrized expressions
+ Extracting the syntax tree of an expression

## How to use Logik ?

Logik is designed to be use in a terminal. You can start Logik by executing `evaluator.py` :

```
$ python3 evaluator.py
```

### Syntax

The syntax of the expressions in Logik is really simple :

**True | Top**
```
1
```

**False | Bottom**
```
0
```

**Implications**
```
a -> b
```

**Conjunction**
```
a et b
```

**Disjunction**
```
a ou b
```

**Negation**
```
non a
```

You can use parenthesis to write some more complex expressions :

```
(a ou b) -> (a et c) or ((a et d) or (b -> (c and e)))
```

When you type expression with free variables like : `a -> b`, Logik automatically returns the associated truth table. In ou case it returns the following table :

```
a b
----
0 0 1
0 1 1
1 0 0
1 1 1
```

It will also return the associated syntax tree :

```
->
  a
  b
```

## TODO(S)

There is still a lot of things which can be added to improve this project. Here is a list of cool features to add in the future :

+ SAT Solver
+ Predicate logic
+ API to manipulate formulas directly in any python project
+ and more ... (feel free to propose your own suggestions)
















