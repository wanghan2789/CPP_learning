    #!/bin/bash
    cd ffmpeg
    NDK=/home/lsc/newDisk2/android-sdk/ndk-bundle
    SYSROOT=$NDK/platforms/android-19/arch-arm/
    TOOLCHAIN=$NDK/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64

    function build_one
    {
    ./configure \
        --prefix=$PREFIX \
        --enable-shared \
        --disable-static \
        --disable-doc \
        --disable-ffserver \
        --enable-cross-compile \
        --cross-prefix=$TOOLCHAIN/bin/arm-linux-androideabi- \
        --target-os=linux \
        --arch=arm \
        --sysroot=$SYSROOT \
        --extra-cflags="-Os -fpic $ADDI_CFLAGS" \
        --extra-ldflags="$ADDI_LDFLAGS" \
        $ADDITIONAL_CONFIGURE_FLAG
    }
    CPU=arm
    PREFIX=$(pwd)/android/$CPU
    ADDI_CFLAGS="-marm"
    build_one
    make 
    make install

