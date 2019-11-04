## Stage_01/main/大O记号
大O记号是用于衡量算法优劣的科学记号。
T(n) = O( f(n) ) 存在c>0，当n大于2后，有T(n) < c*f(n)，以此我们可以缩减一个相对复杂的公式，将公式转换成c*f(n)的简写方式，其诀窍是视2为n(所以可将4看成n的平方，6看成n的立方(6接近8，当成8))
![图1-1加载失败](http://a3.qpic.cn/psb?/V123pazn0FKOtx/iHywKwrtwwvT75c3dk9yj4*cFVuXVOYfKztK0.ntLIk!/m/dL4AAAAAAAAAnull&bo=WgN3AAAAAAARBx4!&rf=photolist&t=5 "图1-1")

* 与T(n)相比，f(n)更为简洁，但仍然反应前者的增长趋势。
* 常系数可以忽略： O( f(n) ) = O( c * f(n) )
* 低次项可以向上合并或忽略。
![图1-2加载失败](http://a3.qpic.cn/psb?/V123pazn0FKOtx/zJXm5qmXWKK*6UdOJiLLuIOcTp9Bz4IL3F2aLcI7W*I!/m/dL4AAAAAAAAAnull&bo=VQPHAAAAAAARB6E!&rf=photolist&t=5 "图1-2")
