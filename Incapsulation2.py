class Test():
    def public_function(self):
        print("public method")

    def _protected_function(self):
        print("protected method")

    def __private_function(self):
        print("private method")

    def test_private(self):
        self.__private_function()


test = Test()

test.public_function()
test._protected_function()
test.test_private()
