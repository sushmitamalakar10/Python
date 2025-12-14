# can yu change the values inside a list which is contained in set S?

s = {8, 7, 12, "Sushmita", [1,2]}


# A set can contain only immutable (hashable) elements.
# List is mutable, so it cannot be stored inside a set.

s = {8, 7, 12, "Sushmita", (1, 2)}
# This works because tuple is immutable