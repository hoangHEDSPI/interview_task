import sys

if __name__=="__main__":
    line_counter = 0
    distance = []
    n_houses = 0
    for line in sys.stdin:
        if line_counter == 0:
            n_houses = int(line)
        else:
            d_house = line.split(" ")
            if len(d_house) > 1:
                distance.append([int(d_house[0]), int(d_house[1])])
            else:
                min_distance = float("inf")
                output = 0
                query = int(line)
                for i in distance:
                    if abs(query - i[1]) < min_distance:
                        min_distance = abs(query - i[1])
                        output = i[0]
                    elif abs(query - i[1]) == min_distance:
                        if output > i[0]:
                            output = i[0]
                print(output)
        line_counter += 1
    
                        
                
