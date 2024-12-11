def read_first_n_lines("texttam2.txt" n):
    with open("texttam2.txt", 'r') as file:
        for _ in range(n):
            line = file.readline()
            if not line:       
                break
            print(line.strip())  

read_first_n_lines('example.txt', 5)
