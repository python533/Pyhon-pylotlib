import matplotlib.pyplot as plt

class pistons():
    def __init__(self,basınc_degeri,pistonların_olcusu,piston_adedi):
        self.basınc_degeri=basınc_degeri
        self.pistonların_olcusu=pistonların_olcusu
        self.piston_adedi=piston_adedi

    def hesapla(self):
        x=[-1.0, -0.5, 0.0 , 0.5, 1.0]
        y=[1.0, 0.25, 0.0, 0.25, 1.0]

        plt.plot(x,y)
        plt.show()