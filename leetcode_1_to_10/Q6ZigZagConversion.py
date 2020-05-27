def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    # We'll create list of strings depicting each row. this might help us in making the final output
    list = ["" for i in range(0, numRows)]
    goingDown = True
    currentRow = 0
    for i in range(0, len(s)):
        c = s[i]
        #direction will change at after we are at 0th row or at (n-1) row
        if currentRow == 0:
            goingDown = True
        elif currentRow == numRows-1:
            goingDown = False
        list[currentRow] = list[currentRow] + c
        if goingDown is True:
            currentRow += 1
        else:
            currentRow -= 1
    out = ""
    out = out.join(list)
    return out
print(convert("PAYPALISHIRING", 4))