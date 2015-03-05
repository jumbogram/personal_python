''' Given an array A of size n, which contains values from 1..n, rearrage the
 array so that A[i], has the value of index, at which i is preset.'''

array = []
n = input('Enter the size of the array');
for i in range(0, n):
    x = input('Enter the element');
    array.append(x);

index = 0;
jumpIndex = 0;

while index < n:
    currentValue = array[index];
    if (array[index] >= n):
        index+=1;
        continue;

    if (array[index] == index):
        array[index] += n;
        index+=1;
        continue;

    currIndex = index;
    targetIndex = array[currIndex];
    while True:
        swapValue = array[targetIndex];
        array[targetIndex] = currIndex + n;
        currIndex = targetIndex;
        targetIndex = swapValue;
        if (targetIndex >= n):
            break;

for i in range(0, n):
    print array[i]-n;


