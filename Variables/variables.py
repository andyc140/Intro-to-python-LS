first,last = ['Mary', 'Wonder']

forename = 'Clare'       # initialization (also called assignment)

forename = 'Clare'       # initialization (also called assignment)
# omitted code
forename = 'Victor'      # reassignment

PINING_FOR = 'fjords'         # initialization

left_side = 5
right_side = 32
total = left_side + right_side  # total = 37
print(total)                    # prints 37

def square(number):
    return number * number

forty_two_squared = square(42)
print(forty_two_squared)                # 1764

foo = 42            # foo is 42
foo = foo - 2       # foo is now 40
foo = foo * 3       # foo is now 120
foo = foo + 5       # foo is now 125
foo = foo // 25     # foo is now 5
foo = foo / 2       # foo is now 2.5
foo = foo**3        # foo is now 15.625
print(foo)          # prints 15.625

foo = 42            # foo is 42
foo -= 2            # foo is now 40
foo *= 3            # foo is now 120
foo += 5            # foo is now 125
foo //= 25          # foo is now 5
foo /= 2            # foo is now 2.5
foo **= 3           # foo is now 15.625
print(foo)          # prints 15.625

bar = 'xyz'          # bar is 'xyz'
bar += 'abc'         # bar is now 'xyzabc'
bar *= 2             # bar is now 'xyzabcxyzabc'
print(bar)           # prints xyzabcxyzabc

bar = [1, 2, 3]     # bar is [1, 2, 3]
bar += [4, 5]       # + with lists appends
                    # bar is now [1, 2, 3, 4, 5]
print(bar)          # prints [1, 2, 3, 4, 5]

bar = {1, 2, 3}     # bar is {1, 2, 3}
bar |= {2, 3, 4, 5} # | performs set union
                    # bar is now {1, 2, 3, 4, 5}
bar -= {2, 4}       # - performs set difference
                    # bar is now {1, 3, 5}
print(bar)          # prints {1, 3, 5}

num = 3               # assignment (initialization)
my_list = [1, 2, 3]   # assignment (initialization)
my_dict = {           # assignment (initialization)
    'a': 1,
    'b': 2,
}

num = 42              # Reassignment
my_list[1] = 42       # Reassignment of element,
                      # my_list is mutated!
my_dict['b'] = 3      # Reassignment of dict pair
                      # my_dict is mutated!

# You can still reassign the variables
my_list = [2, 3, 4]   # Reassignment
my_dict = { 'x': 0 }  # Reassignment

#for non-constant variables:
#index	Idiomatic	
#CatName	Non-idiomatic	Should not use uppercase letters
#lazy_dog	Idiomatic	
#quick_Fox	Non-idiomatic	Should not use uppercase letters
#1stCharacter	Illegal	Should not begin with a digit
#operand2	Idiomatic	
#BIG_NUMBER	Non-idiomatic	Should not use uppercase letters
#π	Non-idiomatic	π is not an ASCII character

#for a constant vairable:
#index	Non-idiomatic	Should not use lowercase letters
#CatName	Non-idiomatic	Should not use lowercase letters
#snake_case	Non-idiomatic	Should not use lowercase letters
##LAZY_DOG3	Idiomatic	
#1ST	Illegal	Should not begin with a digit
#operand2	Non-idiomatic	Should not use lowercase letters
#BIG_NUMBER	Idiomatic	
#Π	Non-idiomatic	Π is not an ASCII character

#for class names
##index	Non-idiomatic	Should not begin with a lowercase letter
#CatName	Idiomatic	
#Lazy_Dog	Non-idiomatic	Should not use underscores
#1ST	Illegal	Should not begin with a digit
#operand2	Non-idiomatic	Should not begin with a lowercase letter
#BigNumber3	Idiomatic	
#Πi	Non-idiomatic	Π is not an ASCII character



obj = 'ABcd'      # Reassignment
obj.upper()       # Neither
obj = obj.lower() # Reassignment
print(len(obj))   # Neither
obj = list(obj)   # Reassignment
obj.pop()         # Mutation
obj[2] = 'X'      # Mutation
obj.sort()        # Mutation
set(obj)          # Neither
obj = tuple(obj)  # Reassignment