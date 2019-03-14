# 音视频基础

# 1.直播架构基础

* 实时互动直播，400ms之内
* CDN音视频流的转发
* 信令服务器创建 推送rtmp流 将用户加入 用户拉取流观看节目
* 实时互动结构
  * 自有网络 UDP
  * TCP 发送 确认 超时 重发 无法达到实时
  * 多个节点 服务器可靠 健壮 B2B
  * 控制中心
  * 媒体服务器可以将数据转换 -> CDN RTMP ->用户
* CDN网络
  * CDN为了解决用户访问资源慢
    * 链路过长
    * 运营商阻塞
    * 边缘节点：用户从边缘节点上获取数据
    * 主干节点，用于缓存，减轻源网站的压力
    * 源站：内容提供方将内容放在源站上
* ffmpeg 
* ffplay 播放器
* flashplayer 能够对rtmp流进行解析
* 搭建一个服务器:
  * Linux
  * Nginx(学)
  * RTMP启动Nginx   nginx-with rtmp模块
    * 配置ngnix文件
    * ngnix -s reload
    * netstat -an |grep portid
  * ffmpeg -re -i 推流/拉流

# 2.音频

* 音调 音频
* 音量 振动幅度
* 音色 材质有关 实质是谐波不同
* 20Hz-20kHz
* 音频的量化
  * 模拟数据 - 采样 - 量化 - 编码 -数字信号
  * 模拟数据经过均匀剪裁，保留峰值，然后转码为2进制
  * 采样大小: 量化y轴的高度 16bit 2**16  0~65535
  * 采样率 8k 16k 32k 44.1k
  * 码率 `采样率*采样大小*声道数`
* 压缩
  * 消除冗余，有损压缩
    * 20~20k以外的可以删除
    * 频域遮蔽，时域遮蔽
      * 相似频率之间相互掩盖
      * 同样时间内高声会遮蔽低声
  * 哈夫曼无损
* 编解码器  OPUS(实时互动)  AAC(直播)  Vorbis  Speex(回音消除，降噪)  iLBC  AMR  G.711(固话结合)722
* OPUS > AAC >Vorbis
* AAC
  * 支持RTMP
  * 应用范围广
  * 高保真
  * 取代MP3
  * LC 128k   +(SBR低音频率低点，高音频率高点)HE V1 64k   +(SBR+PS.双声道，一个完整，一个存差异数据.)HE V2  32k
  * ADIF 采样率 采样大小等基本信息存在于头
  * ADTS 在每一个帧前面加一个同步字 可以从任何位置进行解码
  * libfdk_AAC > ffmpeg AAC >libfaac >libvo_aac

# 3.视频

* I 帧 关键帧 帧内压缩技术 (第一帧为关键帧)
* P 帧 向前参考帧 后一帧与前一帧相关 帧间压缩
* B 帧 双向参考，帧间压缩 
* GOF group of frame 一组帧
* SPS 序列参数集 存放帧数，参考书目，尺寸等
* PPS 图像参数集等
* 视频花屏卡顿 GOP中的P帧丢失就会发生错误
  * 丢失P帧，知道下一个I到来前，什么都不会刷新
* x264/x265 x265占用的cpu略高！
* openH264 性能低 支持SVC 视频分层传输，根据网络带宽传输
* vp8/vp9
* H264编码原理
  * 帧内预测压缩，解决空域数据冗余
  * 帧间预测压缩，解决时域数据冗余
  * 整数离散余弦变换 DCT 傅里叶变换
  * CABAC无损压缩 哈弗曼编码
* 宏块划分与分组
  * H264宏块 例如8*8pixel
  * 子块 
  * 帧分组  物体在序列帧之间相对变化比较小
* 视频压缩
  * 组内宏块查找
    * 逐行扫描，找到类似的，放到一张图。生成运动矢量，最终得到矢量以及背景开头等存储，帧间压缩
    * 帧内压缩
      * 每个宏块选择不同的压缩样式
      * 计算预测值和源图的差值，残差值--这时我们只要预测图和残差值就可以了。
    * DCT压缩 
    * 只有角上有数据
    * VLC类似哈弗曼编码
    * CABAC上下文适应
