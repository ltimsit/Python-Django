from local_lib.path import Path



if __name__=='__main__':
    p = Path("local_lib") / "prog"
    text = ["Bonjour les gens", "comment ca va"]
    p.mkdir_p(755)
    file_path = p / "file.txt"
    file_path.write_lines(text)
    lines = file_path.lines()
    for line in lines:
        print(line, end='')
