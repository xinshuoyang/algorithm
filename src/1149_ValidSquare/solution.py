class Solution:
    """
    @param p1: the first point
    @param p2: the second point
    @param p3: the third point
    @param p4: the fourth point
    @return: whether the four points could construct a square
    """
    def validSquare(self, p1, p2, p3, p4):
        # Write your code here
       
        l12 = (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        l13 = (p1[0]-p3[0])**2+(p1[1]-p3[1])**2
        l14 = (p1[0]-p4[0])**2+(p1[1]-p4[1])**2

        if l12 != l13 and l13 != l14 and l12 != l14:
            return False
        else:
            if l12 == l13:
                l24 = (p2[0]-p4[0])**2+(p2[1]-p4[1])**2
                l34 = (p3[0]-p4[0])**2+(p3[1]-p4[1])**2

                if l24 == l34 and l24 == l12:
                    return True
                else:
                    return False
            elif l13 == l14:
                l24 = (p2[0]-p4[0])**2+(p2[1]-p4[1])**2
                l23 = (p2[0]-p3[0])**2+(p2[1]-p3[1])**2

                if l24 == l23 and l13 == l24:
                    return True
                else:
                    return False
            else:
                l32 = (p3[0]-p2[0])**2+(p3[1]-p2[1])**2
                l34 = (p3[0]-p4[0])**2+(p3[1]-p4[1])**2

                if l32 == l34 and l32 == l12:
                    return True
                else:
                    return False
