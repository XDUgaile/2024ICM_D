# 2024美赛D题

### 2024美赛问题D：五大湖水问题

本次是我的最后一次美赛了，和上一次的从众选择C题不一样，我们选择了比较难的题目。因为D题给出了一些数据，而B题没有，为了避免查找数据耽误时间，我们本次选择的是D题。下面给出部分题目翻译：

国际联合委员会（IJC）请求贵公司（国际网络控制建模公司- ICM）提供支持，以协助对直接影响五大湖水流网络水位的控制机制（附录中所示的两座大坝-补偿工程和摩西-桑德斯大坝）进行管理和建模。您的ICM主管已经让您的团队在开发模型和实施模型的管理计划方面处于领先地位。您的主管指出，有几个注意事项可能有助于实现这一目标，首先是构建五大湖的网络模型，并连接从苏必利尔湖上级到大西洋的河流。你的主管提到的其他一些可选的考虑因素或问题是：

确定五个五大湖在一年中任何时候的最佳水位，同时考虑到各利益攸关方的愿望（每个利益攸关方的成本和收益可能不同）。

·根据五个湖泊的流入和流出数据建立算法，以保持五个湖泊的最佳水位。

·了解控制算法对两个控制坝流出量的敏感性。根据2017年的数据，您的新控制措施是否会为各利益相关方带来令人满意或优于当年实际记录的水位？

·您的算法对环境条件的变化有多敏感（例如，降水、冬季积雪、冰塞）？

·集中你的广泛分析，只有利益相关者和影响安大略湖的因素，因为有更多的关注，为这个湖的水位管理最近。

子问题的一些潜在因素是：1）安大略湖的当前水位和一年中的时间。2)渥太华河的流量和一年中的时间。3)积雪和预测渥太华河的流量。4)水位，流速，以及摩西-桑德斯大坝下游圣劳伦斯河上的冰量。5)沿着渥太华河的水库水位。6)其他四个五大湖的水位（最终输入到安大略）;以及7）水温、蒸发率和天气数据。

思路：

一、考虑到最佳水位，则需要从利益相关方入手，通过查找相关文献，我们采用下面的解决方案。

1.**不同利益相关方归类**

2.建立**多目标优化**算法确定最佳水位。

二、本题本题是建立一个流量控制算法，但是需要考虑到每个湖的储水量，和河流的出水量。但是我们这样分析了一通，发现可能会导致任务量过大，经过查找文献，我们发现了一个idea，即以河流流量代替湖泊流量，并找到了对应的公式，这样一来，就得到了我们期望的理想流量值，后面的调节就是和这个值进行比较。对于实际水量，我们通过模糊预测控制，建立五大湖耦合模型，得到预计实际值。所谓调节，即多了就多排水，少了就少排，尽可能维持在最佳水位附近，以满足利益相关者。

1.**以河流流量代替湖泊流量**

2.湖泊水位与流量的转换公式，得到理想流量

3.**模糊预测控制**

（1）基于水量平衡预测

（2）定义目标函数，即逼近理想流量

（3）**滚动优化**

（4）**反馈控制**：引入e(k)，降水+冰盖

（5）五个湖泊相互耦合，得到各阶段流量值

三、本题经过我们的分析，先找到两个控制坝（分别在上下游），仅分析其流出量敏感性（其余的放在第四问），再和2017年的数据进行比较，得出我们方案较优结论，这个结果是通过量化得分得出的。其中量化涉及到了**评分曲线**，各利益相关方的评价曲线权值由查阅资料得到。  
1.灵敏度分析  
2.为各利益方单独构建评分曲线  
3.比较最优水位与2017年得分  

四、本题是针对环境条件的变化，进行模型敏感度分析，分为以下两部分：  
1.**蒙特卡洛**的意义  
通过生成大量可能的情景，可以用来评估不确定性因素在广泛变化下对最高水位的影响  
2.Frank-Copula  
联合分布+条件概率分析影响性  

五、本题是仅针对安大略湖，由于前四问以及分析得很彻底了，并且论文写的很顺利，留给第五问的地方不多了，我们将其分为以下三点，进行较为简单的分析，具体如下：  
1.多加渥太华河，蒙特利尔港  
2.单论与全面的最佳水位对比  
3.利益相关方分析

本次的比赛由于是在农历26结束，队友也都回家了，本次比赛我们三人在线上进行的，但是我们仍旧合作的非常愉快！沟通讨论也都很及时！一次别样的比赛经历，给我们最后一次美赛交上了一份完美的答卷。该好好过年喽！  

<p align="right" >  ——写于2024.2.8</p>
