def parallel_processing(n, m, data):
    output = []
    atm=[0]*n
    for i in data:
      output.append([atm.index(min(atm)),min(atm)])
      atm[atm.index(min(atm))]+=i 
     
      
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    ievade = list(map(int,(input().split())))
    n=ievade[0]
    m=ievade[1]
    data=list(map(int,(input().split())))
  

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i in result:
        print(i[0],i[1])
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
