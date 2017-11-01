def interval_point(a, b, x):
        """Given parameters a, b and x. Takes three numbers and interprets a and b
        as the start and end point of an interval, and x as a fraction
        between 0 and 1 that returns how far to go towards b, starting at a"""
        if a == b:
            value = a
        elif a < 0 and b < 0:
            if x == 0:
               value = a
            else:
                a1 = abs(a)
                b1 = abs(b)
                value = -((a1-b1) + ((a1-b1)*x))
        else:
            value = (a + (b-a)*x)
        return value

print(interval_point(1,3,2))
