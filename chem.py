class Thermal:
    def heat_energy(self, m=None, c=None, t=None, q=None):
        if q is None:
           try: 
               q = m*c*t
               return q
           except: 
               print("PLEASE PUT VAILD NUMBERS")
        elif m is None:
            try: 
               m = q / (c*t)
               return m
            except: 
                print("PLEASE PUT VAILD NUMBERS")
        elif c is None:
            try: 
               c = q / (m*t)
               return c
            except: 
                print("PLEASE PUT VAILD NUMBERS")
        else:
            try: 
                t = q / (m*c)
                return t
            except: 
                print("PLEASE PUT VAILD NUMBERS")

    def enthaply_of_solution(self, q=None, n=None, h=None):
        h = q*n

if __name__ == "__main__":
    given = {"m": 24, "c": 4.18, "t": 5}
    print(Thermal().heat_energy(**given))