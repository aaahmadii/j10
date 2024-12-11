def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        
        return lines[-n:] if n <= len(lines) else lines

file_path = 'texttam2.txt'  
last_lines = read_last_n_lines(file_path,n)

for line in last_lines:
    print(line.strip())
