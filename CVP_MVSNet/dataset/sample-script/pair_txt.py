total_num = 69

with open("pair.txt", "a+") as f:
    f.write(str(total_num) + "\n")
    for i in range(total_num):
        f.write(str(i) + "\n")
        top_10 = []
        if i <= 63:
            top_10 = [x for x in range(i-5, i) if x >= 0 and x != i]
            curr = i+1
            while len(top_10) < 10:
                top_10.append(curr)
                curr += 1
        else:
            top_10 = [x for x in range(i+1, 69) if x < 69 and x != i]
            curr = i-1
            while len(top_10) < 10:
                top_10.append(curr)
                curr -= 1

        curr = []
        start = 1000
        while len(curr) < 10:
            curr.append(start)
            start *= 0.75

        f.write("10 " + str(top_10[0]) + " " + str(curr[0]) + " " + str(top_10[1]) + " " + str(curr[1]) + " " + str(top_10[2]) + " " + str(curr[2]) + " " + str(top_10[3]) + " " + str(curr[3]) + " " + str(top_10[4]) + " " + str(curr[4]) + " " + str(top_10[5]) + " " + str(curr[5]) + " " + str(top_10[6]) + " " + str(curr[6]) + " " + str(top_10[7]) + " " + str(curr[7]) + " " + str(top_10[8]) + " " + str(curr[8]) + " " + str(top_10[9]) + " " + str(curr[9]) + "\n")

