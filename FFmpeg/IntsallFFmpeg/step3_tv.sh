#!/bin/sh

cd ffmpeg

./configure \
--prefix=/home/malfoy/book/tv \
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

make -j3 && make install && make clean
