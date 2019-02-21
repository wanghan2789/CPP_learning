export CC=/opt/openmpi-2.0.2/bin/mpicc
export CXX=/opt/openmpi-2.0.2/bin/mpicxx
export CF=/opt/openmpi-2.0.2/bin/mpif90
export FC=/opt/openmpi-2.0.2/bin/mpif90
export F77=/opt/openmpi-2.0.2/bin/mpif77
export LIBRARY_PATH=/opt/openmpi-2.0.2/lib/:${LIBRARY_PATH}
export PATH=/opt/openmpi-2.0.2/bin/:$PATH
cd ..
cd hdf5
mkdir build && cd build
../configure --prefix=/opt/hdf5-1.8.17/ --enable-parallel
make -j 4
make test
make install
