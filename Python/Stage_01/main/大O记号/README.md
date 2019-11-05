## Stage_01/main/大O记号
大O记号是用于衡量算法优劣的科学记号。
T(n) = O( f(n) ) 存在c>0，当n大于2后，有T(n) < c*f(n)，以此我们可以缩减一个相对复杂的公式，将公式转换成c*f(n)的简写方式，其诀窍是视2为n(所以可将4看成n的平方，6看成n的立方(6接近8，当成8))
![图1-1加载失败](http://a3.qpic.cn/psb?/V123pazn0FKOtx/iHywKwrtwwvT75c3dk9yj4*cFVuXVOYfKztK0.ntLIk!/m/dL4AAAAAAAAAnull&bo=WgN3AAAAAAARBx4!&rf=photolist&t=5 "图1-1")

* 与T(n)相比，f(n)更为简洁，但仍然反应前者的增长趋势。
* 常系数可以忽略： O( f(n) ) = O( c * f(n) )
* 低次项可以向上合并或忽略。
![图1-2加载失败](http://m.qpic.cn/psb?/V123pazn0FKOtx/zJXm5qmXWKK*6UdOJiLLuIOcTp9Bz4IL3F2aLcI7W*I!/b/dL4AAAAAAAAA&bo=VQPHAAAAAAARB6E!&rf=viewer_4&t=5 "图1-2")

###### 所以说，O( f(n) )是对T(n)的一种悲观预测。
### 复杂度分析
#### 常数复杂度 O(1)
若算法中语句执行次数为一个常数，则时间复杂度为O(1)，形如 2 = 2013 = 2013x2013 = O(1) , 甚至2013^2013 = O(1)。这类算法的效率最高
#### 对数复杂度O(logn)
这类算法也非常有效，复杂度无限接近于常数
* 对数 lnn lgn 等等...
* 常数底数无所谓，因为
![图1-3加载失败](http://a3.qpic.cn/psb?/V123pazn0FKOtx/I8fwnhG*5nywo1Qyf7l2HufFe0tGXI8YhHsUpfLEs7Q!/m/dLYAAAAAAAAAnull&bo=xQJTAAAAAAARB6Q!&rf=photolist&t=5 "图1-3")
* 常数幂数无所谓，因为
![图1-4加载失败](http://a3.qpic.cn/psb?/V123pazn0FKOtx/J7cSjXG8ugI5AUYZ5ndOGQHqPkSmd3UNtIGGb3QMUp4!/m/dLYAAAAAAAAAnull&bo=BQI4AAAAAAARBw8!&rf=photolist&t=5 "图1-4")
* 对数多项式可以忽略低次项，从而达到缩减的目的
![图1-5加载失败](http://a4.qpic.cn/psb?/V123pazn0FKOtx/bzQT6pyJXQVFXnD0ngYnmCptBeeIREBrM.WOyJTAvt4!/m/dL8AAAAAAAAAnull&bo=cwI4AAAAAAARB3k!&rf=photolist&t=5 "图1-5")
