from parent import Calculator

class child(Calculator):
    def __init__(self):
        # because in parent class constructor is defined
        #here calling parent constructor within child constructor
        #Calculator.__init__(self,1,2) #another way
        super(child, self).__init__(2,3)

    def superadd(self):
        return self.a + self.b

obj = child()
print(obj.superadd())
