# Using C from Python: How to create a ctypes wrapper

See short tutorial originally from [here](https://pgi-jcns.fz-juelich.de/portal/pages/using-c-from-python.html).

Here I implement the a simple funtion to compute the mutual information between two binary time series in C, and import it to Python via a shared object (.so).

## How to run

1. Create the shared object file: cc -fPIC -shared -o libmi.so mi.c -lm
2. Open the jupyter notebook to run the code.
