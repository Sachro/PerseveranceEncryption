print("-- Type '%STOP%' to break the loop --")
while True:
  from PIL import Image, ImageDraw
  
  #string to binary encrypter
  
  def split(word):
    return [char for char in word]
  
  str = input("\nInput:\n")
  if str == '%STOP%':
    break
  list = split(str)

  #Dictionary of letters and their binary counterparts
  
  binary = {
    'a':'01100001', 
    'b':'01100010',
    'c':'01100011',
    'd':'01100100',
    'e':'01100101',
    'f':'01100110',
    'g':'01100111',
    'h':'01101000',
    'i':'01101001',
    'j':'01101010',
    'k':'01101011',
    'l':'01101100',
    'm':'01101101',
    'n':'01101110',
    'o':'01101111',
    'p':'01110000',
    'q':'01110001',
    'r':'01110010',
    's':'01110011',
    't':'01110100',
    'u':'01110101',
    'v':'01110110',
    'w':'01110111',
    'x':'01111000',
    'y':'01111001',
    'z':'01111010',
    ' ':'00000000',
    'A':'01000001',
    'B':'01000010',
    'C':'01000011',
    'D':'01000100',
    'E':'01000101',
    'F':'01000110',
    'G':'01000111',
    'H':'01001000',
    'I':'01001001',
    'J':'01001010',
    'K':'01001011',
    'L':'01001100',
    'M':'01001101',
    'N':'01001110',
    'O':'01001111',
    'P':'01010000',
    'Q':'01010001',
    'R':'01010010',
    'S':'01010011',
    'T':'01010100',
    'U':'01010101',
    'V':'01010110',
    'W':'01010111',
    'X':'01011000',
    'Y':'01011001',
    'Z':'01011010',
    '0':'00110000',
    '1':'00110001',
    '2':'00110010',
    '3':'00110011',
    '4':'00110100',
    '5':'00110101',
    '6':'00110110',
    '7':'00110111',
    '8':'00111000',
    '9':'00111001',
    '!':'00100001',
    '"':'00100010',
    '#':'00100011',
    '$':'00100100',
    '%':'00100101',
    '&':'00100110',
    "'":'00100111',
    '(':'00101000',
    ')':'00101001',
    '*':'00101010',
    '+':'00101011',
    ',':'00101100',
    '-':'00101101',
    '.':'00101110',
    '/':'00101111',
  }
  encrypted = []
  for items in list:
    if items in binary.keys():
      encrypted.append(binary[items])
  
  eNum = len(encrypted)

  #creating an image

  background = 100,100,100
  width = eNum*100+50
  Output = Image.new("RGB",(width,width),(background))
  CP = width/2
  T = 48
  
  #drawing an arc
  img = ImageDraw.Draw(Output)
  
  #DrawArc Function
  def DrawArc(CenterPoint, Diameter, Thickness, Color, Section):
    x0 = CenterPoint - (0.5*(Diameter))
    y0 = CenterPoint - (0.5*(Diameter))
    x1 = CenterPoint + (0.5*(Diameter))
    y1 = CenterPoint + (0.5*(Diameter))
  
    Sections = {'1' : [180,225], '2' : [225,270], '3' : [270,315], '4' : [315,360],'5' : [0,45], '6':[45,90], '7' : [90,135], '8' : [135,180]}
    
    img.arc([(x0,y0),(x1,y1)], start = Sections[Section][0], end = Sections[Section][1], fill=Color, width = Thickness)
  
  #Drawing the arc
  d=1
  for item in encrypted:
    num = item
    x = split(num) #makes each char in num into an item in x[]
    for i in range(8):
      if x[i] == '0':
        D = 100*d
        C = 'white'
        S = "% s" % (i+1)
      else:
        D = 100*d
        C = 'black'
        S = "% s" % (i+1)
      DrawArc(CP,D,T,C,S)
    d=d+1
  
  #saving the image to a file
  
  #virticle line
  img.line([(CP,CP+CP),(CP,CP-CP)], fill = (background), width = 4)
  
  #horizontal line
  img.line([(CP+CP,CP),(CP-CP,CP)], fill = (background), width = 4)
  
  #45 degree line
  img.line([(CP+CP,CP+CP),(CP-CP,CP-CP)], fill = (background), width = 4)
  
  #45 degre line
  img.line([(CP-CP,CP+CP),(CP+CP,CP-CP)], fill = (background), width = 4)
  
  img.rectangle([(CP,CP-2),(0,CP+2)], fill = 'red')
  Output.save(str+".png")
  print('Done!')
