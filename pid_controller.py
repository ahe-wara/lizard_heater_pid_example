
class PID_Controller :
  
  dt  = 0.0
  max = 0.0
  min = 0.0
  kp  = 0.0
  kd  = 0.0
  ki  = 0.0
  difference = 0.0
  int = 0.0
  
  def __init__(self, dt, max, min, kp, kd, ki) :
    self.dt  = dt
    self.max = max
    self.min = min
    self.kp  = kp
    self.kd  = kd
    self.ki  = ki
    
  def run(self,set_value,actual_value) :
    difference = set_value - actual_value;

    P = self.kp * difference;
    print('P: %.2f' % (P))

    #self.int += difference * self.dt;
    self.int += difference;
    #if clause added ahe
    #if self.int < self.max:
    I = self.ki * self.int;
   # else:
    #    I = self.max
    print('I: %.2f' % (I))

    D = self.kd * (difference - self.difference) / self.dt;
    print('D: %.2f' % (D))

    output = P + I + D;

    if output > self.max :
        output = self.max
    elif output < self.min :
        output = self.min

    self.difference = difference;
    return(output);

'''
def main() :
  pid = myPID(0.1, 100, -100, 0.1, 0.01, 0.5)

  val = 20;
  for i in range(100) :
    inc = pid.run(0, val)
    print('val:','{:7.3f}'.format(val),' inc:','{:7.3f}'.format(inc) )
    val += inc
'''