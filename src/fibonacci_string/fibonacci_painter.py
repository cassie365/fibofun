import turtle

from src.fibonacci_string.fibonacci_string import FibonacciString

class FibonacciPainter:
    """
    Class which allows you to paint a fibonacci string using a turtle
    """
    def __init__(self, dir_path, win_width=2000, win_height=2000, speed=0,update_freq=0, bg_color="black"):
        self.win_width = win_width
        self.win_height = win_height
        self.speed = speed
        self.update_freq = update_freq
        self.bg_color = bg_color
        self.dir_path = dir_path

    def paintFibonacciString(self, generation_file, filename, action):
        """
        Reads our fibonacci string file and paints it to a TKinter canvas.
        Stops when file is done being read.

        Creates an .eps file at the configured directory
        """
        turtle.setup(self.win_width, self.win_height) # Size of the window
        turtle.screensize(self.win_width, self.win_height, self.bg_color) # Size of the canvas
        turtle.tracer(self.update_freq)
        t = turtle.Turtle()
        t.speed(self.speed)

        try:
            output_filepath = f"{self.dir_path}/{filename}.eps"
            with open(generation_file, "r") as f:
                while True:
                    chr = f.read(1)
                    if not chr:
                        break
                    action(chr=chr, t=t)

            canvas = turtle.getscreen().getcanvas()
            canvas.postscript(file=output_filepath)

            self._log(f"Finished painting: {output_filepath}")
        except FileNotFoundError:
            self._log(f"File {filename} not found")
        except PermissionError:
            self._log(f"Painter does not have permission to open {filename}")
        except Exception as e:
            self._log(f"Unexpected error - {e}")
        finally:
            turtle.done()
            self._log(f"Stopped painting")
        
    
    def _log(self,message):
        print(f"FibonacciPainter: {message}")