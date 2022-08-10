from cmath import cos, sin
import numpy

class KinSolver:

    def __init__(self):
        self.L1 = 0.5
        self.L2 = 0.5
        self.L3 = 0.5

    def cos_XY(self, theta_X, theta_Y):
        return (cos(theta_X)*cos(theta_Y) - sin(theta_X)*sin(theta_Y))

    def sin_XY(self, theta_X, theta_Y):
        return (sin(theta_X)*cos(theta_Y) + sin(theta_Y)*cos(theta_X))
    
    def r11(self, theta_1, theta_2, theta_3, theta_4, theta_5):
        return (cos(theta_1)*cos(theta_5)*(cos(theta_2)*self.cos_XY(theta_3, theta_4) - sin(theta_2)*self.sin_XY(theta_3, theta_4)) + sin(theta_1)*sin(theta_5))
    
    def r12(self, theta_1, theta_2, theta_3, theta_4, theta_5):
        return (-cos(theta_1)*sin(theta_5)*(cos(theta_2)*self.cos_XY(theta_3, theta_4) - sin(theta_2)*self.sin_XY(theta_3, theta_4)) + sin(theta_1)*cos(theta_5))
    
    def r13(self, theta_1, theta_2, theta_3, theta_4, theta_5):
        return cos(theta_1)*(cos(theta_2)*self.cos_XY(theta_3, theta_4) - sin(theta_2)*self.sin_XY(theta_3, theta_4))

    def Px(self, theta_1, theta_2, theta_3, theta_4, theta_5, L1, L2, L3):
        return cos(theta_1)*(self.cos_XY(theta_2, theta_3)*L3 + cos(theta_2)*L2 + L1)
    
    def Py(self, theta_1, theta_2, theta_3, theta_4, theta_5, L1, L2, L3):
        return sin(theta_1)*(self.cos_XY(theta_2, theta_3)*L3 + cos(theta_2)*L2 + L1)

    def Pz(self, theta_1, theta_2, theta_3, theta_4, theta_5, L1, L2, L3):
        return (self.sin_XY(theta_2, theta_3)*L3 + sin(theta_2)*L2)

    def main(self):
        theta_1 = 0
        theta_2 = 0
        theta_3 = 0
        theta_4 = 0
        theta_5 = 0

        r11 = self.r11(theta_1, theta_2, theta_3, theta_4, theta_5)
        r12 = self.r12(theta_1, theta_2, theta_3, theta_4, theta_5)
        r13 = self.r13(theta_1, theta_2, theta_3, theta_4, theta_5)

        Px = self.Px(theta_1, theta_2, theta_3, theta_4, theta_5, self.L1, self.L2, self.L3)
        Py = self.Py(theta_1, theta_2, theta_3, theta_4, theta_5, self.L1, self.L2, self.L3)
        Pz = self.Pz(theta_1, theta_2, theta_3, theta_4, theta_5, self.L1, self.L2, self.L3)

        print("r: " + str(r11.real))
        print("p: " + str(r12.real))
        print("y: " + str(r13.real))
        print("x: " + str(Px.real))
        print("y: " + str(Py.real))
        print("z: " + str(Pz.real))

if __name__ == "__main__":
    arm_kin = KinSolver()
    arm_kin.main()