def combined_sorted_array(arr1, arr2):
    answer=[]
    i=j=0
    while i < len(arr1) and j< len(arr2):
        if arr1[i] < arr2[j]:
            answer.append(arr1[i])
            i+=1
        else:
            answer.append(arr2[j])
            j+=1
    while i< len(arr1):
        answer.append(arr1[i])
        i+=1
    while j< len(arr2):
        answer.append(arr2[2])
        j+=1

    return answer
    

