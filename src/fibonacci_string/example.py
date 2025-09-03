import os
from src.fibonacci_string.fibonacci_paint_templates import FibonacciPaintTemplate
from src.fibonacci_string.fibonacci_string import FibonacciString
from src.fibonacci_string.fibonacci_painter import FibonacciPainter

def example():
    '''
    An example of how this project can be used!
    '''
    gen_path = "gens"
    paint_path = "output"

    os.makedirs(gen_path, exist_ok=True)
    os.makedirs(paint_path, exist_ok=True)

    gen_name = "exampleGen"
    a = "a"
    b = "b"
    steps = 20

    # Pre-gen our fibonacci string pattern and save to the "gens" folder
    fib_string = FibonacciString(gen_name, a, b, steps, gen_path)
    fib_string.generateAndSave()

    fib_paint = FibonacciPainter(paint_path)

    # Init our template which will control what
    # happens each time a character is encountered
    fib_template = FibonacciPaintTemplate(a, b)

    # We use the "set" function for simple_turns to adjust the paramaters of generation
    fib_template.set_simple_turns(45, 45, 4)
    action = fib_template.simple_turns

    fib_paint.paintFibonacciString(fib_string.filename, gen_name, action)