import re, json

s1 = 'profile|73241232|<Aamir><Hussain><Khan>|<Mumbai><<72.872075><19.075606>>|73241232.jpg**followers|54543342|<Anil><><Kapoor>|<Delhi><<23.23><12.07>>|54543342.jpg@@|12311334|<Amit><><Bansal>|<Bangalore><<><>>|12311334.jpg'
#s2 = 'profile|73241234|<Niharika><><Khan>|<Mumbai><<72.872075><19.075606>>|73241234.jpg**followers|54543343|<Amitabh><><>|<Dehradun><<><>>|54543343.jpg@@|22112211|<Piyush><><>||'
a = re.split(r'[**]+followers+', s1)
b = a[0].replace('profile', '').replace('|', ' |')
profile = re.split(r'[|]+', b)
name =  re.findall( '<(.*?)>', profile[2], re.DOTALL)
location = re.findall( '<(.*?)>', profile[3], re.DOTALL)
long = float(location[1].replace('<',''))
lat = float(location[2])
#followers
fo = []
for x in re.split(r'[@@]+', a[1]):
    x1 = x.replace('|', ' |')
    y = re.split(r'[|]+', x1)
    f_id = y[1].replace(' ', '')
    f_name = re.findall( '<(.*?)>', y[2], re.DOTALL)
    g = re.findall( '<(.*?)>', y[3], re.DOTALL)
    if (g == []):
        f_location = f_long = f_lat = ''
    else:
        f_location = g[0]
        try:
            f_long = float(g[1].replace('<',''))
        except:
            f_long = g[1].replace('<','')
        try:
            f_lat = float(g[2])
        except:
            f_lat = g[2]
    j = ({"id":f_id, "imageId": y[4], "name": {"first": f_name[0], "middle": f_name[1], "last": f_name[2]}, "location": {"name": f_location, "coords": {"long": f_long, "lat": f_lat}}})
    fo.append(j)

ma = json.dumps({"id":profile[1],"name":{"first":name[0],"middle":name[1],"last":name[2]},"location":{"name":location[0],"coords":{"long":long,"lat":lat,}},"imageId":profile[4],"followers":fo})
print(ma)
