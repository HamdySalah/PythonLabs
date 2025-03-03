class Car:
    '''Car Class:
    - attributes (name, fuelRate, velocity)
    - methods (run, stop)
    '''

    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = self._validate_fuel(fuelRate)
        self.velocity = self._validate_velocity(velocity)

    def _validate_velocity(self, velocity):
        if 0 <= velocity <= 200:
            return velocity
        else:
            raise ValueError("Velocity must be between 0 and 200.")

    def _validate_fuel(self, fuelRate):
        if 0 <= fuelRate <= 100:
            return fuelRate
        else:
            raise ValueError("Fuel Rate must be between 0 and 100.")

    def run(self, velocity, distance):
        '''Decreases fuelRate, updates velocity, and stops if fuel runs out.'''
        self.velocity = self._validate_velocity(velocity)

        print(f"{self.name} is running at {self.velocity} km/h for {distance} km...")

        fuel_needed = distance * 0.5  # Example: Fuel decreases by 0.5 per km
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            remaining_distance = 0
        else:
            remaining_distance = distance - (self.fuelRate / 0.5)
            self.fuelRate = 0

        self.stop(remaining_distance)

    def stop(self, remaining_distance=0):
        '''Stops the car, sets velocity to 0, and notifies the remaining distance.'''
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Car stopped! Fuel empty. Remaining distance: {remaining_distance} km.")
        else:
            print("Car stopped! You have reached your destination.")