#Turn Up the Temperature

#Converting farenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#Temp at 100 F
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#Converting celsius to farenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#Temp at 0 C
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#Use the Force
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")
