def longest_increasing_subsequence(numbers):
    if not numbers:
        return[]
    
    value = len(numbers)
    lengths = [1]* value
    prev_indices = [-1] * value
    
    for i in range(value):
        for j in range(i):
            if numbers[i] > numbers[j] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j
                max_length = max(lengths)
                max_index = lengths.index(max_length)
                
                lis =[]
                while max_index != -1:
                    lis.append(numbers[max_index])
                    max_index = prev_indices[max_index]
                    return lis[::-1]
                
                

number = [3,4,2,8,10,5,1]
results = longest_increasing_subsequence(number)
print(results)
                
     
    