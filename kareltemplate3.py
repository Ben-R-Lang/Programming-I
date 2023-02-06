from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for move"""
    move()

  def tl(self):
    """Turn left"""
    turn_left()

  def tr(self):
      """Turn right"""
      self.tl()
      self.tl()
      self.tl()

  def ta(self):
    """Turn around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Print H using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

    def e(self):
      """Print E using beepers"""
      self.tl()
      self.put5()
      self.tr()
      self.put2()
      self.tr()
      self.m()
      self.m()
      self.tr()
      self.put2()
      self.tl()
      self.m()
      self.m()
      self.tl()
      self.put2()
      self.m()
      self.m()
      

    def l(self):
      """Print L using beepers"""
      self.tl()
      self.put5()
      self.ta()
      self.m()
      self.m()
      self.m()
      self.m()
      self.m()
      self.tl()
      self.m()
      self.put2()
      self.m()
      self.m()

    def o(self):
      """Print O using beepers"""
      self.tl()
      self.put5()
      self.tr()
      self.put2()
      self.m()
      self.put()
      self.tr()
      self.put5()
      self.tr()
      self.m()
      self.put2()
      self.m()
      self.put()
      self.ta()
      self.m()
      self.m()
      self.m()
      self.m()

    def fic(self) -> bool:
     """Front is clear"""
    return front_is_clear()

    def fib(self):
      """Front is blocked"""
      return not self.fic

      def ric(self):
        """Right is clear"""
        self.tr()
        if self.fic():
          self.tl()
        return True
        self.tl()
        return False

        def rib(self):
          """Right is blocked"""
          return not self.ric()

        def mazemove():
          """Maze Move"""
          if self.fib():
            self.tl()
          else: 
            self.m()
            if self.ric():
              self.tr()
              self.m()
            if self.ric():
              self.tr()
              self.m()
            
            pass

def main():
    """ Karel code goes here! """
    kt = ktools()
  
    pass


if __name__ == "__main__":
    run_karel_program()