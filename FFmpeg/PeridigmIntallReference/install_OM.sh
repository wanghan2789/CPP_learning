cd ..
cd openmpi
mkdir build && cd build
../configure --prefix=/opt/openmpi-2.0.2
make –j 4
make install
