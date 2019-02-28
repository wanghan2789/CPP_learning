#!/bin/sh


#FFmpeg source -->git://source.ffmpeg.org/ffmpeg.git
#Build armv7 armv7s arm64  

#Download FFmpeg source
#git clone git://source.ffmpeg.org/ffmpeg.git

cd ffmpeg

#Output DIR
DEST=output

./configure \
--prefix=/home/malfoy/book/output \
--disable-ffmpeg \
--disable-ffplay \
--disable-ffprobe \
--disable-ffserver \
--disable-iconv \
--disable-bzlib \
--enable-avresample \
--enable-avresample  \
--enable-pic	\
--disable-doc	\
--disable-decoders \
--enable-decoder=h264 \
--disable-encoders \
--disable-demuxers \
--enable-demuxer=avi \
--disable-muxers \
--enable-muxer=avi \
--disable-filters
		
make -j4 && make install && make clean

echo "Installed:$DEST/$ARCH"

