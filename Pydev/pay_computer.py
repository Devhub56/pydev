#!/usr/bin/env python
h=float(input('Enter Hours of work :')) #convert the input to float
r=float(input('Enter the rate : '))


def computepay(h,r): #define your function
    if h <=40:
        pay= h*r
    else:
        pay=((40*r)+(h-40)*1.5*r)
    return pay # return the result if any of the conditions is met

total_pay=computepay(h,r) # use the input to calculate the pay using the method you defined above

print('The total payout is :',total_pay) #print your result
