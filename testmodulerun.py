#unlike javascript, python doesn't require explicit export
import testmodule1
from testmodule2 import submodule as sb

testmodule1.testprint("HELLO!")
sb(2,3)