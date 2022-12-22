#把元组用作记录

lax_coordinates = (33.9425, -188.408056)
#元组拆包
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', "XDA205856")]

for passport in sorted(traveler_ids):
    #自动对应前面的两个位置
    print('%s/%s' % passport)

#元组拆包
for country, _ in traveler_ids:
    print(country)