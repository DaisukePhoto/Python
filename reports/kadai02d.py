#kadai02d 16D8101021C 野口大輔　2017-10-02

start_m=int(input("梅雨入りした月は"))
start_d=int(input("梅雨入りした日は"))
end_m=int(input("梅雨明けした月は"))
end_d=int(input("梅雨明けした日は"))

if start_m==5:
 start_d=start_d+30
elif start_m==6:
 start_d=start_d+61
elif start_m==7:
 start_d=start_d+91
elif start_m==8:
 start_d=start_d+122

if end_m==5:
 end_d=end_d+30
elif end_m==6:
 end_d=end_d+61
elif end_m==7:
 end_d=end_d+91
elif end_m==8:
 end_d=end_d+122

days=end_d-start_d

print("梅雨の期間は",days,"日間です")

"""
(py361) [16D8101021C@ise31c ~]$ python kadai02d.py
梅雨入りした月は6
梅雨入りした日は7
梅雨明けした月は7
梅雨明けした日は6
梅雨の期間は 29 日間です
"""
