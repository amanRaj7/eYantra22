# Function to calculate Euclidean distance between two points
def dec_to_binary(n):

    bin_num = None

    # Complete this function to return binary equivalent output of the given number 'n' in 8-bit format
    bin_num = bin(n).replace('0b', '')
    bin_num = (8-len(bin_num))*'0'+bin_num
    return bin_num


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the n value
    for case in range(1,test_cases+1):
        # take the n input values
        n = int(input())

        # print (n)

        # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
        bin_num = dec_to_binary(n)
        print(bin_num)