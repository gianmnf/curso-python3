"""
Sets - Sets in Python (set type)
Sets are taught in mathematics
https://brasilescola.uol.com.br/matematica/conjunto.htm
Graphically represented by Venn diagram
Sets in Python are mutable, but they only accept
immutable types as internal value.
"""

# s1 = set() - empty set
# s1 = {'Gian', 1, 2, 3}
# print(s1)

"""
Sets are efficient for removing duplicate values
of iterables.
- Do not accept mutable values;
- Your values will always be unique;
- has no indexes;
- do not guarantee order;
- are iterable (for, in, not in)

Useful methods:
add, update, clear, discard

Useful operators:
union - Unites
intersection - Items present in both
difference - Items present only in the set on the left
symmetric difference ^ - Items that are not in both
"""

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
s1 ={1, 2, 3}
print(4 in s1)
for numero in s1:
    print(numero)