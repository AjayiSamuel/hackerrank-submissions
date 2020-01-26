def cube_value_check(x,y,z,n):
    the_list = [[i, j, k] for i in range(x+1) for j in range(y + 1) for k in range(z + 1) if((i + j + k) != n)]
    return the_list

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(cube_value_check(x,y,z,n))



# x = int ( raw_input())
# y = int ( raw_input())
# n = int ( raw_input())
# ar = []
# p = 0
# for i in range ( x + 1 ) :
#     for j in range( y + 1):
#         if i+j != n: ar.append([]) ar[p] = [ i , j ] p+=1 print ar
# # Other smaller codes may also exist, but using list comprehensions is always a good option. Code using list comprehensions:
#
# x = int ( raw_input())
# y = int ( raw_input())
# n = int ( raw_input())
# print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]
#
#
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

# x, y, z, n = 2, 2, 2, 2

# def cube_check(x,y,z,n):
#     the_list = [[i, j, k] for i in range(x+1) for j in range(y + 1) for k in range(z + 1) if((i + j + k) != n)]
#     return the_list
#
# print(cube_check(1,1,1,2))
