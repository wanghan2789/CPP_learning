#!/bin/sh


#FFmpeg source -->git://source.ffmpeg.org/ffmpeg.git
#Build armv7 armv7s arm64  

#Download FFmpeg source
#git clone git://source.ffmpeg.org/ffmpeg.git

cd ffmpeg

./configure \
--prefix=./build \
--disable-ffmpeg \
--disable-ffplay \
--disable-ffprobe \
--disable-doc	\
--disable-yasm \
		
make -j4 && make install && make clean

echo "Installed:$DEST/$ARCH"

