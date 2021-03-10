# Path4GMNS

Path4GMNS is an open-source, lightweight, and fast Python path engine for networks encoded in GMNS. Besides the static and time-dependent shortest path calculations and retrievals for simple network analyses, its main functionality is to provide an efficient and flexible framework for column(path)-based modeling/application frameworks in transportations (e.g., activity-based demand modeling).

The column generation scheme is an equivalent single-thread implementation as its DTALite[1] parallel counterpart. Support for the multi-demand-period and multi-agent-type implementation in Path4GMNS is reserved in the current release, and will be implemented soon. Note that the results (i.e., column pool and trajectory for an agent) from Path4GMNS and DTALite are comparable but likely not identical as the shortest paths are usually not unique and subjected to implementations. This phenomenon should be gone and the link performances should be consistent if the iterations on both assignment and column generation are large enough. You can always compare the results (i.e., link_performance.csv) from Path4GMNS with DTALite given the same network.

The whole package is implemented towards high efficiency. The core shortest-path engine is implemented in C++ (deque implementation of the modified label correcting algorithm) along with the equivalent Python implementations for demonstrations. To achieve the maximum efficiency, we use a fixed-length array as the deque (rather than the STL deque) and combine the scan eligible list (represented as deque) with the node presence statutes. With the minimum and fast argument interfacing between the C++ path engine and the corresponding Python modules, its running time is comparable to the pure C++-based DTALite. If you have an extremely large network and/or have requirement on CPU time, please use DTALite[1].

An easy installation process by low dependency is one of our major design goals. The Python modules in Path4GMNS do not require any third-party libraries/packages but a handful of components from the Python standard library (e.g., csv, cytpes, and so on). Furthermore, precompiled shared libraries are embedded to make this package portable across three major desktop environments (i.e., Windows, macOS, and Linux). The C++ path engine itself is implemented using C++11 without any dependency. Users can easily build the path engine from the source code towards the target system if it is not listed as one of the three.

## References
1. DTALite. Available: https://github.com/asu-trans-ai-lab/DTALite