__author__ = 'qgw'
##   https://www.cnblogs.com/alex3714/articles/5188179.html


'''
面向对象介绍：
世界万物，皆可分类
世界万物，皆为对象

        # 只要是对象， 就肯定属于某种品类
        # 只要是对象，就肯定有属性
        

    Class类
        一个类即是对一类拥有相同属性的对象的抽象、蓝图、原型。
                
    Object对象
        一个对象即是一个类的实例化后实例，一个类必须经过实例化后方可在程序中调用，
        一个类可以实例化多个对象，每个对象亦可以有不同的属性，
        就像人类是指所有人，每个人是指具体的对象，人与人之前有共性，亦有不同

特性：        
    Encapsulation 封装
        在类中对数据的赋值、内部调用对外部用户是透明的，这使类变成了一个胶囊或容器，里面包含着类的数据和方法
        封装，也就是把客观事物封装成抽象的类，并且类可以把自己的数据和方法只让可信的类或者对象操作，对不可信的进行信息隐藏。
        
    Inheritance   继承
        一个类可以派生出子类，在这个父类里定义的属性、方法自动被子类继承
        
        
    Polymorphism  多态
        多态是面向对象的重要特性,简单点说:“一个接口，多种实现”，
        指一个基类中派生出了不同的子类，且每个子类在继承了同样的方法名的同时又对父类的方法做了不同的实现，
        这就是同一种事物表现出的多种形态。
           
        编程其实就是一个将具体世界进行抽象化的过程，多态就是抽象化的一种体现，把一系列具体事物的共同点抽象出来, 
        再通过这个抽象的事物, 与不同的具体事物进行对话。 
        对不同类的对象发出相同的消息将会有不同的行为。

        多态允许将子类的对象当作父类的对象使用，某父类型的引用指向其子类型的对象,
        调用的方法是该子类型的方法。这里引用和调用方法的代码编译前就已经决定了,
        而引用所指向的对象可以在运行期间动态绑定。
               

类变量的用途？ 大家共用的属性   节省开销 省内存
  
  
析构函数：在实例释放、销毁的时候执行，通常用于做一些收尾工作，如关闭一些数据库连接，关闭打开的临时文件

私有方法、私有属性： 在属性或者方法前添加“__”;
                 只能在内部调用，外部不能处理




继承

多继承的区别查询：  
        class A
        class B(A)
        class C(A)
        class D(B,C)
        obj = D()
        
    广度优先（python3都是广度优先） 
        B-->C-->A   
    深度优先
        B-->A-->C
py2 经典类是按深度优先来继承的，新式类是按广度优先来继承的
py3 经典类和新式类都是统一按广度优先来继承的
 
多态
一种接口，多种实现
作用：实现


'''

