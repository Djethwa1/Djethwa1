# code to output a star pattern triangle
# top half of triangle has 5 rows, 2 half triangle equals 10 rows
# the number of stars in each row of top half triangle equals the number of rows
# the number of stars in bottom half triangle equates to (10-row number)
# row starts at zero and ends at 10

row_count = 5
start = 0
end = (2 * row_count)
for row_number in range(start, end):
    if row_number <= row_count:
        print(row_number * "*") 
    else:
        print((end - row_number) * "*")
   