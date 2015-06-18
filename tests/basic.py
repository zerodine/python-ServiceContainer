import unittest

from servicecontainer import Service, Container, ServiceInterface

class TestSimple(unittest.TestCase):
    
    def test_service(self):
        c = Container()
        class ExampleService(object):
            val = None
            def __init__(self, param1):
                self.val = param1

        class ExampleService2(ServiceInterface):
            val = None
            def __init__(self, param1):
                self.val = param1

            @classmethod
            def asService(cls, parameters):
                return Service("testservice2", cls, parameters)


        s = Service("testservice", ExampleService, {"param1": "param1_value"})
        c.add(s)
        c.add(ExampleService2.asService({"param1": "param1_value"}))

        instance = c.get('testservice')
        self.assertEqual('param1_value', instance.val)

        list = c.list()
        self.assertEqual(2, len(list))
        self.assertEqual(list[0], 'testservice')

        instance2 = c.get('testservice')
        self.assertIs(instance, instance2)