

# Running
Please have $integrals.py, decay.py,$ and $inertia2.py$ under the same directory. $integrals.py$ has all the helper methods that needed to be imported into the other two (already done). While under the directory with these three files, please run in terminal: (Additionally, please have a ./figures directory in under the same level with the above 3 to have figures saved.
)
```
python $decay.py
```
This will generate the plot for compound decay, with everything overlapped.
```
python $inertia2.py
```
This wil generate error plot for inertia calculated with different integrating mesh sizes, from 10 to 100 in each dimension. In the meantime, terminal will also display the value, time of each iteration. In the end a plot of error and a plot of run time comparison is generated.



