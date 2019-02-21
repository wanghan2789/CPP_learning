export CC=/opt/openmpi-2.0.2/bin/mpicc
export CXX=/opt/openmpi-2.0.2/bin/mpicxx
export CF=/opt/openmpi-2.0.2/bin/mpif90
export FC=/opt/openmpi-2.0.2/bin/mpif90
export F77=/opt/openmpi-2.0.2/bin/mpif77
export LIBRARY_PATH=/opt/openmpi-2.0.2/lib/:${LIBRARY_PATH}
export PATH=/opt/openmpi-2.0.2/bin/:$PATH
cd ..
cd peridigm
mkdir build && cd build
cmake \
-D CMAKE_BUILD_TYPE:STRING=Release \
-D CMAKE_INSTALL_PREFIX:PATH=/opt/Peridigm/ \
-D Boost_NO_SYSTEM_PATHS=ON \
-D Trilinos_DIR:PATH=/opt/trilinos-12.8.1/lib/cmake/Trilinos/ \
-D CMAKE_CXX_COMPILER=/opt/openmpi-2.0.2/bin/mpicxx \
-D CMAKE_C_COMPILER=/opt/openmpi-2.0.2/bin/mpicc \
-D BOOST_ROOT=/opt/boost-1.58/ \
-D CMAKE_CXX_FLAGS:STRING="-O2 -Wall -std=c++11 -pedantic -Wno-long-long -ftrapv -Wno-deprecated " \
..
ulimit -n 140000
make -j 4
make install
