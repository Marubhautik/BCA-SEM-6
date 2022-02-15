def towerofhanoi(n, source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    towerofhanoi(n - 1, source, auxiliary, destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    towerofhanoi(n - 1, auxiliary, destination, source)
n=3

towerofhanoi(n,'A','B','c')
'''Move disk 1 from source A to destination B
Move disk 2 from source A to destination c
Move disk 1 from source B to destination c
Move disk 3 from source A to destination B
Move disk 1 from source c to destination A
Move disk 2 from source c to destination B
Move disk 1 from source A to destination B'''