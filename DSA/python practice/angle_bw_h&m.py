def angle(h,m):
   '''the minutes hand moves 360 and hour moves 360/12=30 deg and 0.5 par min ''' 
   angle_h=((h*30)+(m*0.5))%360
   angle_m=(m*6)%360
   if 0<=h <13 and 0<=m<61:
    angle=abs(angle_h-angle_m)
    return min(angle,360-angle)
h=int(input("enter hour it shoud be between 0 -12"))
m=int(input("enter minute it shoub be 0-60"))
print(f"absolute angle between hour and minute is {angle(h,m)}")