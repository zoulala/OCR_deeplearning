# 验证码识别-CNN

用Tesseract OCR、OpenCV等等其它方法都需把验证码分割为单个字符，然后识别单个字符。分割验证码可是人的强项，如果字符之间相互重叠，那机器就不容易分割了。
本文实现的方法不需要分割验证码，而是把验证码做为一个整体进行识别。ref:http://blog.topspeedsnail.com/archives/10858

### CNN流程图

![流程图](https://github.com/zoulala/OCR_deeplearning/blob/master/CNN/ocr_cnn.png)

图中k为验证码设定长度

### 训练

> python train.py

```
Restored from: models\m_cnn\model-17400
start to training...
step: 17420/20000...  loss: 0.0173... 
step: 17440/20000...  loss: 0.0168... 
step: 17460/20000...  loss: 0.0200... 
step: 17480/20000...  loss: 0.0137... 
step: 17500/20000...  loss: 0.0187... 
step: 17500/20000...  acc: 0.9125...  best: 0.9450... 
step: 17520/20000...  loss: 0.0174... 
step: 17540/20000...  loss: 0.0165... 
step: 17560/20000...  loss: 0.0189... 
step: 17580/20000...  loss: 0.0175... 
step: 17600/20000...  loss: 0.0179... 
step: 17600/20000...  acc: 0.9275...  best: 0.9450... 
```
目前我的验证样本精度是0.94，应该可以通过调节参数获得更好的效果。


### 测试
> python test.py

![测试1](https://github.com/zoulala/OCR_deeplearning/blob/master/CNN/test1.png)
```
start to test...
test text: wOll
predict text: w0ll
```
预测错误：O预测为0

![测试2](https://github.com/zoulala/OCR_deeplearning/blob/master/CNN/test2.png)
```
start to test...
test text: 1Mum
predict text: 1Mum
```
预测正确



### 训练好的模型

链接：https://pan.baidu.com/s/16xe2Hz3e9W5B5Iz9SyPIFw 
提取码：65zr 

下载，将models文件夹放到CNN目录下
