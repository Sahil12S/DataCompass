# 1
def countdown( a ):
    retval = []
    for i in range( a, -1, -1 ):
        retval.append( i )
    return retval
print( "1:" )
print( countdown( 5 ) )

# 2
def print_and_return( l ):
    print( l[0] )
    return l[1]

print( "2:" )
print( print_and_return( [1, 2] ) )

# 3
def first_plus_length( l ):
    return l[0] + len( l )

print( "3:" )
print( first_plus_length( [1, 2, 3, 4, 5] ) )

# 4
def values_greater_than_second( l ):
    retval = []
    second_val = l[1]

    for val in l:
        if val > second_val:
            retval.append( val )
    
    print( len( retval ) )
    return retval

print( "4:" )
print( values_greater_than_second( [5, 2, 3, 2, 1, 4] ) )

# 5
def length_and_value( size, value ):
    return [ value ] * size

print( "5:" )
print( length_and_value( 4, 7 ) )