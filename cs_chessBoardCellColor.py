# Given two cells on the standard chess board, determine whether they have the same color or not.

# def solution(cell1, cell2):
    
    # group_1 = ["A", "C", "E", "G"]
    # group_2 = ["B", "D", "F", "H"]
    # if (int(cell1[1])%2 !=0 and int(cell2[1])%2 ==0) or (int(cell1[1])%2 ==0 and int(cell2[1]) %2!=0):
    #     if cell1[0] in group_1 and cell2[0] in group_2:
    #         return True
    #     if cell1[0] in group_2 and cell2[0] in group_1:
    #         return True
    # elif (int(cell1[1])%2 ==0 and int(cell2[1])%2 ==0) or (int(cell1[1])%2 !=0 and int(cell2[1] )%2!=0):
    #     if cell1[0] in group_1 and cell2[0] in group_1:
    #         return True
    #     if cell1[0] in group_2 and cell2[0] in group_2:
    #         return True
    # return False





def solution(cell1, cell2):
    print(ord(cell1[0]) % 2 == 0)
    print(int(cell1[1]) % 2 == 0)
    cell1Dark = (ord(cell1[0]) % 2 == 0) != (int(cell1[1]) % 2 == 0)
    print(cell1Dark)
    cell2Dark = (ord(cell2[0]) % 2 == 0) != (int(cell2[1]) % 2 == 0)
 
    return cell1Dark == cell2Dark

#还不是很懂怎么逻辑