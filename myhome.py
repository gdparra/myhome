class home(object):
   def __init__(self, color, dimensions, floors, rooms, showers, closets):
      self.color = color
      self.dimensions = dimensions
      self.floors = floors
      self.rooms = rooms
      self.showers = showers
      self.closets = closets
   
   def homedetails(self):
      print 'Home properties: Color: {color} Sq ft: {dimensions} Floors: {floors} Rooms: {rooms} Showers: {showers} Closets: {closets}'.format(color=self.color, dimensions=self.dimensions,floors=self.floors, rooms=self.rooms,showers=self.showers, closets=self.closets)
      print "\n"

   def totalsurface(self):
      self.totalsurface = self.dimensions*self.floors
      print "Your total surface is {totalsurface}".format(totalsurface=self.totalsurface)
      print "\n"

#Subclass of Home inheriting __init__ method
class apartment(home):
   def __init__(self, color, dimensions, floors, rooms, showers, closets, buildingnum):
      self.buildingnum = buildingnum
      super(apartment, self).__init__(color, dimensions, floors, rooms, showers, closets)
   
   def apartmentdetails(self):
      print 'Home properties: Building = {buildingnum} Color: {color} Sq ft: {dimensions} Floors: {floors} Rooms: {rooms} Showers: {showers} Closets: {closets}'.format(buildingnum=self.buildingnum, color=self.color, dimensions=self.dimensions,floors=self.floors, rooms=self.rooms,showers=self.showers, closets=self.closets) 
      print "\n"
      
myhome = home("blue",564,3,1,1,1)
myhome.homedetails()
myhome.totalsurface()

myapartment = apartment("Red", 400, 1, 1, 1, 1, "A")      
myapartment.apartmentdetails()
myapartment.totalsurface()

   
