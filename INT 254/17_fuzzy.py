import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define Fuzzy Variables
temperature = ctrl.Antecedent(np.arange(0,101,1),'temperature')
humidity=ctrl.Antecedent(np.arange(0,101,1),'humidity')
fan_Speed=ctrl.Consequent(np.arange(0,101,1),'fan_speed')

# Define Membership Function
temperature['cold']=fuzz.trimf(temperature.universe,[0,0,50]) # Triangular Membership Function: trimf
temperature['medium']=fuzz.trimf(temperature.universe,[20,50,80])
temperature['hot']=fuzz.trimf(temperature.universe,[50,100,100])

humidity['dry']=fuzz.trimf(humidity.universe,[0,0,50])
humidity['normal']=fuzz.trimf(humidity.universe,[20,50,80])
humidity['humid']=fuzz.trimf(humidity.universe,[50,100,100])

fan_Speed['low']=fuzz.trimf(fan_Speed.universe,[0,0,50])
fan_Speed['medium']=fuzz.trimf(fan_Speed.universe,[20,50,80])
fan_Speed['high']=fuzz.trimf(fan_Speed.universe,[50,100,100])

# Defining Fuzzy Rules
rule1=ctrl.Rule(temperature['cold']|humidity['dry'],fan_Speed['low'])
rule2=ctrl.Rule(temperature['medium']|humidity['normal'],fan_Speed['medium'])
rule3=ctrl.Rule(temperature['hot']|humidity['humid'],fan_Speed['high'])

# Create Fuzzy Inference System:FIS
fis=ctrl.ControlSystem([rule1,rule2,rule3])
fan_speed_ctrl=ctrl.ControlSystemSimulation(fis)

temp=float(input("Enter the Temperature: "))
hum=float(input("Enter the humidity: "))

# Pass input to the FIS and compute the output
fan_speed_ctrl.input['temperature']=temp
fan_speed_ctrl.input['humidity']=hum
fan_speed_ctrl.compute()

# Printing Output
print("Fan Speed:",fan_speed_ctrl.output['fan_speed'])