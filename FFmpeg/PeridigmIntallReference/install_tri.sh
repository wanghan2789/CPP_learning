export CC=/opt/openmpi-2.0.2/bin/mpicc
export CXX=/opt/openmpi-2.0.2/bin/mpicxx
export CF=/opt/openmpi-2.0.2/bin/mpif90
export FC=/opt/openmpi-2.0.2/bin/mpif90
export F77=/opt/openmpi-2.0.2/bin/mpif77
export LIBRARY_PATH=/opt/openmpi-2.0.2/lib/:${LIBRARY_PATH}
export PATH=/opt/openmpi-2.0.2/bin/:$PATH
cd ..
cd trilinos
mkdir build && cd build
cmake \
-D CMAKE_INSTALL_PREFIX:PATH=/opt/trilinos-12.8.1 \
-D CMAKE_CXX_FLAGS:STRING="-O2 -std=c++11 -pedantic -ftrapv -Wall -Wno-long-long" \
-D CMAKE_BUILD_TYPE:STRING=RELEASE \
-D Boost_NO_SYSTEM_PATHS=ON \
-D TPL_ENABLE_MPI=ON \
-D CMAKE_CXX_COMPILER=/opt/openmpi-2.0.2/bin/mpicxx \-D CMAKE_C_COMPILER=/opt/openmpi-2.0.2/bin/mpicc \
-D Trilinos_WARNINGS_AS_ERRORS_FLAGS:STRING="" \
-D Trilinos_ENABLE_ALL_PACKAGES:BOOL=OFF \
-D Trilinos_ENABLE_Teuchos:BOOL=ON \
-D Trilinos_ENABLE_Shards:BOOL=ON \
-D Trilinos_ENABLE_Sacado:BOOL=ON \
-D Trilinos_ENABLE_Epetra:BOOL=ON \
-D Trilinos_ENABLE_EpetraExt:BOOL=ON \
-D Trilinos_ENABLE_Ifpack:BOOL=ON \
-D Trilinos_ENABLE_AztecOO:BOOL=ON \
-D Trilinos_ENABLE_Amesos:BOOL=ON \
-D Trilinos_ENABLE_Anasazi:BOOL=ON \
-D Trilinos_ENABLE_Belos:BOOL=ON \
-D Trilinos_ENABLE_ML:BOOL=ON \
-D Trilinos_ENABLE_Phalanx:BOOL=ON \
-D Trilinos_ENABLE_Intrepid:BOOL=ON \
-D Trilinos_ENABLE_NOX:BOOL=ON \
-D Trilinos_ENABLE_Stratimikos:BOOL=ON \
-D Trilinos_ENABLE_Thyra:BOOL=ON \
-D Trilinos_ENABLE_Rythmos:BOOL=ON \
-D Trilinos_ENABLE_MOOCHO:BOOL=ON \
-D Trilinos_ENABLE_TriKota:BOOL=OFF \
-D Trilinos_ENABLE_Stokhos:BOOL=ON \
-D Trilinos_ENABLE_Zoltan:BOOL=ON \
-D Trilinos_ENABLE_Piro:BOOL=ON \
-D Trilinos_ENABLE_Teko:BOOL=ON \
-D Trilinos_ENABLE_SEACASIoss:BOOL=ON \
-D Trilinos_ENABLE_SEACAS:BOOL=ON \
-D Trilinos_ENABLE_SEACASBlot:BOOL=ON \
-D Trilinos_ENABLE_Pamgen:BOOL=ON \
-D Trilinos_ENABLE_EXAMPLES:BOOL=OFF \
-D Trilinos_ENABLE_TESTS:BOOL=ON \
-D TPL_ENABLE_Matio=OFF \
-D TPL_ENABLE_HDF5:BOOL=ON \
-D HDF5_INCLUDE_DIRS:PATH="/opt/hdf5-1.8.17/include" \
-D HDF5_LIBRARY_DIRS:PATH="/opt/hdf5-1.8.17/lib" \
-D TPL_ENABLE_Netcdf:BOOL=ON \
-D Netcdf_INCLUDE_DIRS:PATH="/opt/netcdf-4.4.1/include" \
-D Netcdf_LIBRARY_DIRS:PATH="/opt/netcdf-4.4.1/lib" \
-D TPL_ENABLE_MPI:BOOL=ON \
-D TPL_ENABLE_BLAS:BOOL=ON \
-D TPL_ENABLE_LAPACK:BOOL=ON \
-D TPL_ENABLE_Boost:BOOL=ON \
-D Boost_INCLUDE_DIRS:PATH="/opt/boost-1.58/include" \-D Boost_LIBRARY_DIRS:PATH="/opt/boost-1.58/lib" \
-D CMAKE_VERBOSE_MAKEFILE:BOOL=OFF \
-D Trilinos_VERBOSE_CONFIGURE:BOOL=OFF \
..
make -j 4
make install
