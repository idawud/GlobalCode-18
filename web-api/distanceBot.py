from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def distance(loc1,loc2):
    geolocator = Nominatim()
    location = geolocator.geocode(loc1) # parameter is a string of the location
    #location = geolocator.reverse("52.509669, 13.376294")
    cit1 = (location.latitude, location.longitude)

    location = geolocator.geocode(loc2)
    cit2 = (location.latitude, location.longitude)
    
##    return geodesic(cit1, cit2).miles
    return geodesic(cit1, cit2).km

if __name__ == "__main__":
    print("Enter Location in the form 'Cape Coast,GH' ")
    plc1 = str(input("Enter LOCTAION one: "))
    plc2 = str(input("Enter LOCTAION two: "))
    #print(plc1)
    dist = distance(plc1,plc2)
    print("The Distance between {} and {} is: {}km".format(plc1,plc2,round(dist,2)))
