#!/bin/sh

#FFmpeg source -->git://source.ffmpeg.org/ffmpeg.git
#Build armv7 armv7s arm64  

#Download FFmpeg source
#git clone git://source.ffmpeg.org/ffmpeg.git

cd ffmpeg

./configure \
--prefix=/home/malfoy/book/ARCH \
--disable-ffmpeg \
--disable-ffplay \
--disable-ffprobe \
--disable-ffserver \
--disable-iconv \
--disable-bzlib \
--enable-avresample \
--disable-armv6	\
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
--disable-armv5te \
--disable-debug
make -j4 && make install && make clean