* H264结构图
  * 序列帧 图像 片 宏块 子块
* H264编码层
  * NAL 网络层
  * VCL视频编码层 原始数据的压缩
* SODB 原始数据比特流
* RBSP 对SODB进行补位对齐 8位对齐
* EBSP 起始位的增加 防止与头的冲突
* NALU EBSP加了一个头
* NAL 单元 NALU头+一个切片
  * NAL header
    * F 必须是0
    * NRI 指示性没啥用
    * type 类型 5代表IDR图像片，关键帧一部分  7序列参数集 8图像参数集 28 29分片的单元
    * RTP包包含单一或者多个NALU
* 图像除了RGB还有YUV
  * 24位 3*8 = 24
  * 电视系统 YUV420  YUV422  YUV444  节省存储空间
  * 420不是只有Y cb 而是每次扫描只有一种色度分量
  * **ffmpeg webrtc OpenGL**

# FFmpegの基本使用

# 0.FFmpeg处理流程

```C++
     demuxer            decoder
输入   -->    编码数据包   -->        ||
                                解码后的数据帧
                                     ||
输出  <--     编码数据包  <--
     muxer              encoder
    
```

# 1.编译安装遇到的问题

## QT里面g++编译C代码

```c++
extern "C"{
#include<libavcodec/avcodec.h>
#include<libavformat/avformat.h>
}
```

## 编译的时候前后顺序问题

```g++
#QT .pro的设置的时候，你需要保证你的库的顺序
unix{
INCLUDEPATH += /home/malfoy/FFmpeg/libFFmpeg/include
LIBS += -L /home/malfoy/FFmpeg/libFFmpeg/lib
LIBS += -lavformat \
        -lavcodec \
        -lavutil \
        -lswscale \
        -lavdevice \
        -lavfilter
LIBS += -lz \
        -lpthread \
        -lswresample \
        -lm
}
```

# 2.常用命令

## 查询

| **参数**     | **说明**                           |
| :----------- | ---------------------------------- |
| -version     | 显示版本。                         |
| -formats     | 显示可用的格式（包括设备）。       |
| -demuxers    | 显示可用的demuxers。               |
| -muxers      | 显示可用的muxers。                 |
| -devices     | 显示可用的设备。                   |
| -codecs      | 显示libavcodec已知的所有编解码器。 |
| -decoders    | 显示可用的解码器。                 |
| -encoders    | 显示所有可用的编码器。             |
| -bsfs        | 显示可用的比特流filter。           |
| -protocols   | 显示可用的协议。                   |
| -filters     | 显示可用的libavfilter过滤器。      |
| -pix_fmts    | 显示可用的像素格式。               |
| -sample_fmts | 显示可用的采样格式。               |
| -layouts     | 显示channel名称和标准channel布局。 |
| -colors      | 显示识别的颜色名称。               |

## 录制

* ffmpeg -f avfoundation -i 1 -r 30 out.yuv
  * -f 使用avfoundation库采集数据
  * -i 从哪里采集数据 0摄像头 1屏幕
  * -r 帧率
  * 注意 avfoudation用于mac对其他的环境你需要重新选择参数
* ffmpeg -f avfoundation -i :1 out.wav
  * 冒号后面表示音频
* ffmpeg  -f avfoundation -i 1:0  -r 29.97 -c:v libx264 -crf 0 -c:a libfdk_aac -profile:a aac_he_v2 -b:a 32k  out.flv
  * 包含声音
* ffplay -s 2560*1600 -pix_fmt uyvy42 out.yuv

## 分解/复用

* ffmpeg -i out.mp4 -vcoder copy -acodec copy out.flv
  * 格式转换
* ffmpeg -i out.mp4 -acodec copy -vn out.aac
  * 抽取音频
