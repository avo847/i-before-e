
class Counter:
  "counter class for cases"
  
  def __init__(self):
    self.one = 0
    self.two = 0
    self.three = 0
    self.four = 0
    
  def display_counts(self):
    print "displaying case counts:"
    print "case one (i before e, not following c): ", self.one
    print "case two (e before i , not following c): ", self.two
    print "case three (i before e, after c): ", self.three
    print "case four (e before i, after c): ", self.four
    
  def display_percentages(self):
    tot = self.one + self.two + self.three + self.four
    print "displaying percentages:"
    print "case one: {0:.3f}".format(1.0 * self.one / tot)
    print "case two: {0:.3f}".format(1.0 * self.two / tot)
    print "case three: {0:.3f}".format(1.0 * self.three / tot)
    print "case four: {0:.3f}".format(1.0 * self.four / tot)
  



def ei_ie_finder(word, counter, start=0):
  """ 
  search word for insances of ie and ei beginning at at start.
  (characters are indexed starting at 0). If found, call check_case function
  """
  while True:
    ie = word.find('ie', start)
    ei = word.find('ei',start)
    loc = 0
  
    if ie >= 0 and ei >= 0:
      loc = min(ie,ie)
    elif ie >= 0:
      loc = ie
    elif ei >= 0:
      loc = ei
    else:
      return
    start = loc+2
    check_case(word, counter, loc)
  
  
  
  
def check_case(word, counter, loc):
  """
  ei or ie has been found in word at location indexed by loc.
  check whether preceding character is c or not. 
  -word is the full string 
  -counter contains counts of cases encountered
  -loc indexes start of ei or ie
  """
  
  if loc == 0:
    # choose an action for words that start with ie or ie
    return -1
  
  vow= word[loc]
  pre = word[loc-1]
  
  if vow == 'i' and pre != 'c':
    counter.one += 1
  elif vow == 'e' and pre != 'c':
    counter.two +=1
  elif vow == 'i' and pre == 'c':
    counter.three += 1
  elif vow == 'e' and pre == 'c':
    counter.four += 1
  else:
    print "error: unknown case"
    return -1
    
  return 0
  
  

case_count = Counter()


f = open('norvig_list.txt','r')
for line in f:
  ei_ie_finder(line, case_count)

case_count.display_counts()
print
case_count.display_percentages()