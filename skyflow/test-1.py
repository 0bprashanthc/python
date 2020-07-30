"""
Func get_movies( movieLengths []int, duration int){

}

3, [1,2,2] -> 1,2
4, [1,3,1] -> [1,3],[3,1]
1, [2,3,3] -> 0
2, [2,3,3] -> 2

[] O(n)
1,2,2 -> (d-1) in sub-list -> [1,2]

4, [1,3,1,2] :
1: [1]
2: [1,1]
3: [(1,1,1),(1,2)]

O(n)


 
Movies >= Duration of flight 


"""
