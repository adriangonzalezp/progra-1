def main():
    nums = readNums()
    mean = findMean(nums)
    larger = findLarger(nums)
    smaller = findSmaller(nums)
    median = findMedian(nums)
    printResults(nums,mean,larger,smaller,median)

def readNums():
    nums = input("Escriba la lista de numeros separados por coma: ")
    result = list(map(int,nums.split(",")))
    return result

def findMean(nums):
    acum = 0
    for i in nums:
        acum = acum + i
    return (acum / len(nums))

def findLarger(nums):
    return max(nums)

def findSmaller(nums):
    return min(nums)

def findMedian(nums):
    nums.sort()
    numsLen = len(nums)
    index = int((numsLen - 1) / 2)
    if numsLen % 2 == 0:
        i1 = nums[index + 1]
        i2 = nums[index]
        return (i1 + i2) / 2
    else:   
        return nums[index]

def printResults(nums,mean,larger,smaller,median):
    nums.sort()
    print(f"Lista ordenada: {nums} ")
    print(f"El promedio es: {mean}")
    print(f"El mayor es: {larger}")
    print(f"El menor es: {smaller}")
    print(f"La media es: {median}")

main()