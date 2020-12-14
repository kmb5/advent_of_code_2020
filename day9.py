from helpers import readlines

def main():


    data = readlines('inputs/day9_input.txt')

    data = [int(x) for x in data]

    subArraySum(data, len(data), 466456641)

    d = data[493:510]
    d.sort()
    print(d[0] + d[-1])

    return

    for i in range(5, len(data)):

        to_check = data[i-25:i]
        #print(to_check)

        sums = _generate_sums(to_check)

        if data[i] not in sums:
            print(data[i])
    
def _generate_sums(data):

    sums = []

    for num1 in data:
        for num2 in data[1:]:
            #print(num1)
            #print(num2)
            sum_nums = num1 + num2
            sums.append(sum_nums)

    #print(sums)
    return sums

    
def subArraySum(arr, n, sum): 
      
    # Initialize curr_sum as 
    # value of first element 
    # and starting point as 0  
    curr_sum = arr[0] 
    start = 0
  
    # Add elements one by  
    # one to curr_sum and  
    # if the curr_sum exceeds  
    # the sum, then remove  
    # starting element  
    i = 1
    while i <= n: 
          
        # If curr_sum exceeds 
        # the sum, then remove 
        # the starting elements 
        while curr_sum > sum and start < i-1: 
          
            curr_sum = curr_sum - arr[start] 
            start += 1
              
        # If curr_sum becomes 
        # equal to sum, then 
        # return true 
        if curr_sum == sum: 
            print ("Sum found between indexes") 
            print ("% d and % d"%(start, i-1)) 
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
  
    # If we reach here,  
    # then no subarray 
    print ("No subarray found") 
    return 0

if __name__ == "__main__":
    main()
