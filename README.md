# Cache-Simulator
This is a Cache simulator developer as a Course project under **ES215: Computer Organisation and Organisation**. It demonstrates some of the different replacement, and mapping policies that the actual CPUs implement. The trace file used in the project is project has its reference [here](https://occs.oberlin.edu/~ctaylor/classes/210SP13/cache.html)

## Input
- `CacheSize` (in bytes) input the power of 2.
- `BlockSize` (in byter) in power of two.
- `Associativity` in multiple of two.
- `Policies` currently `LRU` and `FIFO` is supported by this simulator. Future scope of the project can be to make it compatible with other policies as well.

## Output
- `CacheSize`, `BlockSize`, `Associativity`, `Replacement Policy`
- `Access Data`: `Read` and `Write` Access
- `Compulsory misses`,`Conflict misses`, `Capacity missed`, `Read misses`, `Write misses`.
- `Dirty Blocks evicted`

## Simulation
- To run this project in the local environment, you must have python and necessary libraries installed.
- Use: `python3 main.py` to run the file in local environment after cloning the github repository.
- Output file named as `output.txt` will be created.

## Note
- The project is now also hosted using Flask.
