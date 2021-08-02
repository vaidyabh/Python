
#-----------------------------------------------------###-------------------------------------###------------------------###-----------------------------------------
# 1) Concat the longest array based on the number of the joined varibales given in the string

def longest_consec(strarr, k):
    longest_arr = ''
    # Read all the values except number of consecutive occurance
    # If k = 1, then need to return the longest string - AV
    if k <= 0:
        longest_arr = ''
        return longest_arr
    elif k == 1:
        for i in range (0, len(strarr)):
            if len(longest_arr) < len(strarr[i]):
                longest_arr = strarr[i]
        return longest_arr
    # When k is > 1 -- AV
    else:
        for key in range(len(strarr) - k + 1):
            arr_data = ''.join(strarr[key : key + k])
            
        # If the length of the new consecutive occurance is > old occurance, replace it
            if len(arr_data) > len(longest_arr):
                longest_arr = arr_data

        return longest_arr

testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")





#-----------------------------------------------------###-------------------------------------###------------------------###-----------------------------------------
