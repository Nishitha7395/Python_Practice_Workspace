#Program for demonstrating Inheritance
#InhEx2.py
class C1:
    def disp1(self):
        print("C1---disp1()")

class C2(C1):
    def disp2(self):
        self.disp1()
        print("C2----disp2()")

#main program
o2=C2()
o2.disp2()
