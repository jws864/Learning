<<<<<<< HEAD
# hey it's me :)
# Jutin Simms and my email and shit
=======
>>>>>>> master
import sys
from greeter import Greeter

name = sys.argv[1] if len(sys.argv) > 1 else 'World'
greeter = Greeter(name)
print greeter.greet()