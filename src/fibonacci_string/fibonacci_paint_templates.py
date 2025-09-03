import turtle
import random

class FibonacciPaintTemplate:
    """
    Class containing specific rules and operations for painting fibonacci strings
    per character
    """
    def __init__(self, string_a, string_b, delimiter=".", color_palette = ["#EFBDEB","","#B68CB8","#6461A0","#314CB6","#0A81D1"]):
        self.string_a = string_a
        self.string_b = string_b
        self.delimiter = delimiter
        self.color_palette = color_palette
        self.color = 0

        # TODO: Split these guys out into individual classes?
        self.simple_turns_a_angle = 90
        self.simple_turns_b_angle = 180
        self.simple_turns_fwrd = 1

        self.vines_vine_angle = random.randint(5,15)
        self.vines_vine_len = random.randint(4,6)
        self.vines_main_leaf_length = random.randint(4,20)
        self.vines_sub_leaf_length = random.randint(2,6)
    
    def makeLeaf(self, t: turtle.Turtle, len = 2, point_len = 2, base_len = 2):
        """
        A prefab template for a single leaf
        """
        t.left(45)
        t.forward(base_len)
        t.right(45)
        t.forward(len)
        t.right(45)
        t.forward(point_len)
        t.right(90)
        t.forward(point_len)
        t.right(45)
        t.forward(len)
        t.right(45)
        t.forward(base_len)

    def getNextColor(self, change=1):
        if (self.color+change >= len(self.color_palette)):
            self.color = 0
        elif (self.color+change < 0):
            self.color = len(self.color_palette)-1
        else:
            self.color = self.color+change

    def checkActionKwargs(self, kwargs):
        t = kwargs.get("t")
        chr = kwargs.get("chr")
        if (t == None or chr == None):
            raise Exception(f"Unable to paint, missing kwargs t={t} chr={chr}")
        
        return chr, t

    def vines(self, **kwargs):
        """
        Paint template which creates interesting vine-like structures.

        Configurable in set_vines
        """
        chr, t = self.checkActionKwargs(kwargs)

        if (t.color != self.color):
            t.color(self.color_palette[self.color])
            
        if (chr == self.delimiter):
            self.getNextColor()
            return

        if (chr == self.string_a):
            t.right(self.vines_vine_angle)
            t.forward(self.vines_vine_len)
        elif (chr == self.string_b):
            self.makeLeaf(t, self.vines_sub_leaf_length, 1, 1)
            t.left(135)
            t.forward(2)
            self.makeLeaf(t, self.vines_main_leaf_length, 3, 3)
            t.left(135)
            t.forward(2)
            self.makeLeaf(t, self.vines_sub_leaf_length, 1, 1)
            t.left(135)
            t.forward(1)

        t.right(20)

    def set_vines(self, vine_len, vine_angle, main_leaf_length, sub_leaf_length):
        """
        Configures the vines template

        vine_len = How long the vines are
        vine_angle = How intense the vine curves will be
        main_leaf_length = How long the middle leaf will be
        sub_leaf_length = How long either of the sub leaves will be
        """
        self.vines_vine_len = vine_len
        self.vines_vine_angle = vine_angle
        self.vines_main_leaf_length = main_leaf_length
        self.vines_sub_leaf_length = sub_leaf_length

    def simple_turns(self, **kwargs):
        """
        Paint template which makes simple angle changes to the
        turtle based on character type.

        Configurable in set_simple_turns
        """
        chr, t = self.checkActionKwargs(kwargs)

        if (t.color != self.color):
            t.color(self.color_palette[self.color])
            
        if (chr == self.delimiter):
            self.getNextColor()
            turtle.update()
            return

        if (chr == self.string_a):
            t.right(self.simple_turns_a_angle)
        elif (chr == self.string_b):
            t.left(self.simple_turns_b_angle)
        t.forward(self.simple_turns_fwrd)

    def set_simple_turns(self, a_angle=90, b_angle=180, fwrd=2):
        """
        Configures the simple turns template
        
        a_angle = How many degrees to turn when A is encountered
        b_angle = How many degrees to turn when B is encountered
        fwrd = How far the turtle should move each time
        """
        self.simple_turns_a_angle = a_angle
        self.simple_turns_b_angle = b_angle
        self.simple_turns_fward = fwrd