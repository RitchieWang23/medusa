#!/usr/bin/env python
# coding:utf-8


"""
工厂方法模式(Factory Method Pattern)
    在工厂方法模式中，
    工厂父类负责定义创建产品对象的公共接口，
    工厂子类则负责生成具体的产品对象，
    这样做的目的是将产品类的实例化操作延迟到工厂子类中完成，即通过工厂子类来确定究竟应该实例化哪一个具体产品类。

工厂方法模式包含四个角色：
    [抽象产品]是定义产品的接口，是工厂方法模式所创建对象的超类型，即产品对象的共同父类或接口；
    [具体产品]实现了抽象产品接口，某种类型的具体产品由专门的具体工厂创建，它们之间往往一一对应；
    [抽象工厂]中声明了工厂方法，用于返回一个产品，它是工厂方法模式的核心，任何在模式中创建对象的工厂类都必须实现该接口；
    [具体工厂]是抽象工厂类的子类，实现了抽象工厂中定义的工厂方法，并可由客户调用，返回一个具体产品类的实例；

工厂方法模式是简单工厂模式的进一步抽象和推广。
由于使用了面向对象的多态性，工厂方法模式保持了简单工厂模式的优点，而且克服了它的缺点。
在工厂方法模式中，核心的工厂类不再负责所有产品的创建，而是将具体创建工作交给子类去做。
这个核心类仅仅负责给出具体工厂必须实现的接口，而不负责产品类被实例化这种细节，
这使得工厂方法模式可以允许系统在不修改工厂角色的情况下引进新产品。

工厂方法模式适用情况包括：
    一个类不知道它所需要的对象的类；
    一个类通过其子类来指定创建哪个对象；
    将创建对象的任务委托给多个工厂子类中的某一个，客户端在使用时可以无须关心是哪一个工厂子类创建产品子类，需要时再动态指定。

工厂方法模式又称为工厂模式，也叫虚拟构造器(Virtual Constructor)模式或者多态工厂(Polymorphic Factory)模式，它属于类创建型模式。
"""

class Product_abstract(object):
    """
    抽象产品
    """
    def use(self):
        pass

class Product_concrete_int(Product_abstract):
    """
    具体产品 1
    """
    def use(self):
        print 1234567890

class Product_concrete_str(Product_abstract):
    """
    具体产品 2
    """
    def use(self):
        print 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Factory_abstract(object):
    """
    抽象工厂
    """
    def create_product(self):
        return Product_abstract()

class Factory_concrete_int(Factory_abstract):
    """
    具体工厂 1
    """
    def create_product(self):
        return Product_concrete_int()

class Factory_concrete_str(Factory_abstract):
    """
    具体工厂 2
    """
    def create_product(self):
        return Product_concrete_str()


factory_int = Factory_concrete_int()
product_int = factory_int.create_product()
product_int.use()
# 1234567890

factory_str = Factory_concrete_str()
product_str = factory_str.create_product()
product_str.use()
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
