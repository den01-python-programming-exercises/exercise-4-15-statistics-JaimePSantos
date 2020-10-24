from statistics import Statistics
def main():
  evenN = 0
  oddN = 0
  stat = Statistics()
  print("Enter numbers:")
  while(True):
    number = int(input())
    if(number==-1):
      break
    if(number%2==0):
      evenN += number
    if(number%2!= 0):
      oddN += number
    stat.add_number(number)
  print("Sum: %s"%stat.sum)
  print("Sum of even numbers: %s"%evenN)
  print("Sum of odd numbers: %s"%oddN)


if __name__ == '__main__':
    main()
