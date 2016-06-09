# Basic PyCharm Debugging

This print from 0 what we want 1.

Set a breakpoint at the print.
 
```python
x = 3
y = "hi"

for i in range(10):
    print i

print "done"
```

Then look at the variables x, y, i. 

Show them the output.

Now set a breakpoint at print. it is clear that i is 0.

single step to show them the output coming out in the variables changing. Then "continue" to see it finish.

can change range to `range(1,11)` to get 1..10.