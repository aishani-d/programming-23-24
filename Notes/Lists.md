In Python, lists are a collection of items
We store values inside of lists
The values of the items can be different [[Types]]
Order matters in a list

# Creating a List
To make a list, we use brackets \[\] to surround our list
We separate the individual items with commas 

```python 
some_list = ["Jimmy", "Sara", "Frederique"]
```

# Access Elements in the List
We can access the individual things from lists using **bracket notation**
In the example below, we'll use bracket notation to access "Sara"

```python
some_list[1]         # "Sara"
some_list[0]         # "Jimmy"
some_list[2]         # "Frederique"
some_list[-1]         # "Frederique" counts from the end
some_list[-2]         # "Sara"
```

Inside the brackets, we give the *index* of the item we want 
Python uses **0-index** counting, which means we start counting at 0

# Modules

**Modules** are pieces of code that we can borrow in Python
This includes things like functions

> For example, in `random` we use the `.choice()` function to choose something randomly from [[Lists]]

These pieces of code are not automatically included, so we need to `import` them into our code explicitly

# `import`
The `import` keyword loads the module into our Python file
**`import` should be at the top of our file under the header