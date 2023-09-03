from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    
    def __init__(self, **info):
    
        self.designation = info.get('designation')
        if info.get('name') != '':
            self.name = info.get('name')
        else:
            self.name = None
        #self.diameter = info.get('diameter',float('nan'))
        self.diameter = float(info['diameter']) if info.get('diameter', '') != '' else float('nan')
        self.hazardous = info.get('hazardous')

        self.approaches = []

    @property
    def fullname(self):
        return self.designation + ' ' + self.name

    def __str__(self):
        s = "NEO {} has a diameter of {} km and {} potentially hazardous.".format(
            self.fullname,
            self.diameter,
            'is' if self.hazardous else 'is not'
        )
        return s

    def __repr__(self):
        return "NearEarthObject(designation={!r}, name={!r}, diameter={:.3f}, hazardous={!r})".format(
            self.designation,
            self.name,
            self.diameter,
            self.hazardous
        )

class CloseApproach:
    
    def __init__(self, **info):
        
        self.designation = info.get("designation")
        self.time = info.get('time')  # TODO: Use the cd_to_datetime function for this attribute.
        if self.time:
            self.time = cd_to_datetime(self.time)
        self.distance = float(info.get('distance',0.0))
        self.velocity = float(info.get('velocity',0.0))

        # Create an attribute for the referenced NEO, originally None.
        self.neo = info.get('neo',None)

    @property
    def time_str(self):
        return datetime_to_str(self.time)

    def __str__(self):
        return "At {}, '{}' approaches Earth at a distance of {} au and a velocity of {} km/s.".format(
            self.time_str,
            self.neo.fullname,
            self.distance,
            self.velocity
        )

    def __repr__(self):
        return "CloseApproach(time={!r}, distance={}, velocity={}, neo={!r})".format(
            self.time_str,
            self.distance,
            self.velocity,
            self.neo
        )