* ffmpeg -i input.mp4 -vcodec copy -an out.h264
  * 抽取视频

## 处理原始数据

* ffmpeg -i input.mp4 -an -c:v rawvideo -pixel_format yuv420p out.yuv
  * -an a no 没有音频
  * rawvideo 原始格式
  * ffmplay -pixel_format 638*358 out.yuv
* ffmpeg -i out.mp4 -vn -ar 44100 -ac 2 -f s16le out.pcm
  * ar 音频采样率
  * ac 声道数量
  * ffplay -ar 44100 -ac 2 -f s16le -i out.pcm

## 剪裁与合并

* ffmpeg -i in.mp4 -ss 00:00:00 -t 10 out.ts
  - -ss就是什么时候开始裁剪
  - -t给多少秒
* ffmpeg -f concat -i inputs.txt out.flv
  * txt是一个文件名列表 要求每行格式 'file 文件名'
  * file 1.mp4
* ​

## 图片视频互转

## 直播相关

* 推流
  * ffmpeg -re -i out.mp4 -c copy -f flv rtmp://server/live/streamName
    * 流推出到rtmp服务器
    * -re减慢帧率，保持同步
    * copy不用重设音视频参数
* 拉流
  * ffmpeg -i rtmp://server/live/streamName -c copy dump.flv
* B站推拉流

## 滤镜命令

* filter滤镜 
* 解码并加滤镜->对相应处理后的进行编码
* ffmpeg -i in.mov -vf crop=in_w-200:in_h-200 -c:v libx264 -c:a copy out.mp4
  * 输入的宽度w-200 高度h-200
  * 裁剪

# 3.回顾基础

## 1.Vim回顾

* 命令模式  i/a 切换  编辑模式
* vim filename 创建命令
*  :w 写
*  :q 退出
*  :wq 写之后退出
* 拷贝
  * yy 拷贝一行
  * yw 拷贝一个词
* 粘贴
  * p
* 删除
  * dd 删除一行
  * dw 删除一个词
* 光标移动
  * h左 j下 k上 l右
  * gg 跳文件头
  * G 文件尾部
  * ^ 移动到行首
  * $ 行尾
  * 行内按单词移动 一个词 w/ 两个词 2w/ 向后 b/ 2b/
* 查找
  *   /关键词     按n查找下一个  N查找前面的一个
  * 替换  :%s/查找的单词/替换的单词/gc
    * a 替换所有的
    * 替换特定的行数    :21,23%s/查找的单词/替换的单词/gc
* 替换
* set number    显示行号
* 多窗口
  * split横向切割窗口    vsplit纵向切割
  * 窗口跳转  crtl ww   crtl w[hjkl]
  * 缩放窗口 crtl w [- =]
  * close 关闭当前窗口  

## 2.C回顾

* 指针是内存地址   void*  char*
* %p 打印地址
* `a = (int*)malloc(sizeof(int));`
* 数组本身就是个地址，不需要上级地址
* enum枚举类型   第一个有默认值  则后面每个比上一个多1 枚举用 , 隔开
* 函数指针
  *  返回值类型 (*指针变量名) ([参数列表])
  * int (*f)(int x);
  * 指针名没有改，但是我可以通过一个函数做很多行为
* 编译器
  * gcc -g -O2 -o test test.c -I -L -l
  * -g: 输出调试信息
  * -O2: O1不优化
  * -o: 输出文件
  * test 输出文件文件名
  * test.c 源代码
  * -I: 指定头文件
  * -L: 指定库文件的位置
  * -l: 指定是用什么库
    * 请按顺序书写
  * gcc -g -c filename.c    生成一个.o库
  * libtool -static -o libmylib.a  必须以lib开头！但是你配置 -l的时候必须去掉lib 即 gcc ... -lmylib
* 调试器 GDB lldb
  * 常用命令
    * 设置断点  b
    * 运行程序  r
    * 单步执行  n
    * 跳入函数  s
    * 跳出函数  finish
    * 打印内容  p  变量名
    * 查看断点  break list