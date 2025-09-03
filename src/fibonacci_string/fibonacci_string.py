class FibonacciString:
    """
    Class which generates and saves fibonacci strings
    """
    def __init__(self, name:str, string_a:str, string_b:str, steps:int, dir_path:str, delimiter="."):
        self.string_a = string_a
        self.string_b = string_b
        self.steps = steps
        self.name = name
        self.has_generated = False
        self.dir_path = dir_path
        self.filename = dir_path+"/"+name+".txt"
        self.delimiter=delimiter

    def generateAndSave(self):
        string_a = self.string_a
        string_b = self.string_b
        steps = self.steps
        delimiter = self.delimiter

        if (self.has_generated):
            self._log(f"Already Generated {self.filename}")

        try:

            with open(self.filename, 'w') as f:
                a = [""]
                b = [string_a]
                for i in range(steps+1):
                    if (i >= 1):
                        newB = self._appendToEachElement(a, string_b) + self._appendToEachElement(b, string_a)
                        a = b
                        b = newB
                    a_chars = "".join(a)
                    f.write(a_chars+delimiter)

            self._log(f"String generation successful: {self.filename}")

        except IOError as e:
            self.has_generated = False
            self._log(f"An error occured while writing fibonacci string to file: {e}")

        finally:
            self.has_generated = True
            self._log("Stopping string generation.")


    def _log(self, message:str):
        print(f"FibonacciString: {message}")
    
    
    def _appendToEachElement(self, ogList, stringToAppend):
        newList = ogList.copy()
        for i in range(len(newList)):
            newList[i] = newList[i]+stringToAppend

        return newList